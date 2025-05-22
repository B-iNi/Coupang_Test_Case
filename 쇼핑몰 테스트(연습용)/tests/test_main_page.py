import re
from playwright.sync_api import Page, expect
import pytest

# 메인페이지 테스트 시나리오

# unittest.TestCase 대신 pytest 클래스로 변경
class TestMainPage:

    # setUp, tearDown 대신 pytest의 page fixture를 사용합니다.
    # 테스트 함수는 page: Page 인자를 받습니다.
    def test_main_page_loads(self, page: Page):
        """메인 페이지가 올바르게 로드되는지 테스트"""
        page.goto("https://www.nibbuns.co.kr/")
        # unittest.TestCase의 assert 대신 Playwright expect 사용
        expect(page).to_have_title(re.compile(r".*니쁜스.*")) # 타이틀에 "니쁜스"가 포함되는지 확인

    def test_navigation_menu(self, page: Page):
        """네비게이션 메뉴가 존재하고 클릭 가능한지 테스트"""
        page.goto("https://www.nibbuns.co.kr/")
        try:
            # 메뉴 요소 찾기 (실제 선택자는 웹사이트에 맞게 조정 필요)
            # CSS 선택자 'ul.nav > li'를 가진 모든 요소를 찾습니다.
            menu_locators = page.locator("ul.nav > li")
            # Playwright는 요소가 존재할 때까지 자동 대기합니다.

            # 최소한 몇 개의 메뉴 항목이 있는지 확인
            # unittest.TestCase의 assert 대신 Playwright expect 사용
            expect(menu_locators).to_have_count(expect.be_greater_than(0)) # 메뉴 항목이 1개 이상인지 확인

            # 첫 번째 메뉴 클릭 테스트
            menu_locators.first.click() # 첫 번째 메뉴 클릭 (Playwright는 클릭 가능할 때까지 자동 대기)
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 페이지 이동 확인 (URL 변경)
            # 현재 URL이 메인 페이지 URL과 다른지 확인
            expect(page).not_to_have_url("https://www.nibbuns.co.kr/")

        except Exception as e: # TimeoutError 등 Playwright 예외 포함
            print(f"An error occurred during navigation menu test: {e}")
            pytest.fail(f"네비게이션 메뉴 테스트 실패: {e}") # pytest에서 테스트 실패로 표시

    def test_product_display(self, page: Page):
        """상품이 메인 페이지에 올바르게 표시되는지 테스트"""
        page.goto("https://www.nibbuns.co.kr/")
        try:
            # 상품 요소 찾기 (실제 선택자는 웹사이트에 맞게 조정 필요)
            # CSS 선택자 '.item-wrap'을 가진 모든 요소를 찾습니다.
            product_locators = page.locator(".item-wrap")
            # Playwright는 요소가 존재할 때까지 자동 대기합니다.

            # 상품이 표시되는지 확인
            # unittest.TestCase의 assert 대신 Playwright expect 사용
            expect(product_locators).to_have_count(expect.be_greater_than(0)) # 상품이 1개 이상인지 확인

            # 첫 번째 상품의 상세 페이지로 이동
            product_locators.first.click() # 첫 번째 상품 클릭 (Playwright는 클릭 가능할 때까지 자동 대기)
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 상품 상세 페이지에 필요한 요소가 있는지 확인
            product_title = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".item-title"))
            )
            self.assertIsNotNone(
                product_title, "상품 상세 페이지가 올바르게 로드되지 않았습니다"
            ) # 이 부분은 Playwright expect로 변경 필요
            # expect(page.locator(".item-title")).to_be_visible() # 상품 타이틀이 보이는지 확인

        except Exception as e: # TimeoutError 등 Playwright 예외 포함
            print(f"An error occurred during product display test: {e}")
            pytest.fail(f"상품 표시 테스트 실패: {e}") # pytest에서 테스트 실패로 표시

    def test_search_functionality(self, page: Page):
        """검색 기능이 올바르게 작동하는지 테스트"""
        page.goto("https://www.nibbuns.co.kr/")
        try:
            # 검색창 찾기
            # CSS 선택자 'input[name="search"]'를 가진 input 태그를 찾습니다.
            search_input_locator = page.locator("input[name='search']")
            # Playwright는 요소가 존재할 때까지 자동 대기합니다.

            # 검색어 입력 및 검색 실행
            search_term = "원피스"
            search_input_locator.fill(search_term) # send_keys 대신 fill 사용
            search_input_locator.press('Enter') # submit() 대신 press('Enter') 사용 (또는 검색 버튼 클릭)
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 검색 결과 확인
            # CSS 선택자 '.item-wrap'을 가진 모든 요소를 찾습니다.
            search_results_locators = page.locator(".item-wrap")
            # unittest.TestCase의 assert 대신 Playwright expect 사용
            expect(search_results_locators).to_have_count(expect.be_greater_than(0)) # 검색 결과가 1개 이상인지 확인

        except Exception as e: # TimeoutError 등 Playwright 예외 포함
            print(f"An error occurred during search functionality test: {e}")
            pytest.fail(f"검색 기능 테스트 실패: {e}") # pytest에서 테스트 실패로 표시
