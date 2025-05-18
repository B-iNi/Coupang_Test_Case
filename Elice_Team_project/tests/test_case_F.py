import time
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
from src.pages.loginPage import LoginPage
from src.pages.team_pid import TeamPid
pytest_plugins = "pytest_html"



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
    def test_Case_F_01(self,setup):
        driver = setup
        team_pid = TeamPid(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_F_001. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


        
        # 메인에서 팀피드 버튼 검증
        TEAM_PID_BUTTON = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[2]/a')))
        assert TEAM_PID_BUTTON.is_displayed(),"❌'팀 피드' 버튼 오류"
        logging.info("✅ '팀 피드' 버튼 정상 출력")
    
        # 팀피드 페이지 이동
        TEAM_PID_BUTTON.click()
        logging.info("🔍 팀 피드 페이지 이동중...")
        assert driver.current_url != "https://kdt-pt-1-pj-2-team03.elicecoding.com"
        logging.info("✅'팀 피드' 페이지 정상 이동 완료.")
        
    
        # 팀 카테고리 버튼 검증                                                                    
        CATEGORY_BUTTON = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/button')))
        assert CATEGORY_BUTTON.is_displayed(),"❌팀 카테고리 버튼 오류"
        logging.info("✅ 팀 카테고리 버튼 정상 출력")
    
    
        # 팀 음식성향 검증
        FOOD_INCLINATION = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/section')))
        assert FOOD_INCLINATION.is_displayed(),"❌팀 음식성향 오류"
        logging.info("✅ 팀 성향 정상 출력")
        
        TEAM = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/section/div[1]/div/div/div')))
        assert TEAM.is_displayed(),"❌팀 표기 오류"
        logging.info(f"팀 : {TEAM.text}")
        USER_TEAM = TEAM.text
    
        INCLINATION = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/section/div[2]/span')))
        assert INCLINATION.is_displayed(),"❌음식 성향 표기 오류"
        logging.info(f"{INCLINATION.text}")
    
        for i in range(1,4):
            INFORMATION = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="root"]/div[1]/main/section/section/section/div[2]/section[{i}]')))
            logging.info(f"{INFORMATION.text}")
            assert INFORMATION.is_displayed(),"❌표기 오류"
        for j in range(1,3):
            REVIEW = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="root"]/div[1]/main/section/section/section/div[2]/div[{j}]/p')))
            logging.info(f"{REVIEW.text}")
            assert REVIEW.is_displayed(),"❌표기 오류"
    
    
        # 팀 통계 검증
        STATISTICS = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[2]/div/div/canvas')))
        assert STATISTICS.is_displayed(),"❌표기 오류"
        
        GRAPH = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[2]/canvas')))
        actions = ActionChains(driver)
        actions.move_to_element(GRAPH).perform()
        assert GRAPH.is_displayed(),"❌표기 오류"
    
        
        seen_menu_names = set()
        menu_items = []
        total_scrolls = 10
        logging.info(f"{USER_TEAM} 이 먹은 메뉴")
        for _ in range(total_scrolls):
            TEAM_MENU = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'flex.w-full.gap-6.p-4.shadow-md.rounded-2xl')))
    
            for item in TEAM_MENU:
                menu_name = item.find_element(By.CLASS_NAME,'font-bold').text
    
                if menu_name not in seen_menu_names:
                    seen_menu_names.add(menu_name)
                    menu_items.append(item)
                    logging.info(f"{menu_name}")
    
            driver.execute_script("window.scrollBy(0, 2000);")
            time.sleep(1)  
        
        logging.info(f"✅ 총 {len(menu_items)}개의 메뉴 발견")
        for item in menu_items:
            pass



    def test_Case_F_02(self,setup):
        driver = setup
        login_page = LoginPage(driver)
        logging.info("\n[Test_F_004. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)


       


        # 메인 타이틀 검증임
        TITLE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/header/div/span')))
        title = TITLE.text
        assert title == "오늘 뭐먹지 ?","❌ 타이틀 오류"
        logging.info(f"✅ 타이틀 출력 : {title}")

        # 메뉴 버튼 검증
        SOLO_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]/div/p')))
        SOLO = SOLO_BUTTON.text
        
        TOGETHER_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]/div/p')))
        TOGETHER = TOGETHER_BUTTON.text

        TEAM_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[3]/div/p')))
        TEAM = TEAM_BUTTON.text

        assert SOLO_BUTTON.is_displayed(),"❌ '혼자먹기' 버튼 오류"
        assert TOGETHER_BUTTON.is_displayed(),"❌ '같이먹기' 버튼 오류"
        assert TEAM_BUTTON.is_displayed(),"❌ '회식하기' 버튼 오류"
        logging.info(f"'{SOLO}' '{TOGETHER}' '{TEAM}'")
        logging.info("✅ 상단 버튼 출력")
        

        # 홈에 그래프 검증
        GRAPH = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/canvas')))
        assert GRAPH.is_displayed(),"❌ 출력 오류 (그래프)"
        logging.info("✅ 그래프 출력")

        # 추천 메뉴 이미지
        RECOMMEND_IMAGE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[1]')))
        assert RECOMMEND_IMAGE.is_displayed(),"❌ 추천 메뉴 이미지 오류"
        logging.info("✅ 추천 메뉴 이미지 출력")

        # 추천 메뉴
        RECOMMEND_DISH = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/p')))
        assert RECOMMEND_DISH.is_displayed(),"❌ 추천 메뉴 오류"
        DISH = RECOMMEND_DISH.text
        logging.info(f"✅ {DISH}")

        # AI 분석
        AI = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[2]/span')))
        ai = AI.text
        PERCENT = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[2]/div')))
        percent = PERCENT.text
        assert AI,"❌ 분석오류"
        assert PERCENT,"❌ 분석오류"
        logging.info(f"✅ {ai} : {percent}")

        # 하단 버튼 검증
        HOME = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[1]/a')))
        assert HOME.is_displayed(),"❌ 홈 오류 "
        TEAM_PID = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[2]/a')))                                               
        assert TEAM_PID.is_displayed(),"❌ 팀 피드 오류"
        HISTORY = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a')))
        assert HISTORY.is_displayed(),"❌ 히스토리 오류"
        PID = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[4]/a')))
        assert PID.is_displayed(),"❌ 개인 피드 오류"

        logging.info(f"'{HOME.text}' '{TEAM_PID.text}' '{HISTORY.text}' '{PID.text}'")
        logging.info("✅ 하단 버튼 출력")


