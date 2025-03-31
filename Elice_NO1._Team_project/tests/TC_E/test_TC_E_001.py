import os
import sys
import selenium
import time
import random
import pytest
import faker
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains  # 연속 동작 수행 (예: 드래그 앤 드롭)
from selenium.webdriver.common.keys import Keys  # 키보드 입력 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.loginPage import LoginPage
from src.pages.team_dinner import TeamDinner



logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = 'test_03_06.log',
    encoding = 'utf-8',
    force='a'
    
)
logger = logging.getLogger(__name__)


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://kdt-pt-1-pj-2-team03.elicecoding.com")
    yield driver
    driver.quit()



def test_case005_1(setup):
    driver = setup
    team_dinner = TeamDinner(driver)
    login_page = LoginPage(driver)
    logging.info("\n[Test_E_001. Start!]")
    login_page.input_password_and_email()
    
    # 메인에서 회식하기 버튼 검증
    TEAM_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[3]')))
    assert TEAM_BUTTON.is_displayed(),"❌'📅회식하기' 버튼 오류"
    logging.info("✅ '📅회식하기' 버튼 정상 출력")


    # 회식하기 페이지 이동
    team_dinner.go_team_dinner()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
    assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
    logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")


    # 카테고리 버튼 검증                                
    categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
    assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
    logging.info("✅ 카테고리 버튼 정상 출력")
