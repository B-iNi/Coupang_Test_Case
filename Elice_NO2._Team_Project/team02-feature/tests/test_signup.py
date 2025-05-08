import pytest
import random, string
import logging
from selenium import webdriver
from src.pages.Sign_Up_page import Sign_Up_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_random_email():
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    domain = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"{user}@{domain}.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def signup_page(driver):
    page = Sign_Up_page(driver)
    page.open()
    return page
    



#---------------------------------------------------------------------
# 입력칸 UI 확인
def test_TC_002(signup_page):
    logging.info("📋 TC_002 / Test Start!")

    assert signup_page.driver.find_element(*signup_page.Username_input).is_displayed()
    logging.info("Username input Box ✅")
    assert signup_page.driver.find_element(*signup_page.Email_input).is_displayed()
    logging.info("Email input Box ✅")
    assert signup_page.driver.find_element(*signup_page.Password_input).is_displayed()
    logging.info("Password input Box ✅")

#---------------------------------------------------------------------
# 버튼 UI 확인
def test_TC_003(signup_page):
    logging.info("📋 TC_003 / Test Start!")

    assert signup_page.driver.find_element(*signup_page.Sign_up_button).is_displayed()
    logging.info("Sign up Button ✅")
    assert signup_page.driver.find_element(*signup_page.Have_an_account_button).is_displayed()
    logging.info("Have an account Button ✅")
    assert signup_page.driver.find_element(*signup_page.conduit).is_displayed()
    logging.info("Conduit Button ✅")
    assert signup_page.driver.find_element(*signup_page.Home).is_displayed()
    logging.info("Home Button ✅")
    assert signup_page.driver.find_element(*signup_page.Sign_in).is_displayed()
    logging.info("sign in Button ✅")
    assert signup_page.driver.find_element(*signup_page.Sign_up).is_displayed()
    logging.info("Sign up Button ✅")


#---------------------------------------------------------------------
# 회원가입 확인
def test_TC_004(signup_page):
    logging.info("📋 TC_004 / Test Start!")

    username = generate_random_username()
    email = generate_random_email()
    password = generate_random_password()
    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)
    

    expected_url = "http://localhost:4100"
    wait.until(EC.url_changes(expected_url))  
    assert signup_page.driver.current_url != expected_url
    logging.info("회원가입 완료! ✅")


#---------------------------------------------------------------------
# username 미 입력 확인
def test_TC_005(signup_page):
    logging.info("📋 TC_005 / Test Start!")

    email = generate_random_email()
    password = generate_random_password()
    username = ""

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)
    
    
    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info("회원가입 실패 ✅")

#---------------------------------------------------------------------
# email 미 입력 확인
def test_TC_007(signup_page):
    logging.info("📋 TC_007 / Test Start!")

    email = "" 
    password = generate_random_password()
    username = generate_random_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info("회원가입 실패 ✅")
   
#---------------------------------------------------------------------
# password 미 입력 확인
def test_TC_009(signup_page):
    logging.info("📋 TC_009 / Test Start!")

    email = generate_random_email()
    password = ""
    username = generate_random_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info("회원가입 실패 ✅")

#---------------------------------------------------------------------    
# username, email, password 미 입력 확인
def test_TC_010(signup_page):
    logging.info("📋 TC_010 / Test Start!")
    email = ""
    password = ""
    username = ""

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: {password}")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info("회원가입 실패✅")

#---------------------------------------------------------------------    
# Have an account 버튼 클릭 확인
def test_TC_011(signup_page):
    logging.info("📋 TC_010 / Test Start!")

    wait = WebDriverWait(signup_page.driver,10)
    wait.until(EC.element_to_be_clickable(signup_page.Have_an_account_button)).click()
    logging.info("Have an account Button click!")

    expected_url = "http://localhost:4100/login"
    wait.until(EC.url_to_be(expected_url))
    assert signup_page.driver.current_url == expected_url
    logging.info(signup_page.driver.current_url)
    logging.info("로그인 페이지 이동 완료✅")

