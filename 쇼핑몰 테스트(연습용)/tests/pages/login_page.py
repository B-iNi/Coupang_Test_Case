from playwright.sync_api import Page


class LoginPage:
    URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"

    def __init__(self, page: Page):
        self.page = page

    #페이지 열기
    def open(self):
        self.page.goto(self.URL)

    def input_id_and_password(self, id: str, password: str):
        self.page.locator('input[name="id"]').fill(id)
        self.page.locator('input[name="passwd"]').fill(password)
 

    def click_login_button(self):
        self.page.locator('.btn-mlog').click()