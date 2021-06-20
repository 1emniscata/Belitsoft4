import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.page_object9 import HiddenLayersPage

def test_sample_app(browser):
    URL = 'http://uitestingplayground.com/hiddenlayers'

    base_page = BasePage(browser)
    base_page.load(URL)

    layers_page = HiddenLayersPage(browser)
    layers_page.press_button()
    assert layers_page.check_visibility()

    # assert sample_app_page.check_completion()