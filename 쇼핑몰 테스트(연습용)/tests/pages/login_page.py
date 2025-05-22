from playwright.sync_api import Page

review_page.py shopdetail_page.py 35678
class LoginPage:
    URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"

    def __init__(self, page: Page):
        # Selenium WebDriver 대신 Playwright Page 객체를 받도록 변경
        self.page = page

    #페이지 열기
    def open(self):
        self.page.goto(self.URL)

    def input_id_and_password(self, id: str, password: str):
        # Selenium find_element 대신 Playwright locator 사용
        self.page.locator('input[name="id"]').fill(id)
        self.page.locator('input[name="passwd"]').fill(password)

    def click_login_button(self):
        # Selenium find_element 대신 Playwright locator 사용
        # 클래스 이름 'btn-mlog'를 가진 요소를 찾습니다.
        self.page.locator('.btn-mlog').click()