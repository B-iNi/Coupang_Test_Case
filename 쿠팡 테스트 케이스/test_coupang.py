import os
import time
import pytest
import logging
from coupang_main import open_site, search_keyword, login_page, go_login

log_file = os.path.join(os.getcwd(),"coupang_test.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="coupang_test.log",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)

# test1. 쿠팡 페이지 연다
def test_open(driver):
    logger.info("[Test1.쿠팡페이지 열기!!]")
    open_site(driver,"http://www.coupang.com")
    time.sleep(1)
    current_url = driver.current_url
    logger.info(f"✅ succese :{current_url}")

# test2. 쿠팡 페이지 열고 검색창으로 검색해봄(비로그인)
def test_open_and_search(driver):
    logger.info("[Test2.쿠팡페이지 열고 검색!!]")
    open_site(driver,"http://www.coupang.com")
    time.sleep(1)
    current_url = driver.current_url
    logger.info(f"현재 페이지 :{current_url}")
    time.sleep(1)
    keyword = "노트북"
    search_keyword(driver,keyword)
    logger.info(f"검색 키워드: {keyword}")
    current_url = driver.current_url
    logger.info(f"✅ succese :{current_url}")
    time.sleep(1)

# test.3 쿠팡 페이지 열고 검색창으로 검색해봄(로그인)
def test_open_and_search_login(driver):
    logger.info("[Test2.쿠팡페이지 열고 검색!!]")
    open_site(driver,"http://www.coupang.com")
    time.sleep(1)
    current_url = driver.current_url
    logger.info(f"현재 페이지 :{current_url}")
    time.sleep(1)
    login_page(driver)
    time.sleep(2)
    ID = "bini3925@nate.com"
    PW = "Qudtlsdk0)"
    go_login(driver,ID,PW)
    time.sleep(3)
    keyword = "노트북"
    search_keyword(driver,keyword)
    logger.info(f"검색 키워드: {keyword}")
    current_url = driver.current_url
    logger.info(f"✅ succese :{current_url}")
    time.sleep(3)