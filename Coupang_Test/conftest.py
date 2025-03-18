import pytest
from coupang_main import driver_init


# 테스트 할때마다 이거 적기 귀찮
@pytest.fixture
def driver():
    driver = driver_init()
    yield driver
    driver.quit()
