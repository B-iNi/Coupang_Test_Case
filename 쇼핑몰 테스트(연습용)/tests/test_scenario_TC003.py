import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib import parse
from pages.shopdetail_page import ShopdetailPage
from selenium.webdriver.support.ui import Select
import random

@pytest.mark.usefixtures("driver")
class TestMainPage:

    def test_TC003(self, driver: WebDriver):
        try:
            Shopdetail_page = ShopdetailPage(driver)

            #베스트 50 페이지 오픈
            Shopdetail_page.open()
            time.sleep(1)        
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("bestseller"))
            assert "bestseller" in driver.current_url

            #특정 상품 선택
            Shopdetail_page.choice_click_by_bestiem(30)
            time.sleep(2)
            #2번째 옵션 선택 밑 랜덤 옵션 선택
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
