import time
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver 


from tests.pages.signup_page import SignUpPage

class TestTC001:
    def test_signup(self, driver: WebDriver):
        
        try:
            signup_page = SignUpPage(driver)
            signup_page.open()
            
            wait = ws(driver, 20) #최대 20까지 기다림
            wait.until(EC.url_contains("shop/idinfo.html")) 
            assert "shop/idinfo.html" in driver.current_url
            
            signup_page.check_box("yaok2")
            time.sleep(2)
            signup_page.check_box("privacy1")
            
            #버튼 클릭
            signup_page.click_btn('//*[@id="form1"]/fieldset/div/div[2]/a')
            time.sleep(3)
            
            #회원정보 입력
            signup_page.input_info('홍길동', 'testuser100', 'password123', 'password123', 'email@naver.com', '01012345678')
            signup_page.select_box('birthyear', '1988')
            signup_page.select_box('birthmonth', '03')
            signup_page.select_box('birthdate', '04')
            signup_page.check_box('user_age_check')
            
            #버튼 
            signup_page.click_btn('//*[@id="join_form"]/div/div/a/img')
            time.sleep(2)
            driver.switch_to.alert.accept()
            time.sleep(2)
            wait = ws(driver, 10) 
            wait.until(EC.url_contains("nibbuns.co.kr/")) 
            assert "nibbuns.co.kr/" in driver.current_url
            
                
        except Exception as e:
            print("error")
            
    
    
