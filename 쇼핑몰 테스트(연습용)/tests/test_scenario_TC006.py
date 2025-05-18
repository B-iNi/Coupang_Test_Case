import pytest
import os
import time
import logging
from selenium import webdriver
from tests.pages.review_page import REVIEW_PAGE


log_file = os.path.join(os.getcwd(), "test_scenario_TC006.log")

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = log_file,
    encoding="utf-8",
    filemode = 'a',
    force=True
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def review_page(driver):
    return REVIEW_PAGE(driver)



# test1. 리뷰페이지 이동
def test_OPEN_REVIEW_PAGE(review_page):
    logger.info("[Test1.] 리뷰페이지 열기")
    review_page.OPEN_REVIEW_PAGE("https://www.nibbuns.co.kr/shop/reviewmore.html")
    current_url = review_page.driver.current_url
    time.sleep(1)
    logger.info("✅[TEST1.] 테스트 완료")
"""(오류)
# test2. 카테고리 별로 보기 기능 확인
def test_REVIEW_PAGE_CATEGORY(review_page):
    logger.info("[Test2.] 카테고리별로 보기")
    review_page.OPEN_REVIEW_PAGE("https://www.nibbuns.co.kr/shop/reviewmore.html")
    current_url = review_page.driver.current_url
    time.sleep(1)

    review_page.CATEGORY_CLICK()
    time.sleep(1)
    review_page.SELECT_CATEGORY("TOP")
    time.sleep(2)
    reviews = review_page.driver.find_elements(By.CLASS_NAME,"sf_review_user_info set_report")

    for review in reviews:
        product_name = review.find_element(By.CLASS_NAME, "sf_review_item_name").text.strip() if review.find_elements(By.CLASS_NAME, "sf_review_item_name") else "상품명없음"
        review_text = review.find_element(By.CLASS_NAME, "sf_review_user_write_review").text.strip() if review.find_elements(By.CLASS_NAME, "sf_review_user_write_review") else "리뷰없음"

        logger.info(f"📌 상품명: {product_name}")
        logger.info(f"💬 리뷰: {review_text}")

        print(f"📌 상품명: {product_name}")
        print(f"💬 리뷰: {review_text}\n")
