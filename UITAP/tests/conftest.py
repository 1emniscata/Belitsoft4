import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
  # options = ChromeOptions()
  # options.add_argument("--start-maximized")
  driver = Chrome()
  driver.maximize_window()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()