import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.recommendation_page import RecommendationPage
from src.pages.loginPage import LoginPage
import random
import logging


@pytest.mark.usefixtures("driver")
class Test_CASE_G_05:
    def test_case_G_05(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)


            logging.info("TC_G_05")

            while True:
                percent_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'inline-flex') and contains(@class, 'bg-sub')]")))
                percent_text = percent_element.text.strip().replace("%", "")
                percent_value = float(percent_text)

                if percent_value >= 45 :
                    logging.info("적합도 %d%% (기준 충족)", percent_value)
                    break

                rcm.refresh_recommendation()
                logging.info("적합도 %d%% (기준 미달, 재추천)", percent_value)
                time.sleep(2)


            logging.info("TC_G_05 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")
