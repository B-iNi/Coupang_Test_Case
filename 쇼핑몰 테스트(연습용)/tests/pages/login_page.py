import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class LoginPage:
    URL = "https://www.nibbuns.co.kr/shop/member.html?type=login"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    #페이지 열기
    def open(self):
        self.driver.get(self.URL)
        
    def input_id_and_password(self, id: str, password: str):
        id_input_box = self.driver.find_element(By.NAME, 'id')
        id_input_box.send_keys(id)
        password_input_box = self.driver.find_element(By.NAME, 'passwd')
        password_input_box.send_keys(password)
  
    def click_login_button(self):
        login_button = self.driver.find_element(By.CLASS_NAME, 'btn-mlog')
        login_button.click()