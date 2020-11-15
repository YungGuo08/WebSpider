import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
from pymongo import MongoClient
from tqdm import tqdm
import time


def slide():
    # 滑动验证
    slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nc_1_n1z')))
    ActionChains(driver).click_and_hold(slider).perform()
    for i in range(0, 4):
        ActionChains(driver).move_to_element_with_offset(slider, 100, 15).perform()
        time.sleep(0.5)
    ActionChains(driver).release()
    result = EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#nocaptcha > div > span > a'), '刷新')
    if result:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nocaptcha > div > span > a'))).click()
        # time.sleep(1800)
    else:
        print('滑动验证完成！')


def turn_page(page):
    # 翻页
    if page > 1:
        input_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
        input_page.clear()
        input_page.send_keys(page)
        submit.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist  .items .item')))
    get_products(page)


def get_page(page):
    try:
        url = 'https://s.taobao.com/search?q=' + quote(keyword)
        # print(url)
        driver.get('https://s.taobao.com/')
        with open('login_cookie.txt', 'r') as f:
            cookies = json.loads(f.read())
        for cookie in cookies:
            cookie_dict = {
                'domain': '.taobao.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'path': '/',
                'expires': cookie.get('expires'),
                'sameSite': 'None',
                'secure': cookie.get('secure')
            }
            driver.add_cookie(cookie_dict)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })
        driver.get(url)
        title = driver.title
        if len(title) > 0:
            if title == 'security-X5':
                print('需要滑动验证！')
                # time.sleep(1800)
                slide()
                turn_page(page)
            else:
                turn_page(page)
        else:
            print('cookie已失效，请重新获取！')
            driver.close()
            exit()
    except TimeoutException:
        get_page(page)


def get_products(page):
    html = driver.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in tqdm(items, f'保存第{page}页进度'):
        product = {
            # 商品id
            'nid': item.find('.pic .pic-link').attr('data-nid'),
            # 标题
            'title': item.find('.title').text(),
            # 价格
            'price': item.find('.price').text(),
            # 月销量
            'deal': item.find('.deal-cnt').text(),
            # 商品图片
            'image': item.find('.pic .img').attr('data-src'),
            # 商品链接
            'commodity_url': item.find('.pic .pic-link').attr('href'),
            # 店铺
            'shop': item.find('.shop').text(),
            # 店铺类型
            'type': item.find('.icons a').attr('title'),
            # 地址
            'location': item.find('.location').text()
        }
        collection.update_one({'nid': product['nid']}, {'$setOnInsert': product}, upsert=True)
        # collection.insert_one(product)


def main():
    for i in range(1, 101):
        get_page(i)
    driver.close()


if __name__ == '__main__':
    # 初始化mongodb
    client = MongoClient()
    db = client.Taobao
    collection = db.taobao
    # 开启无界面浏览器
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    # driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    keyword = 'iPad'
    main()
