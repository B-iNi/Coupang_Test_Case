import re
import random
import string
from playwright.sync_api import Page, expect
from tests.pages.signup_page import SignUpPage

# python -m pytest -s tests/test_scenario_TC001.py --headed

class TestTC001:
    def test_001(self, page: Page):
        signup_page = SignUpPage(page)
        signup_page.open()


        page.wait_for_url("**/shop/idinfo.html", timeout=20000) 
        expect(page).to_have_url(re.compile(r".*shop/idinfo\.html")) 

        signup_page.check_box("yaok2")
     
        signup_page.check_box("privacy1")

        # 버튼 클릭
        signup_page.click_btn('//*[@id="form1"]/fieldset/div/div[2]/a')
 
        # 랜덤 데이터 생성
        random_suffix = ''.join(random.choices(string.digits, k=5))
        random_name = f"테스트{random_suffix}"
        random_id = f"testuser{random_suffix}"
        # 비밀번호는 영문, 숫자 조합으로 8자 이상 (예시)
        password_chars = string.ascii_letters + string.digits
        random_password = "pw" + ''.join(random.choices(password_chars, k=8))
        random_email = f"test{random_suffix}@example.com"
        random_phone_number = "010" + "".join(random.choices(string.digits, k=8))
        
        random_birth_year = str(random.randint(1970, 2003))
        random_birth_month = f"{random.randint(1, 12):02d}" # 1-12월, 두 자리로 포맷 (예: 03)
        random_birth_date = f"{random.randint(1, 28):02d}" # 1-28일, 두 자리로 포맷 (간단하게 처리)


        # 회원정보 입력
        signup_page.input_info(
            random_name,
            random_id,
            random_password,
            random_password, # 비밀번호 확인은 동일하게
            random_email,
            random_phone_number
        )
        signup_page.select_box('birthyear', random_birth_year)
        signup_page.select_box('birthmonth', random_birth_month)
        signup_page.select_box('birthdate', random_birth_date)
        signup_page.check_box('user_age_check')
        page.on("dialog", lambda dialog: dialog.accept())

        # 회원가입 버튼 클릭 (이 버튼 클릭 시 alert 발생 예상)
        signup_page.click_btn('//*[@id="join_form"]/div/div/a/img')

        page.wait_for_url(re.compile(r"https://www\.nibbuns\.co\.kr/.*\.html"), timeout=20000) 
        expect(page).to_have_url(re.compile(r"https://www\.nibbuns\.co\.kr/html/mainm\.html")) 

