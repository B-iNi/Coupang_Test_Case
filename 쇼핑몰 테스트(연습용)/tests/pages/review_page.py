import os
import time
import logging
from playwright.sync_api import Page

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="Inquiries_test.log",
    encoding="utf-8", # 파일 모드를 'a' (append)로 설정하는 것이 좋습니다.
    filemode='a'
)
logger = logging.getLogger(__name__)

class REVIEW_PAGE:
    def __init__(self, page: Page):
        self.page = page  # 클래스 내에서 사용할 Playwright Page 인스턴스

    # 리뷰 페이지 열기
    def OPEN_REVIEW_PAGE(self, url):
        logger.info("✅ Chrome Driver Start")
        self.driver.get(url)  # 리뷰 페이지로 이동
        time.sleep(2)
        current_url = self.driver.current_url
        logger.info(f"✅ 리뷰 페이지 URL: {current_url}")
        #https://www.nibbuns.co.kr/shop/reviewmore.html

    # 카테고리 설정
    # 이 메서드는 사용되지 않는 것으로 보이며, SELECT_CATEGORY와 기능이 겹칩니다.
    def CATEGORY_CLICK(self):
        category_button = self.driver.find_element(By.CSS_SELECTOR,'select[name="category"]').click()

    # 카테고리 설정(TOP)
    def SELECT_CATEGORY(self,category_name: str):
        category_list = {
            "TOP": 2,
            "BLOUSE": 3,
            "DRESS": 4,
            "PANTS": 5,
            "SKIRT": 6,
            "OUTER": 7,
            "BAG": 8,
            "ACC": 9, 
            "INNER": 10,
            "OUTLET": 11,
            "SELF_PAGE": 12,
            "OUTLET2": 13,
            "NEW_ITEM": 14,
            "PROMOTION": 15,
            "BEST": 16
        }
        if category_name not in category_list:
            raise ValueError(f"잘못된 카테고리{category_name}")
        
        # Playwright는 XPath도 지원하지만, CSS 선택자가 가능한 경우 더 안정적일 수 있습니다.
        # 현재 XPath를 그대로 사용합니다.
        category_locator = self.page.locator(f'xpath=//*[@id="filter_area"]/div/div/div[5]/div/div[3]/div[{category_list[category_name]}]/span')
        category_locator.click()
        logger.info(f"카테고리 설정{category_name}")
        
