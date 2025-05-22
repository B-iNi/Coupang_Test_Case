import time
import random
from playwright.sync_api import Page

class ShopdetailPage:
    URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST&ref=&suburl=shop%2Fbestseller.html%3Fxcode%3DBEST/"
    SEARCH_INPUT_ID = '//*[@id="hd"]/div[3]/div[1]/div[2]/form/fieldset/input'
    SOLD_OUT = '품절'
    # Playwright 로케이터는 CSS 선택자를 기본으로 사용합니다.
    # 기존 XPath를 Playwright 로케이터로 사용하려면 'xpath=' 접두사를 붙여야 합니다.
    # 가능하면 CSS 선택자로 변경하는 것이 좋습니다.
    OPTION_XPATH = '//*[@id="MK_innerOptScroll"]//a[@href]'
    OPTION_CLASS = 'basic_option'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.page.goto(url)

    #bestseller에서 작동    
    def all_click_by_bestiem(self):
        # Playwright는 기본적으로 요소가 클릭 가능할 때까지 기다립니다.
        # execute_script를 사용할 필요가 없습니다.
        # CSS 선택자로 변경하는 것이 좋습니다. 예: '.prdImg'
        links_locators = self.page.locator(".prdImg").all()
        print(len(links_locators))
        for link_locator in links_locators:
            link_locator.click()
            self.page.go_back() # driver.back() 대신 page.go_back() 사용
            # time.sleep(0.5) # Playwright auto-waiting으로 대부분 불필요

    #bestseller에서 작동
    def choice_click_by_bestiem(self, select : int) :
        # CSS 선택자로 변경하는 것이 좋습니다. 예: '.prdImg'
        links_locators = self.page.locator(".prdImg").all()
        if 0 <= select < len(links_locators):
             links_locators[select].click()
        else:
            print(f"Warning: Index {select} is out of bounds for {len(links_locators)} items.")

    #bestseller에서 작동
    def random_click_by_bestiem(self) :
        # CSS 선택자로 변경하는 것이 좋습니다. 예: '.prdImg'
        links_locators = self.page.locator(".prdImg").all()
        if links_locators:
            random_index = random.randint(0, len(links_locators) - 1)
            links_locators[random_index].click()

    #shopdetail에서 작동
    def choice_option(self, select : int) :
        # CSS 선택자로 변경하는 것이 좋습니다. 예: 'select.basic_option'
        option_locator = self.page.locator('select.basic_option')
        # 품절 여부 확인 로직은 Playwright의 text_content()를 사용해야 합니다.
        # 현재 로직은 옵션 텍스트 전체에 "품절"이 있는지 확인하는 것으로 보입니다.
        # 실제 웹사이트 구조에 따라 더 정확한 로직이 필요할 수 있습니다.
        # 여기서는 일단 select_option을 사용하도록 변경합니다.
        # if self.SOLD_OUT not in option_locator.text_content(): # 품절이 아닌 경우에만 선택?
        option_locator.select_option(index=select + 1) # index는 0부터 시작하지만, 첫 번째 옵션은 보통 "선택하세요"이므로 +1

    #shopdetail에서 작동
    def random_option(self) :
        # CSS 선택자로 변경하는 것이 좋습니다. 예: 'select.basic_option'
        option_locator = self.page.locator('select.basic_option')
        # if self.SOLD_OUT not in option_locator.text_content(): # 품절이 아닌 경우에만 선택?
        options_count = option_locator.locator('option').count()
        if options_count > 1: # "선택하세요" 옵션 제외
            random_index = random.randint(1, options_count - 1)
            option_locator.select_option(index=random_index)

    def count_up_option(self, select : int) :
        # XPath 로케이터를 Playwright 로케이터로 변경
        option_locators = self.page.locator(f'xpath={self.OPTION_XPATH}').all()
        # 품절 확인 로직은 실제 웹사이트 구조에 맞게 수정 필요
        if len(option_locators) > select * 3: # or any(self.SOLD_OUT in item for item in [loc.text_content() for loc in option_locators]):
            option_locators[select * 3].click()

    def count_down_option(self, select : int) :
        # XPath 로케이터를 Playwright 로케이터로 변경
        option_locators = self.page.locator(f'xpath={self.OPTION_XPATH}').all()
        # 품절 확인 로직은 실제 웹사이트 구조에 맞게 수정 필요
        if len(option_locators) > select * 3 + 1: # or any(self.SOLD_OUT in item for item in [loc.text_content() for loc in option_locators]):
            option_locators[1 + select * 3].click()

    def choice_del_option(self, select : int) :
        # XPath 로케이터를 Playwright 로케이터로 변경
        option_locators = self.page.locator(f'xpath={self.OPTION_XPATH}').all()
        # 품절 확인 로직은 실제 웹사이트 구조에 맞게 수정 필요
        if len(option_locators) > select * 3 + 2: # or any(self.SOLD_OUT in item for item in [loc.text_content() for loc in option_locators]):
            option_locators[2 + select * 3].click()