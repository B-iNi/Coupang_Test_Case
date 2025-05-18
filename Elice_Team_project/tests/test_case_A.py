import time
import pytest
import logging
from faker import Faker
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.loginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver")
class TestCase_A:
    def test_Case_A_01(self, driver:WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(1)

            email="team2@example.co.kr"
            password="Team2@@@"
            login_page.input_password_and_email(email,password)
            time.sleep(1)

            ws(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/"))  # URL 변경 확인
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/"

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

    def test_Case_A_02(self, driver:WebDriver):
        try:
            logging.info("로그인 비밀번호 찾기를 시작합니다.")
            faker = Faker()
            email = faker.email() 
            reset_password = ResetPasswordPage(driver)

            reset_password.open()
            time.sleep(1)

            reset_password.reset_password()
            logging.info("'비밀번호를 잊으셨나요?' 버튼을 클릭합니다.")
            time.sleep(1)

            reset_password.fill_email_form(email)
            logging.info("이메일 입력 / '계속' 버튼을 클릭합니다.") 
            time.sleep(1)

            wait = ws(driver, 10)

            wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Resend email')]"))
            )
            logging.info("로그인 비밀번호 찾기를 종료합니다.")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False
