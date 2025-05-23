import pytest
import os
import logging
from tests.pages.contact_page import ContactPage
from playwright.sync_api import Page, expect


log_file = os.path.join(os.getcwd(), "test_scenario_TC005.log")

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = log_file,
    encoding="utf-8", # 파일 모드를 'a' (append)로 설정하는 것이 좋습니다.
    filemode = 'a',
    force=True
)
logger = logging.getLogger(__name__)

@pytest.fixture
def contact_page(page: Page):
    # Playwright의 page fixture를 ConTact_Page에 전달합니다.
    return ContactPage(page)


# python -m pytest -s tests/test_scenario_TC005.py --headed

# test1. 문의페이지 글쓰기 페이지 이동
def test_PAGE_MOVE(contact_page):
    logger.info("[Test1.] 문의페이지 >> 글쓰기 페이지 이동 테스트 시작")
    contact_page.open_inquiries_page("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    # Playwright의 expect를 사용하여 URL 검증
    expect(contact_page.page).to_have_url("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.page.url # 로깅을 위해 URL 가져오기
    #logger.info(f"✅ 현재 URL : {current_url}")
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    # time.sleep(1) # Playwright는 자동 대기를 지원하므로 불필요할 수 있습니다.
    contact_page.click_writing_button()
    # 글쓰기 버튼 클릭 후 URL 변경 확인 (예시: write.html 포함)
    expect(contact_page.page).to_have_url(lambda url: "write.html" in url)
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST1.] 테스트 완료")

# test2. 문의페이지 빈칸으로 작성시 작성 안됨
def test_NONE_NAME_PAGE(contact_page):
    logger.info("[Test2.] 글쓰기 페이지 미 입력 작성 테스트 시작")
    contact_page.open_inquiries_page("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    expect(contact_page.page).to_have_url("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.page.url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"

    contact_page.click_writing_button()
    expect(contact_page.page).to_have_url(lambda url: "write.html" in url)
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")

    # alert 발생 전에 dialog 핸들러 등록
    contact_page.page.on("dialog", lambda dialog: (logger.info(f"✅ 팝업 등장 : {dialog.message} - 기능 정상 작동"), dialog.accept()))
    contact_page.click_writing_complete_button()
    # contact_page.page.on 핸들러가 dialog를 처리할 때까지 Playwright가 대기합니다.
    # time.sleep(1) # 일반적으로 불필요
    # 아래 alert 처리는 page.on("dialog",...) 핸들러로 대체되었으므로 제거 가능
    # alert = contact_page.driver.switch_to.alert
    # logger.info(f"✅ 팝업 등장 : {alert.text} - 기능 정상 작동")
    # alert.accept()
    current_url = contact_page.page.url # dialog 후에도 URL은 동일 페이지에 머무를 것으로 예상
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST2.] 테스트 완료")
    
# test3. 문의페이지 PASSWORD 미 입력 작성시 작성 안됨
def test_NONE_PASSWORD_PAGE(contact_page):
    logger.info("[Test3.] 글쓰기 페이지 PASSWORD 미 입력 작성 테스트 시작")
    contact_page.open_inquiries_page("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    expect(contact_page.page).to_have_url("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.page.url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    contact_page.click_writing_button()
    expect(contact_page.page).to_have_url(lambda url: "write.html" in url)
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    contact_page.fill_name("홍길동")

    # alert 발생 전에 dialog 핸들러 등록
    contact_page.page.on("dialog", lambda dialog: (logger.info(f"✅ 팝업 등장 : {dialog.message} - 기능 정상 작동"), dialog.accept()))
    contact_page.click_writing_complete_button()
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST3.] 테스트 완료")

# test4. 문의페이지 TITLE 미 선택 작성시 작성 안됨
def test_NONE_TITLE_PAGE(contact_page):
    logger.info("[Test4.] 글쓰기 페이지 TITLE 미 선택 작성 테스트 시작")
    contact_page.open_inquiries_page("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    expect(contact_page.page).to_have_url("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.page.url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    contact_page.click_writing_button()
    expect(contact_page.page).to_have_url(lambda url: "write.html" in url)
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    contact_page.fill_name("홍길동")
    contact_page.fill_password("123123")

    # alert 발생 전에 dialog 핸들러 등록
    contact_page.page.on("dialog", lambda dialog: (logger.info(f"✅ 팝업 등장 : {dialog.message} - 기능 정상 작동"), dialog.accept()))
    contact_page.click_writing_complete_button()
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST4.] 테스트 완료")

## test5. 문의페이지 CONTENT 미 작성시 작성 안됨
def test_NONE_CONTENT_PAGE(contact_page):
    logger.info("[Test5.] 글쓰기 페이지 CONTENT 미 작성 테스트 시작")
    contact_page.open_inquiries_page("https://www.nibbuns.co.kr/board/board.html?code=piasom") # 페이지 다시 열기
    expect(contact_page.page).to_have_url("https://www.nibbuns.co.kr/board/board.html?code=piasom")
    current_url = contact_page.page.url
    assert "nibbuns.co.kr/board/board.html" in current_url, "❌ 페이지 이동 실패"
    contact_page.click_writing_button()
    expect(contact_page.page).to_have_url(lambda url: "write.html" in url)
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    contact_page.fill_name("홍길동")
    contact_page.fill_password("123123")
    contact_page.select_title_normal()

    # alert 발생 전에 dialog 핸들러 등록
    contact_page.page.on("dialog", lambda dialog: (logger.info(f"✅ 팝업 등장 : {dialog.message} - 기능 정상 작동"), dialog.accept()))
    contact_page.click_writing_complete_button()
    current_url = contact_page.page.url
    logger.info(f"✅ 현재 URL : {current_url}")
    logger.info("✅[TEST5.] 테스트 완료")
