from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


class profile:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = ws(self.driver, 10)

        # 슬라이더 XPATH 설정
        self.sliders = {
            "단맛": '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[1]/div/span[1]/span[2]/span',
            "짠맛": '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[2]/div/span[1]/span[2]/span',
            "매운맛": '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[3]/div/span[1]/span[2]/span'
        }

    # 개인 피드 접근
    def peed_open(self):
        peedbtn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/ul/li[4]/a")))
        peedbtn.click()

    # 프로필 수정 페이지 접근
    def profile_modify(self):
        modifybtn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\]> main > section > section > section > div.flex.items-center.w-full.gap-4 > div.flex.flex-col.w-full.gap-2 > div > svg")
            )
        )
        modifybtn.click()

    # 프로필 사진 변경
    def add_profileimage(self, image_filename="cat.png"):
        proimagebtn = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/div[1]/div/button"))
        )
        proimagebtn.click()

        file_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        image_path = rf"C:\Users\zz910\OneDrive\Desktop\{image_filename}"
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"❌ 이미지 파일을 찾을 수 없습니다: {image_path}")

        file_input.send_keys(image_path)
    
    # 슬라이더 조절 함수
    def drag_slider(self, slider_name, target_value, min_value=0.0, max_value=5.0):
        slider_xpath = self.sliders.get(slider_name)
        if not slider_xpath:
            raise ValueError(f"❌ 슬라이더 '{slider_name}'를 찾을 수 없습니다!")

        slider_element = self.wait.until(EC.presence_of_element_located((By.XPATH, slider_xpath)))
        actions = ActionChains(self.driver)
        slider_bar = slider_element.find_element(By.XPATH, "./parent::span/preceding-sibling::span")
        slider_width = slider_bar.size['width']

        # 🎯 초기화 (최소값으로 이동)
        actions.click_and_hold(slider_element).move_by_offset(-slider_width, 0.0).release().perform()

        # 🎯 목표값 이동 계산 및 이동
        move_ratio = (target_value - min_value) / (max_value - min_value)
        move_distance = int(slider_width * move_ratio)

        # 🎯 이동 범위 제한
        move_distance = max(0, min(move_distance, slider_width))  # 이동 거리를 0과 slider_width 사이로 제한
        actions.click_and_hold(slider_element).move_by_offset(move_distance, 0.0).release().perform()

        # 🎯 값 검증
        updated_value = float(slider_element.get_attribute("aria-valuenow"))
        print(f"✅ 업데이트된 {slider_name} 슬라이더 값: {updated_value}")
        
        # 허용 오차
        tolerance = 0.15
        print(f"✅ 허용 오차값 {tolerance}")
        if abs(updated_value - target_value) > tolerance:
            raise AssertionError(f"❌ {slider_name} 슬라이더 값이 {target_value}이어야 하는데 {updated_value}입니다!")
        print(f"✅ {slider_name} 슬라이더 값이 목표값 {target_value}에 근접합니다.")
        

    # 좋아하는 음식 입력
    def like_food(self):
        textarea_xpath = '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/textarea'
        target_text = "좋아하는 음식 테스트 입니다."
        textarea = self.wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))
        textarea.clear()
        textarea.send_keys(target_text)
        print(f"✅ 좋아하는 음식 입력 완료: {target_text}")

    # 싫어하는 음식 입력
    def hate_food(self):
        textarea_xpath = '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/textarea'
        target_text = "싫어하는 음식 테스트 입니다."
        textarea = self.wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))
        textarea.clear()
        textarea.send_keys(target_text)
        print(f"✅ 싫어하는 음식 입력 완료: {target_text}")

    #수정 완료 버튼
    def modify_access(self):
        endbtn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/button")))
        endbtn.click()
