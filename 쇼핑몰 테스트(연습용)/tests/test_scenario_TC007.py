import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time


class NibbunsTest(unittest.TestCase):

    def setUp(self):
        # 웹드라이버 설정
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # 브라우저 최대화
        chrome_options.add_argument("--disable-notifications")  # 알림 비활성화

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.nibbuns.co.kr/")
        self.driver.implicitly_wait(10)  # 암시적 대기

    def test_product_search(self):
        """상품 검색 기능 테스트"""
        driver = self.driver

        # 검색창 찾기 및 검색어 입력
        search_box = driver.find_element(By.ID, "keyword")  # 실제 ID 확인 필요
        search_box.clear()
        search_box.send_keys("바지")  # 검색어
        search_box.send_keys(Keys.RETURN)

        # 검색 결과 확인
        try:
            pass  # Add your code here
        except Exception as e:
            print(f"An error occurred: {e}")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".prdList"))
            )
            # 검색 결과 수 확인
            products = driver.find_elements(By.CSS_SELECTOR, ".prdList > li")
            print(f"검색된 상품 수: {len(products)}")
            self.assertTrue(len(products) > 0, "검색 결과가 없습니다.")
        except TimeoutException:
            self.fail("검색 결과 페이지 로딩 실패")

    def test_product_details(self):
        """상품 상세 페이지 테스트"""
        driver = self.driver

        # 카테고리로 이동 (예: 여성 의류)
        try:
            category_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), '아우터')]")
                )
            )
            category_menu.click()

            # 첫 번째 상품 선택
            first_product = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".prdList li:first-child a")
                )
            )
            first_product.click()

            # 상품 상세 페이지 요소 확인
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "detailArea"))
            )

            # 상품명 확인
            product_name = driver.find_element(By.CSS_SELECTOR, ".headingArea h2").text
            print(f"상품명: {product_name}")
            self.assertTrue(len(product_name) > 0, "상품명이 표시되지 않습니다.")

            # 가격 확인
            price = driver.find_element(By.CSS_SELECTOR, ".price").text
            print(f"가격: {price}")
            self.assertTrue(len(price) > 0, "가격이 표시되지 않습니다.")

        except TimeoutException:
            self.fail("상품 상세 페이지 로딩 실패")

    def test_add_to_cart(self):
        """장바구니 추가 테스트"""
        driver = self.driver

        # 검색으로 상품 찾기
        search_box = driver.find_element(By.ID, "keyword")
        search_box.clear()
        search_box.send_keys("티셔츠")
        search_box.send_keys(Keys.RETURN)

        # 첫 번째 상품 선택
        first_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".prdList li:first-child a"))
        )
        first_product.click()

        # 상품 옵션 선택 (사이즈)
        try:
            size_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "product_option_id1"))
            )
            Select(size_select).select_by_index(1)  # 첫번째 사이즈 선택

            # 색상 옵션이 있다면 선택
            try:
                color_select = driver.find_element(By.ID, "product_option_id2")
                Select(color_select).select_by_index(1)  # 첫번째 색상 선택
            except:
                print("색상 옵션이 없습니다.")

            # 수량 변경
            quantity_input = driver.find_element(By.ID, "quantity")
            quantity_input.clear()
            quantity_input.send_keys("2")

            # 장바구니 버튼 클릭
            add_to_cart = driver.find_element(By.CSS_SELECTOR, ".btnBasket")
            add_to_cart.click()

            # 장바구니 추가 확인 팝업
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#confirmLayer"))
            )

            # 장바구니로 이동
            go_to_cart = driver.find_element(
                By.CSS_SELECTOR, "#confirmLayer .btnSubmit"
            )
            go_to_cart.click()

            # 장바구니 페이지 확인
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".xans-order-basketpackage")
                )
            )

            # 장바구니에 상품이 있는지 확인
            cart_items = driver.find_elements(
                By.CSS_SELECTOR, ".xans-order-basketpackage .xans-record-"
            )
            self.assertTrue(
                len(cart_items) > 0, "장바구니에 상품이 추가되지 않았습니다."
            )

        except TimeoutException:
            self.fail("장바구니 추가 테스트 실패")

    def test_checkout_process(self):
        """결제 프로세스 테스트 (실제 결제 제외)"""
        # 장바구니에 상품 추가 (이전 테스트 사용)
        self.test_add_to_cart()

        driver = self.driver

        try:
            # 주문하기 버튼 클릭
            order_button = driver.find_element(By.CSS_SELECTOR, ".orderBtn .btnSubmit")
            order_button.click()
        except:

            # 로그인 필요 시
            try:
                # 비회원 구매 선택 (혹은 로그인)
                guest_order = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".xans-member-login .btn_GUEST_ORDER")
                    )
                )
                guest_order.click()
            except TimeoutException:
                print("비회원 구매 옵션을 찾을 수 없습니다.")
            except:
                print("이미 로그인되어 있거나 비회원 구매 옵션이 없습니다.")

            # 주문 페이지 로딩 확인
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#order_form"))
            )

            # 주문서 정보 입력 (실제 주문은 하지 않음)
            # 수령자 정보
            name_field = driver.find_element(By.ID, "rname")
            name_field.clear()
            name_field.send_keys("홍길동")
