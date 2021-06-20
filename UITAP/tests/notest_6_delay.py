import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.page_object6 import DelayPage


def test_button(browser):
    URL = 'http://uitestingplayground.com/clientdelay'

    base_page = BasePage(browser)
    base_page.load(URL)

    delay_page = DelayPage(browser)
    delay_page.press_button()
    assert delay_page.wait_for_text()