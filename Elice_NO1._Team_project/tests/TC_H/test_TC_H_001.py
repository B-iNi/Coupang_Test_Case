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


@pytest.mark.usefixtures("driver")
class Test_CASE_H_01:
    def test_case_H_01(self, driver:WebDriver):
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

            logging.info("TC_H_01")


            team_feed_team = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span'))).text
        

            assert my_team == team_feed_team  , "팀이 다릅니다"


            logging.info("TC_H_01 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

