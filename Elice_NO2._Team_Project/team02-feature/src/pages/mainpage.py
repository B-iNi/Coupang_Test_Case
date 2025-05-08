from selenium.webdriver.chrome.webdriver import WebDriver

class MainPage:
    URL = "http://localhost:4100/"  # 직접 URL을 설정

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)  # 하드코딩된 URL을 사용
