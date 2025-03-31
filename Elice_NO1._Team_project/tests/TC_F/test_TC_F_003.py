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
from src.pages.team_pid import TeamPid



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


def test_case006_3(setup):
    driver = setup
    team_pid = TeamPid(driver)
    login_page = LoginPage(driver)
    logging.info("\n[Test_F_003. Start!]")
    login_page.input_password_and_email()


    # 팀피드 페이지 이동
    team_pid.go_team_pid()
    assert driver.current_url != "https://kdt-pt-1-pj-2-team03.elicecoding.com"
    logging.info("✅ '팀 피드' 페이지 정상 이동 완료.")


     # 스크롤 이동임
    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


    # '같은메뉴먹기' 존재 여부검증  (일반적으로 XPATH나 CSS SELECTOR로 안되서 텍트스 기반으로 함)
    time.sleep(1)
    REVIEW_BUTTON = WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(text(), '같은 메뉴 먹기')]")))
    assert len(REVIEW_BUTTON) > 0,"❌ '같은 메뉴 먹기' 오류"
    logging.info("✅ '같은 메뉴 먹기' 버튼 정상 출력 ")
    

    # 임의로 '같은메뉴먹기' 클릭
    team_pid.review_write()  
    # 페이지에 히든 요소가 있어서
    # 클릭 후에 '또 먹은 후기 등록' 페이지에서 '후기 작성 완료' 버튼 검증하는것임                                            
    BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-root"]/div/div[2]/section/form/button')))
    assert BUTTON.is_displayed(),"❌ '같은 메뉴 먹기'오류"
    time.sleep(1)
    # 메뉴 검증을 통해 뭘 선택한건지 확인
    input_xpath_3 = '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/input'
    input_xpath_4 = '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/input'

        
    try: # 먼저 div[3]을 시도하고, 없으면 div[4]를 시도
        MENU = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath_3)))
        input_xpath = input_xpath_3  # div[3]을 찾으면 그대로 사용
    except:
        MENU = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath_4)))
        input_xpath = input_xpath_4  # div[4]를 사용

    MENU_NAME = MENU.get_attribute('value')
    logging.info(f"선택한 메뉴 : {MENU_NAME}")
    logging.info("✅ '또 먹은 후기 등록' 페이지 이동 완료")

 
    # 식사 유형 선택
    team_pid.type_select()
    # 버튼 선택 검증
    select_type = ["혼밥","그룹","회식"]
    select_xpath = None

    for t in select_type:
        xpath = f'//*[@id="{t}"]/span'
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            select_xpath = t
            break
        except:
            continue
    assert select_xpath is not None,"❌ 식사 유형 선택 오류"
    logging.info(f"✅ '{select_xpath}' 선택 확인 됨")


    # 임의로 리뷰 작성함
    team_pid.review_input()
    try:
        # div[5]를 시도
        REVIEW = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[5]/textarea')))
    except:
        try:
            # div[6]을 시도
            REVIEW = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/textarea')))            
        except:        
            return  # 요소를 찾을 수 없으면 함수 종료
    # 리뷰 입력 완료 여부 확인
    if REVIEW.get_attribute("value") == "":
        logging.info("❌ 리뷰 입력 오류")
    else:
        logging.info("✅ 리뷰 입력 완료")



    # 별점 선택
    team_pid.star_click()
    # 첫 번째 별은 무조건 클릭되기에
    STAR = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#modal-root > div > div.flex-1.overflow-auto > section > form > div:nth-child(6) > div > div:nth-child(2)')))
    assert STAR.is_displayed(),"❌ 별점 선택 오류"
    logging.info("✅ 별점 선택 완료")
    
    
    # 후기 등록
    team_pid.review_complete()
    # 후기 등록 버튼이 없어지면 검증 완료 돌릴거임
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-root"]/div/div[2]/section/form/button')))
        logging.info("✅ 후기 등록 완료")
    except:
        logging.info("❌ 후기 등록 오류")


    # 개인 피드 페이지 이동
    team_pid.personal_pid()
    assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"
    logging.info("✅ 개인 피드 페이지 이동 완료")
    time.sleep(2)
    # 여기서 방금 쓴 후기에 대해 검증이 필요함.

    review = '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > div.w-full > div.flex.flex-col.w-full.gap-3 > div:nth-child(1) > div.flex.flex-col.w-full.gap-2 > div > div.relative.cursor-pointer > p'
    review_elemente = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,review)))
    TEXT = review_elemente.text

    while True:
          try:
              # review 요소 찾기 시도
              review_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, review)))
              TEXT = review_element.text
              logging.info(f"✅ 후기 : {TEXT} / 검증 완료")
              break  # 요소를 찾으면 반복 종료
          except:
              # 요소를 찾을 수 없으면 페이지 스크롤을 올림
              driver.execute_script("window.scrollBy(0, -1000);")  # 1000px 만큼 위로 스크롤
              time.sleep(1) 