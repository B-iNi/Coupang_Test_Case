import os
import logging
import pytest
from coupang_main import driver_init


# 테스트 할때마다 이거 적기 귀찮
@pytest.fixture
def driver():
    driver = driver_init()
    yield driver
    driver.quit()

# 로그 파일 경로 설정
log_file = os.path.join(os.getcwd(), "Test.log")

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file,
        filemode='a',
        encoding="utf-8"
    )
    logger = logging.getLogger(__name__)
    logger.info("✅ 테스트 시작 - 로그 설정 완료")
