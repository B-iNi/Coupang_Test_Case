import pytest
import logging
from selenium import webdriver  # 브라우저 제어
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

class TestCaseC:
    def test_TC_C_001(self,setup):
        driver = setup
        solo_eat = SoloEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_C_001. Start!]")

        login_page.input_password_and_email()


        # 메인에서 혼자먹기 버튼 검증
        SOLO_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]')))
        assert SOLO_BUTTON.is_displayed(),"❌'👤혼자먹기' 버튼 오류"
        logging.info("✅ '👤혼자먹기' 버튼 정상 출력")

        # 메인에서 혼자먹기 페이지 이동
        SOLO_BUTTON.click()
        logging.info("🔍 혼자먹기 페이지 이동중...")

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

    
    def test_TC_C_002(self,setup):
        driver = setup
        solo_eat = SoloEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_C_002. Start!]")
        login_page.input_password_and_email()

        # 메인에서 혼자먹기 페이지 이동 
        solo_eat.go_solo_eat()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone","❌혼자먹기 페이지 이동 오류"
        logging.info("✅ '👤혼자먹기' 페이지 정상 이동 완료.")

        # 먹는 인원에 대한 검증
        USER_PROFILE = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div')))
        assert USER_PROFILE[0].is_displayed(),"❌먹는 인원 오류"
        logging.info(f"🙌먹는 인원 : {len(USER_PROFILE)} 명")
        logging.info("✅ 유저 프로필 정상 출력")
        USER_NAME = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/div[1]')))
        assert USER_NAME.is_displayed(),"❌유저 이름 오류"
        USER_TEAM = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/div[2]')))
        assert USER_TEAM.is_displayed(),"❌유저 소속 팀 오류"
        logging.info(f"\n 이름 : {USER_NAME.text}\n 소속 팀 : {USER_TEAM.text}")


    def test_TC_C_003(self,setup):
        driver = setup
        solo_eat = SoloEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_C_003. Start!]")
        login_page.input_password_and_email()

        # 메인에서 혼자먹기 페이지 이동 
        solo_eat.go_solo_eat()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone","❌혼자먹기 페이지 이동 오류"
        logging.info("✅ '👤혼자먹기' 페이지 정상 이동 완료.")

        # 임의의 음식 카테고리 선택
        solo_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")

        # 그리고 선택완료 누름
        solo_eat.choice_complete()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation","❌선택완료 오류"
        logging.info("✅ 선택완료")

        # 추천 메뉴및 맛집 검증
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

        logging.info(f"✅ {recommand.text} : {len(recommand_list)}개의 맛집 발견")


