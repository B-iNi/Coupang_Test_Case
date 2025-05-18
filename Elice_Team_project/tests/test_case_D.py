import pytest
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains  # 연속 동작 수행 (예: 드래그 앤 드롭)
from selenium.webdriver.common.keys import Keys  # 키보드 입력 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  
from src.pages.together_eat import TogetherEat
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




class TestCaseD:
    def test_Case_D_01(self,setup):
        driver = setup
        together_eat = TogetherEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_D_001. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)



        # 메인에서 같이먹기 버튼 검증
        TOGETHER_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]')))
        assert TOGETHER_BUTTON.is_displayed(),"❌'👥같이먹기' 버튼 오류"
        logging.info("✅ '👥같이먹기' 버튼 정상 출력")

        # 같이먹기 페이지 이동
        TOGETHER_BUTTON.click()
        logging.info("🔍 같이먹기 페이지 이동중...")
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.")


        # 카테고리 버튼 검증
        categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
        assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
        logging.info("✅ 카테고리 버튼 정상 출력")

        # 카테고리 설정
        together_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"



    def test_Case_D_02(self,setup):
        driver = setup
        together_eat = TogetherEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_D_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)



        # 같이먹기 페이지 이동
        together_eat.go_together_eat()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.")

        # 카테고리 설정
        together_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")

        # 임의 인원 추가 함
        together_eat.human_check_box()
        SELECT_HUMAN = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div')))
        assert len(SELECT_HUMAN) > 0,"❌인원 선택 오류"
        logging.info("✅ 인원 선택 완료") 


        # 임의 인원 빼기
        together_eat.un_select_people()
        TO_SELECT_HUMAN = len(SELECT_HUMAN)
        SELECT_HUMAN = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div')))
        assert len(SELECT_HUMAN) != TO_SELECT_HUMAN,"❌인원 선택 오류"
        logging.info(f"✅ 최종 선택 인원 {len(SELECT_HUMAN)} 명")
 



    def test_Case_D_03(self,setup):
        driver = setup
        together_eat = TogetherEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_D_003. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


    
         # 같이먹기 페이지 이동
        together_eat.go_together_eat()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.")
        
        # 카테고리 설정
        together_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")
    
        
    
        # 임의 인원 추가 함
        together_eat.human_check_box()
        SELECT_HUMAN = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div')))
        assert len(SELECT_HUMAN) > 0,"❌인원 선택 오류"
        logging.info("✅ 인원 선택 완료")
    
        
        # 선택완료
        together_eat.choice_complete()
        assert driver.current_url != "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ 선택 완료 및 페이지 이동")
    
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
          
