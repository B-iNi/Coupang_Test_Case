import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="Inquiries_test.log",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

class ConTact_Page:
    def __init__(self, driver):
        self.driver = driver  # 클래스 내에서 사용할 WebDriver 인스턴스

    # 실행 문의 페이지 열기
    def OPEN_INQUIRIES_PAGE(self, url):
        logger.info("✅ Chrome Driver Start")
        self.driver.get(url)  # 문의 페이지로 이동
        time.sleep(2)
        current_url = self.driver.current_url
        logger.info(f"✅ 현재 URL: {current_url}")

    # 글쓰기 버튼 클릭
    def CLICK_WRITING_BUTTON(self):
        self.driver.find_element(By.XPATH, '//*[@id="bbsData"]/div/dl[1]/dd/a').click()
        time.sleep(2)
        logger.info("✅ 글쓰기 페이지 이동")

    # NAME 입력
    def WRITING_NAME(self, name):
        writing_name = self.driver.find_element(By.XPATH, '//*[@id="bw_input_writer"]')
        time.sleep(2)
        writing_name.send_keys(name)
        logger.info(f"✅ NAME 입력: {name}")

    # PASSWORD 입력
    def WRITING_PASSWORD(self, password):
        writing_password = self.driver.find_element(By.XPATH, '//*[@id="bw_input_passwd"]')
        time.sleep(2)
        writing_password.send_keys(password)
        logger.info(f"✅ PASSWORD 입력: {password}")

    # '일반문의' 선택
    def TITLE_NOMAL(self):
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]/option[2]').click()
        logger.info("✅ '일반문의' 선택")

    # '해외배송' 선택
    def TITLE_OVERSEAS(self):
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]/option[3]').click()
        logger.info("✅ '해외배송' 선택")

    # '상품문의' 선택
    def TITLE_PRODUCT_INQUIRY(self):
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]/option[4]').click()
        logger.info("✅ '상품문의' 선택")

    # '입금확인' 선택
    def TITLE_CHECK_WAGES(self):
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="subhead"]/option[5]').click()
        logger.info("✅ '입금확인' 선택")

    # 작성 완료 버튼 클릭
    def WRITING_END_BUTTON(self):
        self.driver.find_element(By.XPATH, '//*[@id="bbsData"]/div/div[3]/form/dl/dd/a[1]').click()
        logger.info("✅ '작성 완료' 클릭")

    # 목록으로 돌아가기 버튼 클릭
    def WRITING_BACK(self):
        self.driver.find_element(By.XPATH, '//*[@id="bbsData"]/div/div[3]/form/dl/dd/a[2]').click()
        logger.info("✅ 목록으로 돌아가기")
