import pytest
import re
from playwright.sync_api import Page, expect
from pages.shopdetail_page import ShopdetailPage

# pytest-playwright의 page fixture를 사용하므로 usefixtures는 필요 없습니다.
class TestMainPage:

    # driver: WebDriver 대신 page: Page fixture를 사용합니다.
    def test_TC003(self, page: Page):
        try:
            Shopdetail_page = ShopdetailPage(page)

            #베스트 50 페이지 오픈
            Shopdetail_page.open()
            time.sleep(1)        
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("bestseller"))
            assert "bestseller" in driver.current_url
            # Playwright의 wait_for_url과 expect를 사용합니다.
            page.wait_for_url("**/bestseller.html", timeout=10000)
            expect(page).to_have_url(re.compile(r".*bestseller\.html"))

            #특정 상품 선택
            Shopdetail_page.choice_click_by_bestiem(30)
            Shopdetail_page.choice_option(2)
            Shopdetail_page.random_option()
            '''
            time.sleep(2)
            #옵션 1의 개수 증가 및 감소 및 삭제
            Shopdetail_page.count_up_option(0)
            Shopdetail_page.count_down_option(0)
            time.sleep(2)
            #옵션 1 삭제
            Shopdetail_page.choice_del_option(0)
            time.sleep(2)
            driver.back()

            #랜덤 상품 선택
            Shopdetail_page.random_click_by_bestiem()
            time.sleep(1)
            #2번째 옵션 선택 밑 랜덤 옵션 선택
            Shopdetail_page.choice_option(2)
            Shopdetail_page.random_option()
            time.sleep(2)
            #옵션 1의 개수 증가 및 감소 및 삭제
            Shopdetail_page.count_up_option(0)
            Shopdetail_page.count_down_option(0)
            time.sleep(2)
            #옵션 1 삭제
            Shopdetail_page.choice_del_option(0)
            time.sleep(2)
            driver.back()
            #today 확인
            Shopdetail_page.open_page("https://www.nibbuns.co.kr/shop/todaygoods.html")
            '''
            time.sleep(10)
            
        except NoSuchElementException as e:
            assert False
