import random
from playwright.sync_api import Page, Locator

class ShopdetailPage:
    URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST&ref=&suburl=shop%2Fbestseller.html%3Fxcode%3DBEST/"
    SOLD_OUT = '품절'
    OPTION_BUTTONS_XPATH = '//*[@id="MK_innerOptScroll"]//a[@href]'
    OPTION_SELECT_CLASS = 'basic_option'

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def open_page(self, url: str):
        self.page.goto(url)

    #bestseller에서 작동    
    def all_click_by_bestitem(self): 
        item_links_locator = self.page.locator(".prdImg")
        count = item_links_locator.count()
        print(f"Found {count} items to click.")
        for i in range(count):
            current_item_link = self.page.locator(".prdImg").nth(i)
            try:
                print(f"Clicking item {i+1}/{count}...")
                current_item_link.click(timeout=15000) 
                self.page.wait_for_load_state('domcontentloaded', timeout=15000)
                print("Navigating back...")
                self.page.go_back(wait_until='domcontentloaded', timeout=15000)
                self.page.wait_for_load_state('domcontentloaded', timeout=15000) 
            except Exception as e:
                print(f"Error clicking or navigating back for item index {i}: {e}")
                new_count = item_links_locator.count()
                if new_count != count:
                    print(f"Item count changed from {count} to {new_count}. Adjusting loop or exiting.")
                    break 
                if i >= new_count:
                    break

    #bestseller에서 작동
    def choice_click_by_bestitem(self, select_index: int): 
        item_links_locator = self.page.locator(".prdImg")
        item_links_locator.nth(select_index).click()

    #bestseller에서 작동
    def random_click_by_bestitem(self):
        item_links_locator = self.page.locator(".prdImg")
        count = item_links_locator.count()
        if count > 0:
            random_idx = random.randint(0, count - 1)
            item_links_locator.nth(random_idx).click()
        else:
            print("No best items found to click randomly.")

    #shopdetail에서 작동
    def choice_option(self, select_idx: int): 
        option_select_locator = self.page.locator(f".{self.OPTION_SELECT_CLASS}").first
        all_options_combined_text = option_select_locator.inner_text()
        target_playwright_option_index = select_idx + 1

        if self.SOLD_OUT in all_options_combined_text: 
            num_options_tags = option_select_locator.locator("option").count()
            if 0 <= target_playwright_option_index < num_options_tags:
                option_select_locator.select_option(index=target_playwright_option_index)
            else:
                print(f"Target option index {target_playwright_option_index} is out of bounds.")
        else:
            print(f"'{self.SOLD_OUT}' not found in the dropdown's combined text. Original logic would not select here. "
                  f"If you intend to select regardless, or check the specific option, please adjust the logic.")

    #shopdetail에서 작동
    def random_option(self):
        option_select_locator = self.page.locator(f".{self.OPTION_SELECT_CLASS}").first
        all_options_combined_text = option_select_locator.inner_text()

        if self.SOLD_OUT in all_options_combined_text: 
            option_tags_locator = option_select_locator.locator("option")
            num_options_tags = option_tags_locator.count()

            if num_options_tags > 1: 
                random_idx_to_select = random.randint(1, num_options_tags - 1)
                option_select_locator.select_option(index=random_idx_to_select)
            else:
                print("Not enough options to select a random one (excluding potential placeholder at index 0).")
        else:
            print(f"'{self.SOLD_OUT}' not found in the dropdown's combined text. Original logic would not select randomly here.")

    def _get_option_buttons_locator(self) -> Locator:
        return self.page.locator(f"xpath={self.OPTION_BUTTONS_XPATH}")

    # shopdetail에서 작동 (수량 증가)
    def count_up_option(self, option_group_index: int): 
        button_index = option_group_index * 3
        option_buttons = self._get_option_buttons_locator()
        if option_buttons.count() > button_index:
            option_buttons.nth(button_index).click()
        else:
            print(f"Count up button for option group index {option_group_index} not found.")

    # shopdetail에서 작동 (수량 감소)
    def count_down_option(self, option_group_index: int): 
        button_index = option_group_index * 3 + 1
        option_buttons = self._get_option_buttons_locator()
        if option_buttons.count() > button_index:
            option_buttons.nth(button_index).click()
        else:
            print(f"Count down button for option group index {option_group_index} not found.")

    # shopdetail에서 작동 (옵션 삭제)
    def choice_del_option(self, option_group_index: int): 
        button_index = option_group_index * 3 + 2
        option_buttons = self._get_option_buttons_locator()
        if option_buttons.count() > button_index:
            option_buttons.nth(button_index).click()
        else:
            print(f"Delete button for option group index {option_group_index} not found.")