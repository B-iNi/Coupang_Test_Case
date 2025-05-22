import re
from playwright.sync_api import Page, expect
from tests.pages.signup_page import SignUpPage

class TestTC001:
    def test_signup(self, page: Page):
        signup_page = SignUpPage(page)
        signup_page.open()

        page.wait_for_url("**/shop/idinfo.html", timeout=20000)
        expect(page).to_have_url(re.compile(r".*shop/idinfo\.html"))

        signup_page.check_box("yaok2")

        signup_page.check_box("privacy1")

        # 버튼 클릭
        signup_page.click_btn('//*[@id="form1"]/fieldset/div/div[2]/a')


        # 회원정보 입력
        signup_page.input_info('홍길동', 'testuser100', 'password123', 'password123', 'email@naver.com', '01012345678')
        signup_page.select_box('birthyear', '1988')
        signup_page.select_box('birthmonth', '03')
        signup_page.select_box('birthdate', '04')
        signup_page.check_box('user_age_check')

        page.on("dialog", lambda dialog: dialog.accept())

        # 회원가입 버튼 클릭 (이 버튼 클릭 시 alert 발생 예상)
        signup_page.click_btn('//*[@id="join_form"]/div/div/a/img')

        # 회원가입 후 리디렉션된 URL 확인

        page.wait_for_url("**/nibbuns.co.kr/", timeout=10000)
        expect(page).to_have_url(re.compile(r".*nibbuns\.co\.kr/"))
