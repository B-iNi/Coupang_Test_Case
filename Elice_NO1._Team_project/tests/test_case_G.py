import time
import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.recommendation_page import RecommendationPage
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestCaseG:
    def test_Case_G_01(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기
            #1.메뉴 추천 페이지 들어간다
            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)

            logging.info("test_case_G_001")


            first_rcm = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text #변경전 메뉴 
            logging.info("변경전 메뉴 : %s", first_rcm)
            time.sleep(2)

        
            rcm.refresh_recommendation()
            time.sleep(2)
            new_rcm= wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text
            logging.info("변경후 메뉴 : %s", new_rcm)
            time.sleep(2)


            logging.info("test_case_G_001 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")




    def test_Case_G_02(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)

            logging.info("test_case_G_002")

            while True:
                no_result = len(driver.find_elements(By.XPATH, "//h1[contains(text(), '검색 결과가 없습니다')]")) > 0

                pagination_btns = driver.find_elements(By.CLASS_NAME, "swiper-pagination-bullet")
                pagination_exists = len(pagination_btns) > 2  #2개 이상일때 스크롤 가능


                if not no_result and pagination_exists:
                    break
  
                rcm.refresh_recommendation()
                logging.info("검색 결과가 없거나 swipe 버튼이 없습니다. 다시 추천 받기")
                time.sleep(2)
                
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-pagination-bullet")))


            logging.info("test_case_G_002 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")



    def test_Case_G_03(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)


            while True:
                no_result = len(driver.find_elements(By.XPATH, "//h1[contains(text(), '검색 결과가 없습니다')]")) > 0

                pagination_btns = driver.find_elements(By.CLASS_NAME, "swiper-pagination-bullet")
                pagination_exists = len(pagination_btns) > 2  #2개 이상일때 스크롤 가능


                if not no_result and pagination_exists:
                    break
  
                rcm.refresh_recommendation()
                logging.info("검색 결과가 없거나 swipe 버튼이 없습니다. 다시 추천 받기")
                time.sleep(2)
                
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-pagination-bullet")))

            logging.info("test_case_G_003")


            swipe_before_place = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-slide-active"))).find_element(By.CLASS_NAME, "font-semibold").text
            logging.info("swipe 전 가게 : %s",swipe_before_place)
            rcm.swipe(3)
            logging.info("swipe 완료")
            swipe_after_place = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-slide-active"))).find_element(By.CLASS_NAME, "font-semibold").text
            logging.info("swipe 후 가게 : %s",swipe_after_place)
            
            assert swipe_before_place != swipe_after_place , "swipe 안됨"
            time.sleep(2)  


            logging.info("test_case_G_003 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")



    def test_Case_G_05(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)


            logging.info("test_case_G_005")

            max_attempts = 10
            attempt = 0

            while True:
    # 시도 횟수 증가
                attempt += 1
    
    # 적합도 요소 찾기
                percent_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'inline-flex') and contains(@class, 'bg-sub')]")))
                percent_text = percent_element.text.strip().replace("%", "")
                percent_value = float(percent_text)

    # 적합도 40% 이상이면 종료
                if percent_value >= 40:
                    logging.info("적합도 %d%% (기준 충족)", percent_value)
                    break

    # 10번 시도 후 종료
                if attempt > max_attempts:
                    logging.info("적합도 %d%% (10번 시도 초과, 없습니다)", percent_value)
                    print("없습니다")
                    break

    # 적합도 미달 시 재추천
                rcm.refresh_recommendation()
                logging.info("적합도 %d%% (기준 미달, 재추천, 시도 %d/%d)", percent_value, attempt, max_attempts)
                time.sleep(2)


                logging.info("test_case_G_005 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

            
    def test_Case_G_06(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)


            logging.info("test_case_G_006")

            rcm_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text
            logging.info("최종 추천 메뉴 : %s",rcm_menu)

            rcm.accept()

            wait.until(EC.url_contains("history"))
            assert "history" in driver.current_url
            logging.info("히스토리 페이지 이동")
            time.sleep(2)

            recent_menu =wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')])[1]"))).find_element(By.CLASS_NAME, "font-bold").text
            logging.info("히스토리 최근 메뉴 : %s",recent_menu)


            assert rcm_menu == recent_menu , "메뉴 일치하지 않음"
            time.sleep(2)



            logging.info("test_case_G_006 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


            
