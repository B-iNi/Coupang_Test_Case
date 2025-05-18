import pytest
import os
import time
import logging
from selenium import webdriver
from tests.pages.contact_page import ConTact_Page


log_file = os.path.join(os.getcwd(), "test_scenario_TC005.log")

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = log_file,
    encoding="utf-8",
    filemode = 'a',
    force=True
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def contact_page(driver):
    return ConTact_Page(driver)



# test1. 문의페이지 글쓰기 페이지 이동
def test_PAGE_MOVE(contact_page):
    logger.info("[Test1.] 문의페이지 >> 글쓰기 페이지 이동 테스트 시작")
    contact_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.driver.current_url
    #logger.info(f"✅ 현재 URL : {current_url}")
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)
    contact_page.CLICK_WRITING_BUTTON()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST1.] 테스트 완료")

# test2. 문의페이지 빈칸으로 작성시 작성 안됨
def test_NONE_NAME_PAGE(contact_page):
    logger.info("[Test2.] 글쓰기 페이지 미 입력 작성 테스트 시작")
    contact_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.driver.current_url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)

    contact_page.CLICK_WRITING_BUTTON()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    time.sleep(1)
    contact_page.WRITING_END_BUTTON()
    time.sleep(1)
    alert = contact_page.driver.switch_to.alert
    logger.info(f"✅ 팝업 등장 : {alert.text} - 기능 정상 작동")
    alert.accept()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST2.] 테스트 완료")
    
# test3. 문의페이지 PASSWORD 미 입력 작성시 작성 안됨
def test_NONE_PASSWORD_PAGE(contact_page):
    logger.info("[Test3.] 글쓰기 페이지 PASSWORD 미 입력 작성 테스트 시작")
    contact_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.driver.current_url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)
    contact_page.CLICK_WRITING_BUTTON()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    time.sleep(1)
    contact_page.WRITING_NAME("홍길동")
    time.sleep(1)
    contact_page.WRITING_END_BUTTON()
    time.sleep(1)
    alert = contact_page.driver.switch_to.alert
    logger.info(f"✅ 팝업 등장 : {alert.text} - 기능 정상 작동")
    alert.accept()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST3.] 테스트 완료")

# test4. 문의페이지 TITLE 미 선택 작성시 작성 안됨
def test_NONE_TITLE_PAGE(contact_page):
    logger.info("[Test4.] 글쓰기 페이지 TITLE 미 선택 작성 테스트 시작")
    contact_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.driver.current_url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)
    contact_page.CLICK_WRITING_BUTTON()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    time.sleep(1)
    contact_page.WRITING_NAME("홍길동")
    time.sleep(1)
    contact_page.WRITING_PASSWORD("123123")
    time.sleep(1)
    contact_page.WRITING_END_BUTTON()
    time.sleep(1)
    alert = contact_page.driver.switch_to.alert
    logger.info(f"✅ 팝업 등장 : {alert.text} - 기능 정상 작동")
    alert.accept()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST4.] 테스트 완료")

## test5. 문의페이지 CONTENT 미 작성시 작성 안됨
def test_NONE_CONTENT_PAGE(contact_page):
    logger.info("[Test5.] 글쓰기 페이지 CONTENT 미 작성 테스트 시작")
    contact_page.OPEN_INQUIRIES_PAGE("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.driver.current_url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    time.sleep(1)
    contact_page.CLICK_WRITING_BUTTON()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    time.sleep(1)
    contact_page.WRITING_NAME("홍길동")
    time.sleep(1)
    contact_page.WRITING_PASSWORD("123123")
    time.sleep(1)
    contact_page.TITLE_NOMAL()
    time.sleep(1)
    contact_page.WRITING_END_BUTTON()
    time.sleep(1)
    alert = contact_page.driver.switch_to.alert
    logger.info(f"✅ 팝업 등장 : {alert.text} - 기능 정상 작동")
    alert.accept()
    current_url = contact_page.driver.current_url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST5.] 테스트 완료")
