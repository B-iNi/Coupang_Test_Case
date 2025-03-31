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
class Test_CASE_H_02:
    def test_case_H_02(self, driver:WebDriver):
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

            logging.info("TC_H_02")


            first_team = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span'))).text


            team_select_btn =wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  #팀 선택 버튼
            team_select_btn.click() 

            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))   #눌렀을떄 뜨는 팀 목록
            random_not_first_team = [option for option in teams_options if first_team not in option.text] # 내 팀 제외
            selected_not_first_team = random.choice(random_not_first_team) # 내 팀 제외 랜덤 선택
            selected_not_first_team.click()

            second_team = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span'))).text
        

            assert second_team != first_team , "팀이 다릅니다"


            logging.info("TC_H_02 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")
