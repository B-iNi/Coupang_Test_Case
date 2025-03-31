import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from src.pages.profile import profile
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestProfile:

    def test_profile_workflow(self, driver: WebDriver):
        """
        통합 프로필 수정 테스트: 로그인 -> 프로필 페이지 접근 -> 사진 변경 -> 슬라이더 조정 -> 좋아하는/싫어하는 음식 입력 -> 수정 완료
        """

            # Page Objects 생성
        profile_page = profile(driver)
        login_page = LoginPage(driver)

        try:

            # 테스트 시작: 페이지 접속
            driver.get("https://kdt-pt-1-pj-2-team03.elicecoding.com")
            wait = ws(driver, 10)
            time.sleep(2)


            # 로그인 로직 실행
            test_email = "testid@test.com"
            test_password = "testpw1!"
            login_page.do_login(test_email, test_password)
            time.sleep(2)  # 로그인 후 대기

            # 개인 피드 접근
            profile_page.peed_open()
            time.sleep(2)  # 피드 열기 대기

            #개인 피드 접근 검증
            current_url = driver.current_url
            expected_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

            assert current_url == expected_url, f"❌ 예상 URL: {expected_url}, 실제 URL: {current_url}"

            # 프로필 수정 페이지 접근
            profile_page.profile_modify()
            time.sleep(2)  # 페이지 로딩 대기


            # 좋아하는 음식 입력
            print("🔧 좋아하는 음식 입력 중...")
            profile_page.like_food()
            time.sleep(1)


            # 수정 완료 버튼 클릭
            print("✅ 수정 완료 버튼 클릭!")
            profile_page.modify_access()
            time.sleep(2)

            # 좋아하는음식 검증
            like_xpath = '//*[@id="root"]/div[1]/main/section/section/section/div[2]/div[1]/p'
        

            like_text = wait.until(EC.presence_of_element_located((By.XPATH, like_xpath))).text
            

            # 비교 로직
            assert like_text == "좋아하는 음식 테스트 입니다.", "❌ 좋아하는 음식 텍스트 값 불일치!"
            

            print("✅ 좋아하는 음식 검증 완료!")
            
        except Exception as e:
            print(f"⚠️ 테스트 실패: {e}")
            assert False
