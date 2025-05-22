from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

class ShopdetailPage:
    URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST&ref=&suburl=shop%2Fbestseller.html%3Fxcode%3DBEST/"
    SEARCH_INPUT_ID = '//*[@id="hd"]/div[3]/div[1]/div[2]/form/fieldset/input'
    SOLD_OUT = '품절'
    OPTION_XPATH = '//*[@id="MK_innerOptScroll"]//a[@href]'
    OPTION_CLASS = 'basic_option'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_page(self, url : str):
        self.driver.get(url)

    #bestseller에서 작동    
    def all_click_by_bestiem(self):
        #link= self.driver.find_elements(By.XPATH,'//*[@id="prdBrand"]/div[3]/div/ul//a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        print(len(links))
        for i in links :
            #클릭을 사용시 화면에 보이는 부분만 가능 대신 화면이 내려가면서 클릭되기 때문에 둘중 하나 선택
            #i.click()
            self.driver.execute_script("arguments[0].click();", i)
            self.driver.back()
            time.sleep(0.5)
        
    #bestseller에서 작동
    def choice_click_by_bestiem(self, select : int) :
        #find_elements(By.XPATH, './/a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        self.driver.execute_script("arguments[0].click();", links[select])

    #bestseller에서 작동
    def random_click_by_bestiem(self) :
        #find_elements(By.XPATH, './/a[@href]')
        links=self.driver.find_elements(By.CLASS_NAME ,"prdImg")
        self.driver.execute_script("arguments[0].click();", links[random.randint(0, len(links)-1)])

    #shopdetail에서 작동
    def choice_option(self, select : int) :
        option = self.driver.find_element(By.CLASS_NAME ,"basic_option")
        if any(self.SOLD_OUT in item for item in option.text) :
            Select(option).select_by_index(select+1)
            
    #shopdetail에서 작동
    def random_option(self) :
        option = self.driver.find_element(By.CLASS_NAME ,"basic_option")
        if any(self.SOLD_OUT in item for item in option.text) :
            Select(option).select_by_index(random.randint(1, len(Select(option).options) - 1))

    def count_up_option(self, select : int) :
        option= self.driver.find_elements(By.XPATH, self.OPTION_XPATH)
        if len(option) > select*3 or any(self.SOLD_OUT in item for item in option.text) :
            option[select*3].click()
        
    def count_down_option(self, select : int) :
        option= self.driver.find_elements(By.XPATH, self.OPTION_XPATH)
        if len(option) > select*3 or any(self.SOLD_OUT in item for item in option.text):
            option[1 + select*3].click()
        
    def choice_del_option(self, select : int) :
        option= self.driver.find_elements(By.XPATH, self.OPTION_XPATH)
        if len(option) > select*3 or any(self.SOLD_OUT in item for item in option.text) :
            option[2 + select*3].click()