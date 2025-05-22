import re
from playwright.sync_api import Page, expect
import pytest


# unittest.TestCase 대신 pytest 클래스로 변경
class TestTC008:

    # setUp, tearDown 대신 pytest의 page fixture를 사용합니다.
    # 테스트 함수는 page: Page 인자를 받습니다.

    def test_add_to_cart(self, page: Page):
    """상품을 장바구니에 추가하는 기능 테스트"""
    page.goto("https://www.nibbuns.co.kr/")

        try:
            # 상품 상세 페이지로 이동 (헬퍼 메서드 내용을 여기에 포함)
            # 첫 번째 제품 선택 (클래스 이름 'item-wrap'을 가진 요소)
            product_locator = page.locator(".item-wrap").first
            product_locator.click() # Playwright는 클릭 가능할 때까지 자동 대기
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 옵션 선택 (있는 경우)
            try:
                # 클래스 이름 'option-select'를 가진 select 태그를 찾고 index 1 옵션 선택
                option_select_locator = page.locator("select.option-select")
                option_select_locator.select_option(index=1) # 첫 번째 옵션 선택 (index 0은 보통 "선택하세요")
            except Exception: # Playwright에서는 NoSuchElementException 대신 다른 예외 발생 가능
                # 옵션이 없는 경우 통과
                pass

            # 장바구니 버튼 클릭
            # 클래스 이름 'cart'를 가진 a 태그를 찾고 클릭
            cart_button_locator = page.locator("a.cart")
            cart_button_locator.click() # Playwright는 클릭 가능할 때까지 자동 대기
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 장바구니 팝업/알림 확인
            try:
                # 확인 버튼 클릭 (alert 또는 confirm)
                # alert 발생 전에 dialog 핸들러 등록
                page.on("dialog", lambda dialog: dialog.accept())
                # alert가 나타날 때까지 기다리는 명시적 코드는 필요 없습니다.
                # click() 메서드 호출 후 Playwright가 자동으로 dialog를 감지하고 핸들러 실행.
            except Exception: # Playwright에서는 다른 예외 발생 가능
                # 알림이 없거나 이미 처리된 경우
                pass

            # 장바구니 페이지로 이동
            page.goto("https://www.nibbuns.co.kr/shop/cart.html")
            # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

            # 장바구니에 상품이 있는지 확인
            # 클래스 이름 'cart-item'을 가진 요소들이 나타날 때까지 대기
            cart_items_locators = page.locator(".cart-item")
            # unittest.TestCase의 assert 대신 Playwright expect 사용
            expect(cart_items_locators).to_have_count(expect.be_greater_than(0)) # 상품이 1개 이상인지 확인

        except Exception as e: # TimeoutError 등 Playwright 예외 포함
            print(f"An error occurred during add to cart test: {e}")
            pytest.fail(f"장바구니 추가 기능 테스트 실패: {e}") # pytest에서 테스트 실패로 표시

def test_update_cart_quantity(self):
    """장바구니 상품 수량 변경 기능 테스트"""
    # 상품을 장바구니에 먼저 추가
    self.test_add_to_cart()

    try:
        # 수량 입력 필드 찾기
        # 클래스 이름 'quantity'를 가진 input 태그를 찾습니다.
        quantity_input_locator = page.locator("input.quantity")
        # Playwright는 요소가 존재할 때까지 자동 대기합니다.
        # expect(quantity_input_locator).to_be_visible() # 명시적 대기 예시

        # 현재 수량 기록
        original_qty = quantity_input_locator.input_value() # get_attribute("value") 대신 input_value()

        # 수량 변경
        quantity_input_locator.fill("2") # clear() + send_keys() 대신 fill() 사용

        # 수량 업데이트 버튼 클릭
        # 클래스 이름 'update-qty'를 가진 a 태그를 찾고 클릭
        update_button_locator = page.locator("a.update-qty")
        update_button_locator.click() # Playwright는 클릭 가능할 때까지 자동 대기
        # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

        # 페이지 새로고침 후 수량 확인
        page.reload() # driver.refresh() 대신 page.reload()
        # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

        # 업데이트된 수량 확인
        updated_quantity_input_locator = page.locator("input.quantity")
        updated_qty = updated_quantity_input_locator.input_value() # get_attribute("value") 대신 input_value()
        # unittest.TestCase의 assert 대신 Playwright expect 사용
        expect(updated_quantity_input_locator).to_have_value("2") # 수량 입력 필드의 값이 '2'인지 확인

    except Exception as e: # TimeoutError 등 Playwright 예외 포함
        print(f"An error occurred during update quantity test: {e}")
        pytest.fail(f"장바구니 수량 변경 기능 테스트 실패: {e}") # pytest에서 테스트 실패로 표시

def test_remove_from_cart(self):
    """장바구니에서 상품 제거 기능 테스트"""
    # 상품을 장바구니에 먼저 추가
    self.test_add_to_cart()

    try:
        # 장바구니에 담긴 상품 수 확인
        cart_items_locators = page.locator(".cart-item")
        # 요소들이 나타날 때까지 대기 (Playwright auto-waiting)
        initial_count = cart_items_locators.count() # 요소 개수 확인

        # 삭제 버튼 찾아 클릭
        # 클래스 이름 'delete-item'을 가진 a 태그를 찾습니다.
        delete_button_locator = page.locator("a.delete-item").first # 첫 번째 삭제 버튼
        # Playwright는 클릭 가능할 때까지 자동 대기합니다.
        # expect(delete_button_locator).to_be_visible() # 명시적 대기 예시

        # alert 발생 전에 dialog 핸들러 등록
        page.on("dialog", lambda dialog: dialog.accept())
        delete_button.click()

        # 확인 알림 처리
        try:
            # page.on("dialog", ...) 핸들러가 이미 처리합니다.
            pass

        # 페이지 새로고침
        page.reload() # driver.refresh() 대신 page.reload()
        # time.sleep(2) # Playwright auto-waiting으로 대부분 불필요

        # 장바구니 항목이 감소했는지 확인
        try:
            cart_items_after_locators = page.locator(".cart-item")
            # unittest.TestCase의 assert 대신 Playwright expect 사용
            # 삭제 후 항목 수가 초기 수보다 적거나 (1개 삭제 시) 0개인지 확인
            # expect(cart_items_after_locators).to_have_count(expect.be_less_than(initial_count)) # 항목 수가 감소했는지 확인
            # 또는 항목이 모두 삭제되었다면 0개인지 확인
            expect(cart_items_after_locators).to_have_count(0)

        except Exception: # 항목이 모두 삭제되어 .cart-item이 없을 때 발생하는 예외 포함
            # 항목이 모두 삭제되었다면 "장바구니가 비어 있습니다" 메시지 확인
            empty_cart_msg_locator = page.locator(".empty-cart")
            expect(empty_cart_msg_locator).to_be_visible() # 비어있다는 메시지가 보이는지 확인

    except Exception as e: # TimeoutError 등 Playwright 예외 포함
        print(f"An error occurred during remove from cart test: {e}")
        pytest.fail(f"장바구니 상품 제거 기능 테스트 실패: {e}") # pytest에서 테스트 실패로 표시
