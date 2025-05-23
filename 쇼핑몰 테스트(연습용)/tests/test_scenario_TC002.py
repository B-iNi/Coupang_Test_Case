import re
from playwright.sync_api import Page, expect
import pytest 

from tests.pages.login_page import LoginPage 

#  python -m pytest -s tests/test_scenario_TC002.py --headed

class TestTC002:
    def test_002(self, page: Page):
        try:
            login_page = LoginPage(page)
            login_page.open()


            expect(page).to_have_url(re.compile(r".*login.*"), timeout=20000)

            login_page.input_id_and_password('testuser100', 'password123')
            login_page.click_login_button()

            expect(page).to_have_url(re.compile(r".*main.*"), timeout=10000)

            # 스크린샷 저장
            page.screenshot(path='로그인-성공.jpg')

        except Exception as e:
            pytest.fail(f"로그인 테스트 중 예외 발생: {e}")