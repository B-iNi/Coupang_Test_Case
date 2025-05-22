import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class SignUpPage:
    URL = "https://www.nibbuns.co.kr/shop/idinfo.html"
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    #페이지 열기
    def open(self):
        self.driver.get(self.URL)
    
    #체크박스 선택      
    def check_box(self, checkbox: str):
        item = self.driver.find_element(By.NAME, checkbox)
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.NAME, checkbox)))
        item.click()
        
    #버튼 클릭
    def click_btn(self, btn: str):
        button = self.driver.find_element(By.XPATH, btn)
        button.click()
    
    def input_info(self, name: str, id: str, password: str, check_password: str, email: str, phone_number: str):
        name_input_box = self.driver.find_element(By.ID, 'hname')
        name_input_box.send_keys(name)
        time.sleep(1)
        id_input_box = self.driver.find_element(By.ID, 'id')
        id_input_box.send_keys(id)
        time.sleep(1)
        password_input_box = self.driver.find_element(By.ID, 'password1')
        password_input_box.send_keys(password)
        time.sleep(1)
        check_password_input_box = self.driver.find_element(By.ID, 'password2')
        check_password_input_box.send_keys(check_password)
        time.sleep(1)
        email_input_box = self.driver.find_element(By.ID, 'email')
        email_input_box.send_keys(email)
        time.sleep(1)
        phone_number_input_box = self.driver.find_element(By.ID, 'etcphone')
        phone_number_input_box.send_keys(phone_number)
        time.sleep(1)
        
    #select box
    def select_box(self, option: str, value: str):
        selected_item = Select(self.driver.find_element(By.NAME, option))
        selected_item.select_by_value(value)
        time.sleep(1)
       
        