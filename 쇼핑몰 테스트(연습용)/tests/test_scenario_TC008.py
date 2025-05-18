import time

import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait, Select

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service


class NibbunsCartTest(unittest.TestCase):

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


def go_to_product_detail(self):
    """상품 상세 페이지로 이동하는 헬퍼 메서드"""

    try:

        # 첫 번째 제품 선택

        product = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-wrap"))
        )

        product.click()

        time.sleep(2)

        return True

    except (TimeoutException, NoSuchElementException):

        self.fail("상품을 찾을 수 없거나 클릭할 수 없습니다")

        return False


def test_add_to_cart(self):
    """상품을 장바구니에 추가하는 기능 테스트"""

    if self.go_to_product_detail():

        try:

            # 옵션 선택 (있는 경우)

            try:

                option_select = Select(
                    self.driver.find_element(By.CSS_SELECTOR, "select.option-select")
                )

                option_select.select_by_index(1)  # 첫 번째 옵션 선택

            except NoSuchElementException:

                # 옵션이 없는 경우 통과

                pass

            # 장바구니 버튼 클릭

            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cart"))
            )

            cart_button.click()

            time.sleep(2)

            # 장바구니 팝업/알림 확인

            try:

                # 확인 버튼 클릭 (alert 또는 confirm)

                self.driver.switch_to.alert.accept()

            except:

                # 알림이 없거나 이미 처리된 경우

                pass

            # 장바구니 페이지로 이동

            self.driver.get("https://www.nibbuns.co.kr/shop/cart.html")

            time.sleep(2)

            # 장바구니에 상품이 있는지 확인

            cart_items = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item"))
            )

            self.assertGreater(
                len(cart_items), 0, "상품이 장바구니에 추가되지 않았습니다"
            )

        except TimeoutException:

            self.fail("장바구니 관련 요소를 찾을 수 없습니다")


def test_update_cart_quantity(self):
    """장바구니 상품 수량 변경 기능 테스트"""

    # 상품을 장바구니에 먼저 추가

    self.test_add_to_cart()

    try:

        # 수량 입력 필드 찾기

        quantity_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.quantity"))
        )

        # 현재 수량 기록

        original_qty = quantity_input.get_attribute("value")

        # 수량 변경

        quantity_input.clear()

        quantity_input.send_keys("2")

        # 수량 업데이트 버튼 클릭

        update_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.update-qty"))
        )

        update_button.click()

        time.sleep(2)

        # 페이지 새로고침 후 수량 확인

        self.driver.refresh()

        time.sleep(2)

        # 업데이트된 수량 확인

        updated_quantity_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.quantity"))
        )

        updated_qty = updated_quantity_input.get_attribute("value")

        self.assertEqual(
            "2", updated_qty, "장바구니 수량이 올바르게 업데이트되지 않았습니다"
        )

    except TimeoutException:

        self.fail("장바구니 수량 관련 요소를 찾을 수 없습니다")


def test_remove_from_cart(self):
    """장바구니에서 상품 제거 기능 테스트"""

    # 상품을 장바구니에 먼저 추가

    self.test_add_to_cart()

    try:

        # 장바구니에 담긴 상품 수 확인

        cart_items_before = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item"))
        )

        initial_count = len(cart_items_before)

        # 삭제 버튼 찾아 클릭

        delete_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.delete-item"))
        )
    except:

        delete_button.click()

        # 확인 알림 처리

        try:

            self.driver.switch_to.alert.accept()

        except:

            pass

        time.sleep(2)

        # 페이지 새로고침

        self.driver.refresh()

        time.sleep(2)

        # 장바구니 항목이 감소했는지 확인

        try:

            cart_items_after = self.driver.find_elements(By.CSS_SELECTOR, ".cart-item")

            self.assertLess(
                len(cart_items_after),
                initial_count,
                "상품이 장바구니에서 삭제되지 않았습니다",
            )

        except:

            # 항목이 모두 삭제되었다면 "장바구니가 비어 있습니다" 메시지 확인

            empty_cart_msg = self.driver.find_element(By.CSS_SELECTOR, ".empty-cart")
