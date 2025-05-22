import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 메인페이지 테스트 시나리오


class NibbunsMainPageTest(unittest.TestCase):
    def setUp(self):
        # 웹드라이버 설정
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.nibbuns.co.kr/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        # 테스트 종료 후 브라우저 닫기
        self.driver.quit()

    def test_main_page_loads(self):
        """메인 페이지가 올바르게 로드되는지 테스트"""
        title = self.driver.title
        self.assertIn("니쁜스", title, "메인 페이지 타이틀이 올바르지 않습니다")

    def test_navigation_menu(self):
        """네비게이션 메뉴가 존재하고 클릭 가능한지 테스트"""
        try:
            # 메뉴 요소 찾기 (실제 선택자는 웹사이트에 맞게 조정 필요)
            menu_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.nav > li"))
            )
            # 최소한 몇 개의 메뉴 항목이 있는지 확인
            self.assertGreater(len(menu_elements), 0, "메뉴 항목이 존재하지 않습니다")

            # 첫 번째 메뉴 클릭 테스트
            menu_elements[0].click()
            # 페이지 이동 확인 (URL 변경 또는 새 요소 확인)
            time.sleep(2)
            current_url = self.driver.current_url
            self.assertNotEqual(
                "https://www.nibbuns.co.kr/",
                current_url,
                "메뉴 클릭 후 페이지가 변경되지 않았습니다",
            )

        except TimeoutException:
            self.fail("메뉴 요소를 찾을 수 없습니다")

    def test_product_display(self):
        """상품이 메인 페이지에 올바르게 표시되는지 테스트"""
        try:
            # 상품 요소 찾기 (실제 선택자는 웹사이트에 맞게 조정 필요)
            product_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-wrap"))
            )
            self.assertGreater(len(product_elements), 0, "상품이 표시되지 않습니다")

            # 첫 번째 상품의 상세 페이지로 이동
            product_elements[0].click()
            time.sleep(2)

            # 상품 상세 페이지에 필요한 요소가 있는지 확인
            product_title = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".item-title"))
            )
            self.assertIsNotNone(
                product_title, "상품 상세 페이지가 올바르게 로드되지 않았습니다"
            )

        except TimeoutException:
            self.fail("상품 요소를 찾을 수 없습니다")

    def test_search_functionality(self):
        """검색 기능이 올바르게 작동하는지 테스트"""
        try:
            # 검색창 찾기
            search_input = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[name='search']")
                )
            )

            # 검색어 입력 및 검색 실행
            search_term = "원피스"
            search_input.send_keys(search_term)
            search_input.submit()
            time.sleep(2)

            # 검색 결과 확인
            search_results = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-wrap"))
            )
            self.assertGreater(
                len(search_results), 0, f"{search_term} 검색 결과가 없습니다"
            )

        except TimeoutException:
            self.fail("검색 요소를 찾을 수 없습니다")
            
    driver.quit()
