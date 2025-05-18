import time
import random
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver 

from tests.pages.login_page import LoginPage


class TestTC002:
    def test_login(self, driver: WebDriver):
        
        try:
            login_page = LoginPage(driver)
            login_page.open()
            
            wait = ws(driver, 20) #최대 20까지 기다림
            wait.until(EC.url_contains("login")) 
            assert "login" in driver.current_url
            
            login_page.input_id_and_password('testuser100', 'password123')
            login_page.click_login_button()
            
            wait = ws(driver, 10)
            wait.until(EC.url_contains("main")) 
            assert "main" in driver.current_url 
            
            driver.save_screenshot('로그인-성공.jpg')
        
        except Exception as e:
            assert False
            
    
    
