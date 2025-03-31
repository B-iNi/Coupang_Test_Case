import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
import logging


@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_02(self, driver:WebDriver):
        try : 
            #Test 시작
            logging.info("[테스트 시작] 회원가입 프로세스를 시작합니다.")
            signupPage = SignupPage(driver)
            wait = ws(driver, 10)
            faker = Faker()

            signupPage.open()
            time.sleep(3)
            logging.info("회원가입 페이지 열기 완료")
            signupPage.go_signup()
            time.sleep(3)
            logging.info("회원가입 폼으로 이동 완료")

            email, password=signupPage.generate_random_email_and_password()
            logging.info("이메일 : %s, 비밀번호 %s", email, password)
            time.sleep(3)

            signupPage.fill_signup_form(email,password)
            time.sleep(3)
            logging.info("이메일 및 비밀번호 입력 완료")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

