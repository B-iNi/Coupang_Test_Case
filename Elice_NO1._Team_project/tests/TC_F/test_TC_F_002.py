import time
import pytest
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver import ActionChains  # 연속 동작 수행 (예: 드래그 앤 드롭)
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.loginPage import LoginPage
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

class TestCaseF:
    def test_case006_2(self,setup):
        driver = setup
        team_pid = TeamPid(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_F_002. Start!]")
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
