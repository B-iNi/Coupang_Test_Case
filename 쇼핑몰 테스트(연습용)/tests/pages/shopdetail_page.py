import pytest
import random
import time
from playwright.sync_api import Page, expect

BESTSELLER_URL = "https://www.nibbuns.co.kr/shop/bestseller.html?xcode=BEST"

def scroll_to_bottom(page: Page):
    page.evaluate("""
        () => {
            window.scrollTo(0, document.body.scrollHeight);
        }
    """)
    time.sleep(3)  # 스크롤 후 로딩 대기

@pytest.mark.parametrize("url", [BESTSELLER_URL])
def test_random_product_select_and_option(page: Page, url: str):
    page.goto(url)
    
    # 모든 상품 로딩될 때까지 스크롤 (최대 5회 반복)
    for _ in range(5):
        scroll_to_bottom(page)

    # 상품 이미지 요소 수집
    product_imgs = page.locator("img.MS_prod_img_l")
    count = product_imgs.count()
    assert count >= 50, f"상품이 50개 미만 로딩됨: {count}개"

    # 랜덤으로 상품 하나 클릭
    random_index = random.randint(0, count - 1)
    product_imgs.nth(random_index).click()

    # 옵션 드롭다운 박스 대기 및 로딩
    page.wait_for_selector("select[name='optionlist[]']")

    # 옵션 리스트 가져오기 (value가 빈 값 제외)
    options = page.locator("select[name='optionlist[]'] option").all()
    valid_options = [opt for opt in options if opt.get_attribute("value") != ""]

    assert valid_options, "옵션이 없습니다!"

    # 랜덤 옵션 선택
    selected = random.choice(valid_options)
    option_value = selected.get_attribute("value")
    option_text = selected.text_content()

    # 옵션 선택
    page.select_option("select[name='optionlist[]']", option_value)
    print(f"✅ 선택한 옵션: {option_text}")
