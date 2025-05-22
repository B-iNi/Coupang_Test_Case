import re
from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage


class TestTC002:
    def test_login(self, page: Page):
        try:
            login_page = LoginPage(page)
            login_page.open()

            # URL이 'login'을 포함하는지 확인 (최대 20초 대기)
            page.wait_for_url("**/member/login.html", timeout=20000)
            expect(page).to_have_url(re.compile(r".*member/login\.html"))

            login_page.input_id_and_password('testuser100', 'password123')
            login_page.click_login_button()

            # 로그인 후 메인 페이지로 이동했는지 URL 확인 (최대 10초 대기)
            # 실제 메인 페이지 URL 패턴으로 변경해야 합니다. 예: "**/index.html" 또는 "**/main.html"
            # 여기서는 nibbuns.co.kr 도메인으로 이동했는지 확인합니다.
            page.wait_for_url("**/nibbuns.co.kr/**", timeout=10000)
            # 더 구체적인 URL 패턴을 사용하는 것이 좋습니다.
            # 예: expect(page).to_have_url(re.compile(r".*nibbuns\.co\.kr/(index\.html)?$"))
            expect(page.url).not_to_contain("login.html") # 로그인 페이지가 아니어야 함

            page.screenshot(path='로그인-성공_playwright.png')

        except Exception as e:
            # Playwright의 expect 구문은 실패 시 AssertionError를 발생시키므로,
            # 특별한 예외 처리가 필요 없다면 이 try-except 블록을 제거해도 됩니다.
            # 테스트 프레임워크가 실패를 자동으로 보고합니다.
            print(f"Test failed: {e}")
            raise # 원래 예외를 다시 발생시켜 테스트 실패로 처리
