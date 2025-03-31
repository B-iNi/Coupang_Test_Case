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
from src.pages.solo_eat import SoloEat
from src.pages.loginPage import LoginPage


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


def test_case003_1(setup):
    driver = setup
    solo_eat = SoloEat(driver)
    login_page = LoginPage(driver)
    logging.info("\n[Test_C_001. Start!]")

    login_page.input_password_and_email()
    #time.sleep(2)

    # 메인에서 혼자먹기 버튼 검증
    SOLO_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]')))
    assert SOLO_BUTTON.is_displayed(),"❌'👤혼자먹기' 버튼 오류"
    logging.info("✅ '👤혼자먹기' 버튼 정상 출력")
    
    # 메인에서 혼자먹기 페이지 이동
    solo_eat.go_solo_eat()
    # 페이지 이동에 대한 검증
    WebDriverWait(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"))
    assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone","❌혼자먹기 페이지 이동 오류"
    logging.info("✅ '👤혼자먹기' 페이지 정상 이동 완료.") #최적화 완

    # 카테고리 버튼 검증
    categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
    assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
    logging.info("✅ 음식 카테고리 버튼 정상 출력")

    # 임의의 음식 카테고리 선택
    solo_eat.category_select()
    # 카테고리 선택에 대한 검증
    CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
    assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"

