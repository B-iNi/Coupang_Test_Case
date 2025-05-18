import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

@pytest.fixture(scope="function")
def driver():
    # 크롬드라이버 자동 설치
    driver_path = chromedriver_autoinstaller.install()

    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 또는 /opt/chrome/chrome
    chrome_options.add_argument("--headless=new")  # 최신 headless 모드
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--log-level=3")
    chrome_options.page_load_strategy = "eager"
    tmp_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={tmp_profile}")
    service = Service(driver_path)
    print(chromedriver_autoinstaller.get_chrome_version())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
