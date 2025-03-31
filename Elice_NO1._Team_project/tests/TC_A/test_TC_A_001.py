import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from pages.loginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

class TestCase_A:
    def test_Case_A_01(self, driver:WebDriver):
        try:
            driver = webdriver.Chrome()

            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(5)

            login_page.input_password_and_email()
            time.sleep(5)

            ws(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/"))  # URL 변경 확인
            assert driver.save_screenshot("로그인-메인페이지-성공.jpg")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False
