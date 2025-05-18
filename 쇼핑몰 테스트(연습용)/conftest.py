# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")

    # WebDriver Manager를 이용해 ChromeDriver 자동 설치 및 Service 객체 생성
    service = Service(ChromeDriverManager().install())

    # 드라이버 객체 생성
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #  대기시간 설정
    driver.implicitly_wait(5)

    yield driver

    # 테스트가 끝나면 드라이버 종료
    driver.quit()

coupang.com => MainPage 
/login => loginPage
/signup => 회원가입 페이지 
