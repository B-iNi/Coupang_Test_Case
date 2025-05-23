import pytest
import random
import time
from playwright.sync_api import Page, expect

BESTSELLER_URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST"

def scroll_to_bottom(page: Page, delay: float = 2.0):
    """페이지 맨 아래로 스크롤하고 로딩을 기다림"""
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)

def test_003(page: Page):
    # 1. 베스트셀러 페이지 열기
    page.goto(BESTSELLER_URL, wait_until="domcontentloaded")

    # 2. 스크롤을 여러 번 내려 상품 로딩
    for _ in range(6):
        scroll_to_bottom(page)

    # 3. 모든 상품 이미지 수집
    product_imgs = page.locator("img.MS_prod_img_l")
    product_count = product_imgs.count()
    assert product_count >= 50, f"상품 수가 부족함: {product_count}개"

    # 4. 상품 중 하나를 랜덤으로 선택해 클릭
    random_index = random.randint(0, product_count - 1)
    print(f"👉 {random_index + 1}번째 상품 클릭")
    product_imgs.nth(random_index).click()

    # 5. 옵션 셀렉트박스 로딩 대기
    page.wait_for_selector("select[name='optionlist[]']", timeout=5000)

    # 6. 옵션 목록 수집 (value가 비어있지 않은 항목만)
    options = page.locator("select[name='optionlist[]'] option").all()
    valid_options = [
        opt for opt in options if opt.get_attribute("value") not in ("", None)
    ]
    assert valid_options, "선택 가능한 옵션이 없습니다!"

    # 7. 랜덤으로 하나의 옵션 선택
    selected_option = random.choice(valid_options)
    option_value = selected_option.get_attribute("value")
    option_text = selected_option.text_content()

    # 8. 옵션 선택 실행
    page.select_option("select[name='optionlist[]']", value=option_value)
    print(f"✅ 선택한 옵션: {option_text} (value={option_value})")

def test_004(page: Page):
    # 1. 베스트셀러 페이지 열기
    page.goto(BESTSELLER_URL, wait_until="domcontentloaded")

    # 2. 스크롤을 여러 번 내려 상품 로딩
    for _ in range(6): # 기존과 동일하게 6번 스크롤
        scroll_to_bottom(page)

    # 3. 모든 상품 이미지 수집
    product_imgs = page.locator("img.MS_prod_img_l")
    product_count = product_imgs.count()
    assert product_count >= 50, f"상품 수가 부족함: {product_count}개 (2개 옵션 테스트용)"

    # 4. 상품 중 하나를 랜덤으로 선택해 클릭
    random_index = random.randint(0, product_count - 1)
    print(f"👉 {random_index + 1}번째 상품 클릭 (2개 옵션 테스트용)")
    product_imgs.nth(random_index).click()

    # 5. 옵션 셀렉트박스 로딩 대기
    option_select_locator_str = "select[name='optionlist[]']"
    page.wait_for_selector(option_select_locator_str, timeout=7000) # 타임아웃 약간 증가

    # 6. 옵션 목록 수집 (value가 비어있지 않은 항목만)
    options = page.locator(f"{option_select_locator_str} option").all()
    valid_options = [
        opt for opt in options if opt.get_attribute("value") not in ("", None)
    ]

    if len(valid_options) < 2:
        pytest.skip(f"선택할 수 있는 유효한 옵션이 2개 미만입니다 ({len(valid_options)}개 발견). 테스트를 건너뜁니다.")

    # 7. 랜덤으로 2개의 옵션 선택 (중복 없이)
    selected_option_elements = random.sample(valid_options, 2)

    # 8. 첫 번째 옵션 선택 실행
    print(f"✅ 첫 번째 선택 시도 옵션: {selected_option_elements[0].text_content()} (value={selected_option_elements[0].get_attribute('value')})")
    page.select_option(option_select_locator_str, value=selected_option_elements[0].get_attribute("value"))
    page.wait_for_timeout(500) # 첫 번째 옵션 선택 후 UI 반응 대기 (필요에 따라 조정)

    # 9. 두 번째 옵션 선택 실행
    print(f"✅ 두 번째 선택 시도 옵션: {selected_option_elements[1].text_content()} (value={selected_option_elements[1].get_attribute('value')})")
    page.select_option(option_select_locator_str, value=selected_option_elements[1].get_attribute("value"))
    print(f"✅ 최종 선택된 옵션 (확인용): {selected_option_elements[1].text_content()} (value={selected_option_elements[1].get_attribute('value')})")
    

def test_005(page: Page):
    page.goto(BESTSELLER_URL, wait_until="domcontentloaded")
    for _ in range(6):
        scroll_to_bottom(page)

    product_imgs = page.locator("img.MS_prod_img_l")
    product_count = product_imgs.count()
    assert product_count >= 50, f"상품 수가 부족함: {product_count}개"

    random_index = random.randint(0, product_count - 1)
    print(f"👉 {random_index + 1}번째 상품 클릭")
    product_imgs.nth(random_index).click()

    page.wait_for_selector("select[name='optionlist[]']", timeout=5000)

    options = page.locator("select[name='optionlist[]'] option").all()
    valid_options = [opt for opt in options if opt.get_attribute("value") not in ("", None)]
    assert valid_options, "선택 가능한 옵션이 없습니다!"

    selected_option = random.choice(valid_options)
    option_value = selected_option.get_attribute("value")
    option_text = selected_option.text_content()
    page.select_option("select[name='optionlist[]']", value=option_value)
    print(f"✅ 선택한 옵션: {option_text} (value={option_value})")

    # 수량 조절 버튼과 입력 필드 로딩 대기
    page.wait_for_selector("a.MK_btn-up", timeout=5000)
    page.wait_for_selector("input#MS_amount_basic_0")

    # 1~4 사이로 랜덤 수량 증가 횟수
    increase_times = random.randint(1, 4)
    for _ in range(increase_times):
        page.click("a.MK_btn-up")
        time.sleep(0.3)  # UI 반응 대기

    # 0 ~ (increase_times - 1) 사이로 감소
    decrease_times = random.randint(0, increase_times - 1)
    for _ in range(decrease_times):
        page.click("a.MK_btn-dw")
        time.sleep(0.3)  # UI 반응 대기

    # 최종 수량 읽기
    quantity_input = page.locator("input#MS_amount_basic_0")
    final_quantity = quantity_input.input_value()
    print(f"🧾 수량 증가 횟수: {increase_times}")
    print(f"🧾 수량 감소 횟수: {decrease_times}")
    print(f"✅ 최종 수량: {final_quantity}")

    # 검증 (최소 수량이 1 이상이어야 함)
    assert int(final_quantity) >= 1, "최종 수량은 1 이상이어야 합니다."