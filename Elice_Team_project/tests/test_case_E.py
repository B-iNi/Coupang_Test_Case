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


class TestCaseE:
    def test_Case_E_01(self,setup):
        driver = setup
        team_dinner = TeamDinner(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_E_001. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


        
        # 메인에서 회식하기 버튼 검증
        TEAM_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[3]')))
        assert TEAM_BUTTON.is_displayed(),"❌'📅회식하기' 버튼 오류"
        logging.info("✅ '📅회식하기' 버튼 정상 출력")
    
    
        # 회식하기 페이지 이동
        TEAM_BUTTON.click()
        logging.info("🔍 회식하기 페이지 이동중...")
        WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")
    
    
        # 카테고리 버튼 검증                                
        categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
        assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
        logging.info("✅ 카테고리 버튼 정상 출력")



    def test_Case_E_02(self,setup):
        driver = setup
        team_dinner = TeamDinner(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_E_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


    
        # 회식하기 페이지 이동
        team_dinner.go_team_dinner()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")
    
    
        # 먹는 인원(팀)에 대한 검증
        USER_TEAM = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/span')))
        assert USER_TEAM.is_displayed(),"❌먹는 인원 오류"
        logging.info(f"🙌먹는 인원 : {USER_TEAM.text}")
        logging.info("✅ 소속 팀 정상 출력")
                                                 
        # 카테고리 설정
        team_dinner.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")    



    def test_Case_E_03(self,setup):
        driver = setup
        team_dinner = TeamDinner(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_E_003. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


    
         # 회식하기 페이지 이동
        team_dinner.go_team_dinner()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")
    
    
        # 카테고리 설정
        team_dinner.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")
    
            
        # 선택완료
        team_dinner.choice_complete()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
        logging.info("✅ 선택완료")
        
    
        # 추천 메뉴와 맛집 리스트 검증
        recommand_menu = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/span/span')))
        assert recommand_menu.is_displayed(),"❌ 메뉴추천 오류"
        logging.info("✅ 정상 출력")
        logging.info(f"✅ 추천 메뉴 : {recommand_menu.text}")
        menu_image = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/div/img')))
        
        if menu_image:
            logging.info("✅ 메뉴 사진 정상 출력")
        else:
            logging.error("❌메뉴 사진 오류")
    
        recommand = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[2]/span')
        recommand_list = driver.find_elements(By.CLASS_NAME,"swiper-slide")
    
        logging.info(f"{recommand.text} : {len(recommand_list)}개의 맛집 발견")
        
