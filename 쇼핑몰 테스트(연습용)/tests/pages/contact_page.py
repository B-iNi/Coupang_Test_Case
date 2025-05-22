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

class ContactPage: 
    def __init__(self, page: Page):
        self.page = page  

    # 실행 문의 페이지 열기
    def open_inquiries_page(self, url: str): 
        logger.info(f"✅ Navigating to inquiries page: {url}")
        self.page.goto(url)  
        current_url = self.page.url
        logger.info(f"✅ 현재 URL: {current_url}")

    # 글쓰기 버튼 클릭
    def click_writing_button(self): 
        self.page.locator('xpath=//*[@id="bbsData"]/div/dl[1]/dd/a').click()
       
        logger.info("✅ 글쓰기 페이지 이동")

    # NAME 입력
    def fill_name(self, name: str): 
        name_input_locator = self.page.locator('xpath=//*[@id="bw_input_writer"]')
        name_input_locator.fill(name)
        logger.info(f"✅ NAME 입력: {name}")

    # PASSWORD 입력
    def fill_password(self, password: str): 
        password_input_locator = self.page.locator('xpath=//*[@id="bw_input_passwd"]')
        password_input_locator.fill(password)
        logger.info(f"✅ PASSWORD 입력: {password}")

    # '일반문의' 선택
    def select_title_normal(self): 
        self.page.locator("#subhead").select_option(index=1)
        
        logger.info("✅ '일반문의' 선택")

    # '해외배송' 선택
    def select_title_overseas(self): 
        self.page.locator("#subhead").select_option(index=2)
       
        logger.info("✅ '해외배송' 선택")

    # '상품문의' 선택
    def select_title_product_inquiry(self): 
        self.page.locator("#subhead").select_option(index=3)
    
        logger.info("✅ '상품문의' 선택")

    # '입금확인' 선택
    def select_title_check_wages(self): 
        self.page.locator("#subhead").select_option(index=4)
        
        logger.info("✅ '입금확인' 선택")

    # 작성 완료 버튼 클릭
    def click_writing_complete_button(self): 
        self.page.locator('xpath=//*[@id="bbsData"]/div/div[3]/form/dl/dd/a[1]').click()
        logger.info("✅ '작성 완료' 클릭")

    # 목록으로 돌아가기 버튼 클릭
    def click_back_to_list_button(self): 
        self.page.locator('xpath=//*[@id="bbsData"]/div/div[3]/form/dl/dd/a[2]').click()
        logger.info("✅ 목록으로 돌아가기")
