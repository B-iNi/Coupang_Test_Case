import logging
from playwright.sync_api import Page

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="Inquiries_test.log",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

class REVIEW_PAGE:
    def __init__(self, page: Page):
        self.page = page  

    # 리뷰 페이지 열기
    def OPEN_REVIEW_PAGE(self, url):
        logger.info(f"✅ Navigating to review page: {url}")
        self.page.goto(url)  # 리뷰 페이지로 이동
        current_url = self.page.url
        logger.info(f"✅ 현재 URL: {current_url}")
        #https://www.nibbuns.co.kr/shop/reviewmore.html

    # 카테고리 설정
    def CATEGORY_CLICK(self):
        self.page.locator('select[name="category"]').click()
        logger.info("✅ 카테고리 드롭다운 클릭")

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
        
        category_xpath = f'//*[@id="filter_area"]/div/div/div[5]/div/div[3]/div[{category_list[category_name]}]/span'
        self.page.locator(f"xpath={category_xpath}").click()
        logger.info(f"✅ 카테고리 선택: {category_name}")

        