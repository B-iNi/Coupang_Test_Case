import pytest
import logging
import time
import random
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage


@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_Case_H_01(self, driver:WebDriver):
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

            logging.info("test_case_H_001")


            team_feed_team = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span'))).text
        

            assert my_team == team_feed_team  , "팀이 다릅니다"


            logging.info("test_case_H_001 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")



    def test_case_H_002(self, driver: WebDriver):
        wait = ws(driver, 10)
        login = LoginPage(driver)
        team = TeamPage(driver)

        logging.info("🔹 Precondition 시작")

        email = "team2@example.co.kr"
        password = "Team2@@@"
        
        try:
            login.do_login(email, password)

            my_team = team.my_team()
            logging.info(f"내 팀: {my_team}")

            logging.info("🔹 test_case_H_002 시작")

            first_team_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span')))
            first_team = first_team_element.text

            team_select_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  
            team_select_btn.click() 

            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))

            # 내 팀 제외한 팀 목록 필터링
            random_not_first_team = [option for option in teams_options if first_team not in option.text]
            if not random_not_first_team:
                pytest.fail("❌ 선택할 다른 팀이 없습니다.")

            selected_not_first_team = random.choice(random_not_first_team)

            # 🔹 Stale Element 방지: 요소를 다시 찾고 클릭
            for _ in range(3):
                try:
                    selected_not_first_team.click()
                    break
                except StaleElementReferenceException:
                    logging.warning("⚠️ StaleElementReferenceException 발생, 팀 선택 요소 다시 찾는 중...")
                    teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))
                    random_not_first_team = [option for option in teams_options if first_team not in option.text]
                    selected_not_first_team = random.choice(random_not_first_team)

            second_team_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span')))
            second_team = second_team_element.text

            assert second_team != first_team, "❌ 팀 변경이 되지 않았습니다."

            logging.info("✅ test_case_H_002 테스트 완료")

        except Exception as e:
            pytest.fail(f"❌ 테스트 중 오류 발생: {e}")



    def test_case_H_003(self, driver:WebDriver):
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

            logging.info("test_case_H_003")


            team_select_btn =wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  #팀 선택 버튼
            team_select_btn.click() 

            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))   #눌렀을떄 뜨는 팀 목록
            random_not_my_team = [option for option in teams_options if my_team not in option.text] # 내 팀 제외
            selected_not_my_team = random.choice(random_not_my_team) # 내 팀 제외 랜덤 선택
            logging.info(f"선택된 옵션: {selected_not_my_team.text}")
            selected_not_my_team.click()


            team.scroll_down()
            same_menu_btns = driver.find_elements(By.XPATH, "//button[contains(text(), '같은 메뉴 먹기')]")   #같은 메뉴 먹기 버튼(같은 팀에서만 존재)
            assert len(same_menu_btns) == 0, f"'같은 메뉴 먹기' 버튼이 존재합니다!!"
            logging.info("다른팀 test 완료")


            team.scroll_to_top()  # 다시 맨 위로 이동
            time.sleep(2)


            team_select_btn =wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  #팀 선택 버튼
            team_select_btn.click() 
            time.sleep(2)
            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))
            random_my_team = [option for option in teams_options if my_team in option.text]
            selected_my_team = random.choice(random_my_team)
            logging.info(f"선택된 옵션: {selected_my_team.text}")
            selected_my_team.click()

            same_menu_btns = driver.find_elements(By.XPATH, "//button[contains(text(), '같은 메뉴 먹기')]")  #다시 찾기
            team.scroll_down()
            assert len(same_menu_btns) > 0, "다른팀입니다."



            logging.info("test_case_H_003 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

        



    def test_case_H_004(self, driver:WebDriver):
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

            logging.info("test_case_H_004")


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)
            logging.info("test_case_H_004 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

       


    def test_case_H_005(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_005")

            eat_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@role='radio']")))
            selected_eat_option = random.choice(eat_options)   #식사 유형 랜덤으로 선택(혼밥, 그룹, 회식)
            logging.info(f"선택된 옵션: {selected_eat_option.get_attribute('value')}")  
            selected_eat_option.click()
            logging.info("유형 선택 완료!")
            time.sleep(2)

            #그룹일때만 나타나는 같이 먹은 사람 
            if selected_eat_option.get_attribute('value') == "그룹":
                wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='이름을 검색해주세요']"))).send_keys("김정재")  #김정재 검색 후 클릭
                driver.find_element(By.XPATH, "//li[contains(@class, 'cursor-pointer')]").click()


            logging.info("test_case_H_005 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")



    def test_case_H_006(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_006")


            image_path="/var/jenkins_home/workspace/team2/cat.png"
            team.add_image(image_path)
            logging.info("이미지 추가 완료!")

            review_image = driver.find_element(By.XPATH, '//img[@alt="후기 사진"]')  #사진 추가 시 생김

            assert review_image is not None, "후기 사진이 존재하지 않습니다!"


            logging.info("test_case_H_006 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")




    def test_case_H_007(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_007")

            food_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(3)] #한글 3글자 랜덤 설정
            food = ''.join(food_hangul_chars)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='메뉴 명을 입력해주세요.']"))).send_keys(food)

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            comment =''.join(comment_hangul_chars)
            wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']"))).send_keys(comment)
            logging.info("후기 입력 완료")
            time.sleep(2)


            logging.info("test_case_H_007 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")



    def test_case_H_008(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_008")

            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='음식 카테고리를 설정해주세요']]")))
            category_button.click()
            category_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))
            selected_category_element = random.choice(category_options)
            selected_category = selected_category_element.text   #마지막 assert 할때 카테고리 비교하기 위한 변수
            selected_category_element.click()
            logging.info(f"카테고리 설정 완료: {selected_category}")
            time.sleep(2)

            logging.info("test_case_H_008 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


    def test_case_H_009(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_009")

            stars = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]")))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1 # 검증 때 사용
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")
            time.sleep(2)

            logging.info("test_case_H_009 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


    def test_case_H_010(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)

            #식사 유형 선택
            eat_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@role='radio']")))
            selected_eat_option = random.choice(eat_options)   #식사 유형 랜덤으로 선택(혼밥, 그룹, 회식)
            logging.info(f"선택된 옵션: {selected_eat_option.get_attribute('value')}")  
            selected_eat_option.click()
            logging.info("유형 선택 완료!")

            #그룹일때만 나타나는 같이 먹은 사람 
            if selected_eat_option.get_attribute('value') == "그룹":
                wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='이름을 검색해주세요']"))).send_keys("김정재")  #김정재 검색 후 클릭
                driver.find_element(By.XPATH, "//li[contains(@class, 'cursor-pointer')]").click()


            #이미지 추가
            image_path="/var/jenkins_home/workspace/team2/cat.png"
            team.add_image(image_path)
            logging.info("이미지 추가 완료!")

            #메뉴이름 
            food_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(3)] #한글 3글자 랜덤 설정
            food = ''.join(food_hangul_chars)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='메뉴 명을 입력해주세요.']"))).send_keys(food)

            #후기
            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            comment =''.join(comment_hangul_chars)
            wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']"))).send_keys(comment)
            logging.info("후기 입력 완료")
            time.sleep(2)

            #카테고리  
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='음식 카테고리를 설정해주세요']]")))
            category_button.click()
            category_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))
            selected_category_element = random.choice(category_options)
            selected_category = selected_category_element.text   #마지막 assert 할때 카테고리 비교하기 위한 변수
            selected_category_element.click()
            logging.info(f"카테고리 설정 완료: {selected_category}")
            time.sleep(2)

            # 별점 선택
            stars = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]")))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1 # 검증 때 사용
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")
            time.sleep(2)


            logging.info("test_case_H_010")

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '후기 작성 완료')]"))).click()
            logging.info("후기 작성 완료")
            time.sleep(2)

            #개인 피드 버튼 클릭 후 이동
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='개인 피드']]"))).click()
            logging.info("개인 피드 이동")
            time.sleep(2)

            first_food_card = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')])[1]")))
            feed_food_name = first_food_card.find_element(By.XPATH, ".//div[@class='font-bold']").text
            food_category = [tag.text.strip() for tag in first_food_card.find_elements(By.XPATH, ".//div[contains(@class, 'inline-flex')]")]
            review_stars = len(first_food_card.find_elements(By.XPATH, ".//span[contains(text(), '★')]"))

            assert feed_food_name == food, "음식 이름이 일치하지 않음"
            logging.info("음식일치!")
            assert selected_category in food_category, "카테고리가 일치하지 않음"
            logging.info("카테고리 일치!")
            assert selected_star_count == review_stars, f"별점 개수가 일치하지 않음"
            logging.info("별 일치!")
            time.sleep(2)

            logging.info("test_case_H_010 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

    def test_case_H_011(self, driver:WebDriver):
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

            logging.info("test_case_H_011")


            menus = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'shadow-md') and contains(@class, 'rounded-2xl')]"))) #팀원들이 먹은 메뉴
            random_select_menu = random.choice(menus)  #메뉴들 중 랜덤으로 하나 선택
            menu_name = random_select_menu.find_element(By.XPATH, ".//div[@class='font-bold']").text
            logging.info(menu_name) #메뉴 이름 출력


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:   #화면에 보일 떄 까지 스크롤
                    try:
                        same_menu_button = random_select_menu.find_element(By.XPATH, ".//button[contains(@class, 'bg-main-black')]")
                        tag = random_select_menu.find_element(By.XPATH, ".//div[contains(concat(' ', normalize-space(@class), ' '), ' bg-main ')]").text  #혼밥,그룹,회식 태그                   
                        same_menu_button.click()
            
                        break  # 클릭 성공하면 루프 종료
                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1) 

            logging.info(tag)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='또 먹은 후기 등록하기']")))
            logging.info("또 먹은 후기 등록하기 페이지로 이동")
            time.sleep(5)

            checked_tag = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[@aria-checked='true']"))).get_attribute('value')  #미리 선택되어 있는 태그 이름
            menu_input = driver.find_element(By.XPATH, ".//input[@name='menu']").get_attribute('value')  #미리 선택 되어 있는 메뉴 이름
            logging.info(checked_tag)     
            logging.info(menu_input)   

            #랜덤으로 고른 메뉴랑 눌러서 들어간 거랑 메뉴,태그가 같은지 검증
            assert tag == checked_tag, "태그가 바뀜"
            assert menu_name == menu_input, "메뉴가 바뀜"


            logging.info("test_case_H_011 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

    def test_case_H_012(self, driver:WebDriver):
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

            menus = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'shadow-md') and contains(@class, 'rounded-2xl')]"))) #팀원들이 먹은 메뉴
            random_select_menu = random.choice(menus)  #메뉴들 중 랜덤으로 하나 선택
            menu_name = random_select_menu.find_element(By.XPATH, ".//div[@class='font-bold']").text
            logging.info(menu_name) #메뉴 이름 출력


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:   #화면에 보일 떄 까지 스크롤
                    try:
                        same_menu_button = random_select_menu.find_element(By.XPATH, ".//button[contains(@class, 'bg-main-black')]")
                        tag = random_select_menu.find_element(By.XPATH, ".//div[contains(concat(' ', normalize-space(@class), ' '), ' bg-main ')]").text  #혼밥,그룹,회식 태그                   
                        same_menu_button.click()
            
                        break  # 클릭 성공하면 루프 종료
                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1) 

            logging.info(tag)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='또 먹은 후기 등록하기']")))
            logging.info("또 먹은 후기 등록하기 페이지로 이동")
            time.sleep(5)

            checked_tag = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[@aria-checked='true']"))).get_attribute('value')  #미리 선택되어 있는 태그 이름
            menu_input = driver.find_element(By.XPATH, ".//input[@name='menu']").get_attribute('value')  #미리 선택 되어 있는 메뉴 이름
            logging.info(checked_tag)     
            logging.info(menu_input)   

            #랜덤으로 고른 메뉴랑 눌러서 들어간 거랑 메뉴,태그가 같은지 검증
            assert tag == checked_tag, "태그가 바뀜"
            assert menu_name == menu_input, "메뉴가 바뀜"


            logging.info("test_case_H_012")


            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            comment =''.join(comment_hangul_chars)
            #후기
            cmt = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']")))  #기존 후기 창에 입력되어 있는 글 지우고 새로 입력
            cmt.clear()
            cmt.send_keys(comment)  #위에서 생성한 랜덤 10글자 입력
            logging.info("후기 입력 완료")

            #별점 
            stars = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]")))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1 
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")



            logging.info("test_case_H_012 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

    def test_case_H_013(self, driver:WebDriver):
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

            menus = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'shadow-md') and contains(@class, 'rounded-2xl')]"))) #팀원들이 먹은 메뉴
            random_select_menu = random.choice(menus)  #메뉴들 중 랜덤으로 하나 선택
            menu_name = random_select_menu.find_element(By.XPATH, ".//div[@class='font-bold']").text
            logging.info(menu_name) #메뉴 이름 출력


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:   #화면에 보일 떄 까지 스크롤
                    try:
                        same_menu_button = random_select_menu.find_element(By.XPATH, ".//button[contains(@class, 'bg-main-black')]")
                        tag = random_select_menu.find_element(By.XPATH, ".//div[contains(concat(' ', normalize-space(@class), ' '), ' bg-main ')]").text  #혼밥,그룹,회식 태그                   
                        same_menu_button.click()
            
                        break  # 클릭 성공하면 루프 종료
                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1) 

            logging.info(tag)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='또 먹은 후기 등록하기']")))
            logging.info("또 먹은 후기 등록하기 페이지로 이동")
            time.sleep(5)

            checked_tag = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[@aria-checked='true']"))).get_attribute('value')  #미리 선택되어 있는 태그 이름
            menu_input = driver.find_element(By.XPATH, ".//input[@name='menu']").get_attribute('value')  #미리 선택 되어 있는 메뉴 이름
            logging.info(checked_tag)     
            logging.info(menu_input)   

            #랜덤으로 고른 메뉴랑 눌러서 들어간 거랑 메뉴,태그가 같은지 검증
            assert tag == checked_tag, "태그가 바뀜"
            assert menu_name == menu_input, "메뉴가 바뀜"

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            comment =''.join(comment_hangul_chars)
            #후기
            cmt = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']")))  #기존 후기 창에 입력되어 있는 글 지우고 새로 입력
            cmt.clear()
            cmt.send_keys(comment)  #위에서 생성한 랜덤 10글자 입력
            logging.info("후기 입력 완료")

            #별점 
            stars = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]")))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1 
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")

            logging.info("test_case_H_013")

            #후기 작성 버튼 클릭
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '후기 작성 완료')]"))).click()
            logging.info("후기 작성 완료")
            time.sleep(2)

            #개인 피드 이동
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='개인 피드']]"))).click()
            logging.info("개인 피드 이동")
            time.sleep(2)


            first_food_card = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')])[1]")))
            food_name = first_food_card.find_element(By.XPATH, ".//div[@class='font-bold']").text
            food_category = [tag.text.strip() for tag in first_food_card.find_elements(By.XPATH, ".//div[contains(@class, 'inline-flex')]")]
            review_stars = len(first_food_card.find_elements(By.XPATH, ".//span[contains(text(), '★')]"))

            #후기 추가한거랑 개인피드 맨위 비교
            assert food_name == menu_name , "메뉴가 다름"
            assert tag in food_category , "카테고리가 다름"
            assert selected_star_count == review_stars, f"별점 개수가 일치하지 않음"

    
            time.sleep(2)



            logging.info("test_case_H_013 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")

    def test_case_H_014(self, driver:WebDriver):
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

            logging.info("test_case_H_014")


           
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)



            logging.info("test_case_H_014 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


    def test_case_H_015(self, driver:WebDriver):
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

            


            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("test_case_H_015")

            sweet = round(random.uniform(1.0, 5.0), 1)
            salty = round(random.uniform(1.0, 5.0), 1)
            spicy = round(random.uniform(1.0, 5.0), 1)


            sweet_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[4]")))
            team.drag_slider(sweet_slider, sweet)

            time.sleep(2)

            salty_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[5]")))
            team.drag_slider(salty_slider, salty)

            time.sleep(2)

            spicy_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[6]")))
            team.drag_slider(spicy_slider, spicy)


            logging.info("test_case_H_015 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


    def test_case_H_016(self, driver:WebDriver):
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

            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("TC_H_16")

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            bad_comment =''.join(comment_hangul_chars)
            bad_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='cons']")))
            bad_input.clear()
            bad_input.send_keys(bad_comment)

            time.sleep(2)



            logging.info("test_case_H_016 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


    def test_case_H_017(self, driver:WebDriver):
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

            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("test_case_H_017")

            sweet = round(random.uniform(0.0, 0.9), 1)  # 1점 미만 하나 추가
            salty = round(random.uniform(1.0, 5.0), 1)
            spicy = round(random.uniform(1.0, 5.0), 1)


            sweet_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[4]")))
            team.drag_slider(sweet_slider, sweet)

            time.sleep(2)

            salty_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[5]")))
            team.drag_slider(salty_slider, salty)

            time.sleep(2)

            spicy_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[6]")))
            team.drag_slider(spicy_slider, spicy)


            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(9)] # 한글 9글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            bad_comment =''.join(comment_hangul_chars)
            bad_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='cons']")))
            bad_input.clear()
            bad_input.send_keys(bad_comment)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '프로필 수정 완료')]"))).click()

            flavor_error_msg = driver.find_element(By.XPATH,  "//p[@class='font-semibold text-red-500 text-description' and text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")
            assert flavor_error_msg.is_displayed()

            text_error_msg = driver.find_element(By.XPATH, "//p[@class='font-semibold text-red-500 text-description' and text()='10자 이상 입력해주세요']")


            assert text_error_msg.is_displayed()

            sweet = round(random.uniform(1.0, 5.0), 1)
            team.drag_slider(sweet_slider, sweet)


            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)
            corr_num = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "w-8")]')))
            corr_sweet = corr_num[3].text
            corr_salty = corr_num[4].text
            corr_spicy = corr_num[5].text

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '프로필 수정 완료')]"))).click()

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.font-bold.text-sub-2.text-title")))

            time.sleep(2)

            feed_num = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "w-8")]')))
            feed_sweet = feed_num[0].text
            feed_salty = feed_num[1].text
            feed_spicy = feed_num[2].text
            assert corr_sweet == feed_sweet  # +0.1 은 보정
            assert corr_salty  == feed_salty
            assert corr_spicy  == feed_spicy

            feed_write = driver.find_elements(By.XPATH, "//p[contains(@class, 'w-4/5')]")
            feed_good = feed_write[0].text
            feed_bad = feed_write[1].text

            assert good_comment == feed_good
            assert bad_comment == feed_bad

            logging.info("test_case_H_017 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


