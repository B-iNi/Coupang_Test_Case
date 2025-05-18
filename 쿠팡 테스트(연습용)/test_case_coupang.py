import os
import time
import pytest
import logging
from coupang_main import open_site, search_keyword, login_page, go_login, get_item, putin_item, go_item_bag



log_file = os.path.join(os.getcwd(), "Test.log")

# logging 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=log_file,  # 상대 경로 사용
    filemode='a',  # 기존 로그에 이어서 기록
    encoding="utf-8",
    force=True
)

logger = logging.getLogger(__name__)




##### 한 글자씩 입력하게 하려고 함
def type_like_human(element,text,delay=1.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

"""
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
    logger.info("[Test3.쿠팡페이지 열고 로그인 후 검색!!]")
    open_site(driver,"http://www.coupang.com")
    time.sleep(1)
    current_url = driver.current_url
    logger.info(f"현재 페이지 :{current_url}")
    time.sleep(1)
    login_page(driver)
    time.sleep(2)
    ID = "00000"
    PW = "00000"
    go_login(driver,ID,PW)
    logger.info("[로그인 성공]")
    time.sleep(3)
    keyword = "노트북"
    search_keyword(driver,keyword)
    logger.info(f"검색 키워드: {keyword}")
    current_url = driver.current_url
    logger.info(f"✅ succese :{current_url}")
    time.sleep(3)
"""
# test.4 임의 제품 페이지에서 클릭 해서 장바구니 넣고 수량 조절해 보기
def test_open_get_item(driver):
    logger.info("[Test4.임의 상품 검색 페이지에서 장바구니에 넣고 수량 조절!!]")
    open_site(driver,"https://www.coupang.com/np/search?component=&q=%EC%95%A0%ED%94%8C%EC%9B%8C%EC%B9%98&channel=user")
    time.sleep(1)
    current_url = driver.current_url
    logger.info(f"현재 상품 페이지 :{current_url}")
    time.sleep(2)
    get_item(driver)
    current_url = driver.current_url
    logger.info(f"상세 페이지로 이동 {current_url}")
    time.sleep(1)
    putin_item(driver)
    logger.info("장바구니에 넣기 완료")
    time.sleep(1)
    go_item_bag(driver)
    time.sleep(2)
    current_url = driver.current_url
    logger.info(f"장바구니로 이동 {current_url}")


    
