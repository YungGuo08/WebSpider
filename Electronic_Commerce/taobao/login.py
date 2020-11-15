import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def login():
    try:
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })
        driver.get('https://login.taobao.com/')
        user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#fm-login-id')))
        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#fm-login-password')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-form > div.fm-btn > button')))
        user.clear()
        user.send_keys('') # 用户名
        password.clear()
        password.send_keys('') # 密码
        submit.click()
        print('登录成功！')
    except TimeoutException:
        login()
    cookies = driver.get_cookies()
    # print(cookies)
    return cookies


def save_cookie(cookies):
    with open('login_cookie.txt', 'w') as f:
        f.write(json.dumps(cookies))


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    # driver.maximize_window()
    print('登录中...')
    cookies = login()
    save_cookie(cookies)
    driver.close()
