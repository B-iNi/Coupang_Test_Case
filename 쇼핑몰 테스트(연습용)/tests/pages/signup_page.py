from playwright.sync_api import Page


class SignUpPage:
    URL = "https://www.nibbuns.co.kr/shop/idinfo.html"

    def __init__(self, page: Page):
        self.page = page

    #페이지 열기
    def open(self):
        self.page.goto(self.URL)

    #체크박스 선택
    def check_box(self, checkbox_name: str):
        checkbox_locator = self.page.locator(f'input[name="{checkbox_name}"]')
        checkbox_locator.check()

    #버튼 클릭
    def click_btn(self, btn_xpath: str):
        button_locator = self.page.locator(f"xpath={btn_xpath}")
        button_locator.click()

    def input_info(self, name: str, id: str, password: str, check_password: str, email: str, phone_number: str):
        self.page.locator('#hname').fill(name)
        self.page.locator('#id').fill(id)
        self.page.locator('#password1').fill(password)
        self.page.locator('#password2').fill(check_password)
        self.page.locator('#email').fill(email)
        self.page.locator('#etcphone').fill(phone_number)

    #select box
    def select_box(self, select_name: str, value: str):
        select_locator = self.page.locator(f'select[name="{select_name}"]')
        select_locator.select_option(value=value)
