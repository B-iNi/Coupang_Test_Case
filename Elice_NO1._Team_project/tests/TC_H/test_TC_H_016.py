import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage
import random
import logging
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("driver")
class Test_CASE_H_16:
    def test_case_H_16(self, driver:WebDriver):
        try:

            wait = ws(driver, 10)
            login=LoginPage(driver)
            team=TeamPage(driver)

            logging.info("Preconditon")


            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            my_team= team.my_team()
            logging.info("내 팀 : %s",my_team)

            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("TC_H_16")

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            bad_comment =''.join(comment_hangul_chars)
            bad_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='cons']")))
            bad_input.clear()
            bad_input.send_keys(bad_comment)

            time.sleep(2)



            logging.info("TC_H_16 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

