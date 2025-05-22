import pytest
import os
import logging
from tests.pages.review_page import REVIEW_PAGE
from playwright.sync_api import Page, expect


log_file = os.path.join(os.getcwd(), "test_scenario_TC006.log")

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = log_file,
    encoding="utf-8", # 파일 모드를 'a' (append)로 설정하는 것이 좋습니다.
    filemode = 'a',
    force=True
)
logger = logging.getLogger(__name__)

@pytest.fixture
def review_page(page: Page):
    # Playwright의 page fixture를 REVIEW_PAGE에 전달합니다.
    return REVIEW_PAGE(page)

# 참고: REVIEW_PAGE 클래스의 CATEGORY_CLICK 메서드는 사용되지 않는 것으로 보입니다.


# test1. 리뷰페이지 이동
def test_OPEN_REVIEW_PAGE(review_page):
    logger.info("[Test1.] 리뷰페이지 열기")
    review_page.OPEN_REVIEW_PAGE("https://www.nibbuns.co.kr/shop/reviewmore.html")
    # Playwright의 expect를 사용하여 URL 검증
    expect(review_page.page).to_have_url("https://www.nibbuns.co.kr/shop/reviewmore.html")
    time.sleep(1)
    logger.info("✅[TEST1.] 테스트 완료")
"""(오류)
# test2. 카테고리 별로 보기 기능 확인
def test_REVIEW_PAGE_CATEGORY(review_page):
    logger.info("[Test2.] 카테고리별로 보기")
    review_page.OPEN_REVIEW_PAGE("https://www.nibbuns.co.kr/shop/reviewmore.html")
    expect(review_page.page).to_have_url("https://www.nibbuns.co.kr/shop/reviewmore.html")
    # time.sleep(1) # Playwright auto-waiting으로 대부분 불필요

    # review_page.CATEGORY_CLICK() # 이 메서드는 사용되지 않는 것으로 보입니다.
    # time.sleep(1) # Playwright auto-waiting으로 대부분 불필요
    review_page.SELECT_CATEGORY("TOP")
    # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

    reviews = review_page.driver.find_elements(By.CLASS_NAME,"sf_review_user_info set_report")

    for review in reviews:
        product_name = review.find_element(By.CLASS_NAME, "sf_review_item_name").text.strip() if review.find_elements(By.CLASS_NAME, "sf_review_item_name") else "상품명없음"
        review_text = review.find_element(By.CLASS_NAME, "sf_review_user_write_review").text.strip() if review.find_elements(By.CLASS_NAME, "sf_review_user_write_review") else "리뷰없음"

        logger.info(f"📌 상품명: {product_name}")
        logger.info(f"💬 리뷰: {review_text}")

        print(f"📌 상품명: {product_name}")
        print(f"💬 리뷰: {review_text}\n") # 이 부분은 Playwright 로케이터로 변경 필요

    # Playwright 로케이터로 변경 예시:
    # review_locators = review_page.page.locator(".sf_review_user_info.set_report").all()
    # for review_locator in review_locators:
    #     # Playwright는 find_element 대신 locator를 사용합니다.
    #     # text_content()는 요소의 텍스트를 가져옵니다.
    #     product_name = review_locator.locator(".sf_review_item_name").text_content().strip() if review_locator.locator(".sf_review_item_name").count() > 0 else "상품명없음"
    #     review_text = review_locator.locator(".sf_review_user_write_review").text_content().strip() if review_locator.locator(".sf_review_user_write_review").count() > 0 else "리뷰없음"
    #     logger.info(f"📌 상품명: {product_name}")
    #     logger.info(f"💬 리뷰: {review_text}")
    #     print(f"📌 상품명: {product_name}")
    #     print(f"💬 리뷰: {review_text}\n")
