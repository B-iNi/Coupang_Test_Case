import pytest
from playwright.sync_api import Page, expect
import re

# It's good practice to define base URLs or common selectors as constants if they are used multiple times.
BASE_URL = "https://www.nibbuns.co.kr/"

class TestNibbunsProductFlows:

    def test_product_search(self, page: Page):
        """상품 검색 기능 테스트"""
        page.goto(BASE_URL)

        # 검색창 찾기 및 검색어 입력
        search_box = page.locator("#keyword")  # 실제 ID 확인 필요
        # search_box.clear() # .fill() clears the input first
        search_box.fill("바지")  # 검색어
        search_box.press("Enter")

        # 검색 결과 확인
        # Playwright auto-waits for elements to be available.
        # We expect a list of products to be visible.
        product_list_container = page.locator(".prdList") # Selector for the product list area
        expect(product_list_container).to_be_visible(timeout=10000)

        # 검색 결과 수 확인
        products_locators = page.locator(".prdList > li") # Selector for individual product items
        
        # Expect at least one product to be found and visible
        expect(products_locators.first).to_be_visible(timeout=5000) # Wait for the first product to appear
        
        product_count = products_locators.count()
        print(f"검색된 상품 수: {product_count}")
        assert product_count > 0, "검색 결과가 없습니다."

    def test_product_details(self, page: Page):
        """상품 상세 페이지 테스트"""
        page.goto(BASE_URL)

        # 카테고리로 이동 (예: 아우터)
        # Using a text-based selector for the category link.
        # This is often more resilient to minor HTML structure changes than complex XPaths.
        category_menu = page.locator("a:has-text('아우터')")
        expect(category_menu).to_be_visible(timeout=10000)
        category_menu.click()

        # 페이지 이동 후 상품 목록이 나타날 때까지 기다릴 수 있습니다.
        # 예: expect(page.locator(".prdList")).to_be_visible(timeout=10000)
        # 또는 URL 변경을 확인할 수 있습니다.
        # expect(page).to_have_url(re.compile(r".*category_path_for_outer.*"), timeout=10000)


        # 첫 번째 상품 선택
        first_product_link = page.locator(".prdList li:first-child a")
        expect(first_product_link).to_be_clickable(timeout=10000)
        first_product_link.click()

        # 상품 상세 페이지 요소 확인
        # detailArea ID를 가진 요소가 나타날 때까지 기다립니다.
        detail_area = page.locator("#detailArea")
        expect(detail_area).to_be_visible(timeout=10000)

        # 상품명 확인
        product_name_element = page.locator(".headingArea h2") # Selector from original
        expect(product_name_element).to_be_visible()
        product_name = product_name_element.text_content().strip()
        print(f"상품명: {product_name}")
        assert len(product_name) > 0, "상품명이 표시되지 않습니다."

        # 가격 확인
        price_element = page.locator(".price") # Selector from original
        expect(price_element).to_be_visible()
        price = price_element.text_content().strip()
        print(f"가격: {price}")
        assert len(price) > 0, "가격이 표시되지 않습니다."

    def _add_product_to_cart(self, page: Page, search_term: str, quantity: str = "1", select_options: bool = True):
        """Helper function to search for a product, optionally select options, and add to cart."""
        # This helper assumes it might be called from various states, so it starts by ensuring it's on the base URL.
        # If called sequentially where page state is known, this goto can be conditional.
        # page.goto(BASE_URL) # Uncomment if this helper needs to be fully standalone for each call

        search_box = page.locator("#keyword")
        search_box.fill(search_term)
        search_box.press("Enter")

        # 첫 번째 상품 선택
        first_product_link = page.locator(".prdList li:first-child a")
        expect(first_product_link).to_be_clickable(timeout=10000)
        first_product_link.click()

        # 상품 상세 페이지 로드 확인
        expect(page.locator("#detailArea")).to_be_visible(timeout=10000)

        if select_options:
            # 상품 옵션 선택 (사이즈) - 실제 ID와 옵션 값 확인 필요
            size_select = page.locator("#product_option_id1") # 실제 사이즈 선택 select ID
            if size_select.is_visible(timeout=5000):
                if size_select.locator("option").count() > 1: # Placeholder가 아닌 실제 옵션이 있는지 확인
                    size_select.select_option(index=1)  # 두 번째 옵션 선택 (첫 번째는 보통 "선택하세요")
                else:
                    print(f"'{search_term}' 상품의 사이즈 옵션(#product_option_id1)에 선택할 항목이 없습니다.")
            else:
                print(f"'{search_term}' 상품의 사이즈 옵션(#product_option_id1)을 찾을 수 없습니다.")

            # 색상 옵션이 있다면 선택 - 실제 ID와 옵션 값 확인 필요
            color_select = page.locator("#product_option_id2") # 실제 색상 선택 select ID
            if color_select.is_visible(timeout=3000): # 색상 옵션은 선택 사항일 수 있으므로 짧은 타임아웃
                if color_select.locator("option").count() > 1:
                     color_select.select_option(index=1) # 두 번째 옵션 선택
                else:
                    print(f"'{search_term}' 상품의 색상 옵션(#product_option_id2)에 선택할 항목이 없습니다.")
            else:
                print(f"'{search_term}' 상품의 색상 옵션(#product_option_id2)이 없거나 시간 내에 나타나지 않았습니다.")
        
        # 수량 변경
        quantity_input = page.locator("#quantity") # 실제 수량 input ID
        if quantity_input.is_visible(timeout=3000):
            quantity_input.fill(quantity)
        else:
            print(f"'{search_term}' 상품의 수량 입력 필드(#quantity)를 찾을 수 없습니다.")


        # 장바구니 버튼 클릭
        add_to_cart_button = page.locator(".btnBasket") # 실제 장바구니 버튼 selector
        expect(add_to_cart_button).to_be_clickable()
        add_to_cart_button.click()

        # 장바구니 추가 확인 팝업/레이어 확인
        confirm_layer = page.locator("#confirmLayer") # 실제 확인 레이어 selector
        expect(confirm_layer).to_be_visible(timeout=10000)

        # 장바구니로 이동 버튼 클릭
        go_to_cart_button = confirm_layer.locator(".btnSubmit") # 확인 레이어 내의 장바구니 이동 버튼
        expect(go_to_cart_button).to_be_clickable()
        go_to_cart_button.click()

        # 장바구니 페이지 확인 (URL 또는 특정 요소로)
        # expect(page).to_have_url(re.compile(r".*/order/basket\.html"), timeout=10000) # 실제 장바구니 URL 패턴
        expect(page.locator(".xans-order-basketpackage")).to_be_visible(timeout=10000) # 장바구니 페이지 특정 요소

    def test_add_to_cart(self, page: Page):
        """장바구니 추가 테스트"""
        page.goto(BASE_URL) # 각 테스트는 독립적으로 시작
        self._add_product_to_cart(page, search_term="티셔츠", quantity="2", select_options=True)

        # 장바구니에 상품이 있는지 확인
        cart_items = page.locator(".xans-order-basketpackage .xans-record-") # 장바구니 아이템 selector
        expect(cart_items.count()).to_be_greater_than(0, message="장바구니에 상품이 추가되지 않았습니다.")
        
        # 추가적으로 특정 상품명, 수량 등을 확인할 수 있습니다.
        # first_item_name = cart_items.first.locator(".item_name_selector").text_content()
        # expect(first_item_name).to_contain("티셔츠")
        # first_item_quantity = cart_items.first.locator("input.quantity_selector").input_value()
        # expect(first_item_quantity).to_equal("2")


    def test_checkout_process(self, page: Page):
        """결제 프로세스 테스트 (실제 결제 제외)"""
        page.goto(BASE_URL) # 각 테스트는 독립적으로 시작
        # 장바구니에 상품 추가 (헬퍼 함수 사용)
        self._add_product_to_cart(page, search_term="자켓", quantity="1", select_options=True)

        # 현재 장바구니 페이지에 있어야 합니다.
        # 주문하기 버튼 클릭
        order_button = page.locator(".orderBtn .btnSubmit") # 장바구니 페이지의 주문 버튼 selector
        expect(order_button).to_be_clickable()
        order_button.click()

        # 주문 페이지 로딩 또는 로그인/비회원 구매 페이지 확인
        order_form_locator = page.locator("#order_form")
        guest_order_button_locator = page.locator(".xans-member-login .btn_GUEST_ORDER") # 비회원 주문 버튼 selector

        # 주문서 양식이 바로 보이는지 확인, 아니라면 비회원 주문 시도
        try:
            expect(order_form_locator).to_be_visible(timeout=5000) # 주문서가 바로 보이면 통과 (로그인 상태 등)
            print("주문서 양식(#order_form)이 바로 표시됨.")
        except AssertionError: # TimeoutError는 Playwright에서 AssertionError의 한 종류로 처리될 수 있음
            print("주문서 양식이 바로 표시되지 않음. 비회원 구매 옵션 확인 중...")
            if guest_order_button_locator.is_visible(timeout=5000):
                print("비회원 구매 버튼을 찾았습니다. 클릭합니다.")
                guest_order_button_locator.click()
                # 비회원 구매 클릭 후 주문서 양식이 나타나는지 다시 확인
                expect(order_form_locator).to_be_visible(timeout=10000)
            else:
                # 이 경우는 로그인도 안되어있고, 비회원 구매 버튼도 없는 예외적인 상황
                pytest.fail("주문서 양식도, 비회원 구매 버튼도 찾을 수 없습니다. 페이지 상태를 확인하세요.")
        
        # 주문서 정보 입력 (실제 주문은 하지 않음)
        # 수령자 정보
        name_field = page.locator("#rname") # 수령자 이름 필드 ID
        expect(name_field).to_be_visible()
        name_field.fill("홍길동")
        expect(name_field).to_have_value("홍길동")

        # 여기에 추가적인 주문서 필드 입력 및 검증 로직을 추가할 수 있습니다.
        # 예: 전화번호, 주소 등
        # phone_field = page.locator("#rphone")
        # phone_field.fill("01012345678")
        # expect(phone_field).to_have_value("01012345678")

        print("결제 프로세스 테스트 중 주문서 일부 입력 완료 (실제 결제는 진행하지 않음).")
