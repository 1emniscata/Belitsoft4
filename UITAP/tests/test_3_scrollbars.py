import time

import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.page_object3 import ScrollbarsPage

def test_sample_app(browser):
    URL = 'http://uitestingplayground.com/scrollbars'

    base_page = BasePage(browser)
    base_page.load(URL)

    layers_page = ScrollbarsPage(browser)
    layers_page.scroll()
    # time.sleep(4)
    assert layers_page.check_button_visibility()


    # assert sample_app_page.check_completion()