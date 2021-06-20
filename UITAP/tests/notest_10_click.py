import pytest
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.page_object10 import ClickPage

def test_sample_app(browser):
    URL = 'http://uitestingplayground.com/click'

    base_page = BasePage(browser)
    base_page.load(URL)

    layers_page = ClickPage(browser)
    layers_page.press_button()
    # time.sleep(2)
    assert layers_page.check_clickability()

    # assert sample_app_page.check_completion()