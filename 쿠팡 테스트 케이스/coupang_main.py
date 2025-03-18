import os
import time
import selenium
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="exe.log",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)
"""

# ✅ Chrome 옵션 설정
def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("detach", True)  # ✅ 브라우저 자동 종료 방지
    return chrome_options

# ✅ WebDriver 실행
def driver_init():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=get_chrome_options())
    return driver


##### 한 글자씩 입력하게 하려고 함
def type_like_human(element,text,delay=1.3):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

        
####쿠팡 기준으로 할거임####

# 1.) 사이트 이동
def open_site(driver,url):
    driver.get(url) # 사이트 열기

# 1-1.) 검색창에 키워드 입력하고 엔터
def search_keyword(driver,KEYWORD):
    SEARCH_BOX = driver.find_element(By.XPATH,'//*[@id="headerSearchKeyword"]')
    time.sleep(1)
    SEARCH_BOX.send_keys(KEYWORD)
    driver.find_element(By.XPATH,'//*[@id="headerSearchBtn"]').click()


# 2.) 홈에서 로그인 페이지로..
def login_page(driver):
    driver.find_element(By.XPATH,'//*[@id="login"]/a').click()
    time.sleep(2)


# 2-1.) 로그인 하기
def go_login(driver,ID,PW):
    ID_BOX = driver.find_element(By.XPATH,'//*[@id="login-email-input"]')
    ID_BOX.send_keys(ID)
    time.sleep(2)
    PW_BOX = driver.find_element(By.XPATH,'//*[@id="login-password-input"]')
    PW_BOX.send_keys(PW)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="memberLogin"]/div[1]/form/div[5]/button').click()
# 로그인 페이지(https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F)


# 3-1.) 상세페이지 이동
def get_item(driver):
    driver.find_element(By.XPATH,'//*[@id="8336500238"]/a/dl/dt/img').click()
    time.sleep(5)
# 3-2.) 장바구니 넣기 클릭
def putin_item(driver):
    driver.find_element(By.XPATH,'//*[@id="contents"]/div[2]/div[1]/div[3]/div[8]/div[2]/div[2]/div/button[1]').click()
    time.sleep(5)
# 3-3.) 장바구니 아이콘 클릭
def go_item_bag(driver):    
    driver.find_element(By.XPATH,'//*[@id="header"]/section/div[1]/ul/li[2]/a/span[1]').click()

    

if __name__ == "__main__":
    driver = driver_init() 
    get_item(driver)
    driver.quit()  # 브라우저 닫기


