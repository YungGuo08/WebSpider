import requests
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from pymongo import MongoClient
from tqdm import tqdm


def get_page():
    driver.set_page_load_timeout(10)
    page = 1
    size = 1
    for i in range(100):
        try:
            driver.get(f'https://search.jd.com/Search?keyword={keyword}&page={page}&s={size}')
        except TimeoutException:
            driver.execute_script('window.stop();')
            driver.refresh()
        driver.execute_script('window.scrollTo(0,10000)')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList .gl-item')))
        time.sleep(1)
        get_products(i)
        page += 2
        size += 50


def get_comment(sku):
    try:
        comment_url = f'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={sku}'
        response = requests.get(comment_url, headers=headers)
        # print(response)
        if response.status_code == 200:
            comment_number = response.json()['CommentsCount'][0]['CommentCount']
            return comment_number
    except requests.ConnectionError:
        get_comment(sku)


def get_products(i):
    html = driver.page_source
    # print(html)
    doc = pq(html)
    items = doc('#J_goodsList .gl-item').items()
    # print(items)
    for item in tqdm(items, f'第{i + 1}页：'):
        sku_id = item.attr('data-sku')
        # print(sku_id)
        comment_number = get_comment(sku_id)
        image = item.find('.p-img a img').attr('src')
        image = item.find('.p-img a img').attr('data-lazy-img') if image is None else image
        product = {
            'sku_id': sku_id,
            'title': item.find('.p-name em').text().replace('\n', ' '),
            'price': item.find('.p-price i').text(),
            'comment': comment_number,
            'shop': item.find('.p-shop .curr-shop').text(),
            'type': item.find('.p-icons .goods-icons').text(),
            'image': image,
            'link': item.find('.p-name a').attr('href')
        }
        # print(product)
        collection.update_one({'sku_id': sku_id}, {'$setOnInsert': product}, upsert=True)


if __name__ == '__main__':
    client = MongoClient()
    db = client.jd
    collection = db.jingdong
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    keyword = 'iPad'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    get_page()
