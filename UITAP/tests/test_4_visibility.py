from pages.base_page import BasePage
from pages.page_object4 import VisibilityPage


def test_visibility(browser):
    URL = 'http://uitestingplayground.com/visibility'

    base_page = BasePage(browser)
    base_page.load(URL)

    page_object = VisibilityPage(browser)
    page_object.press_hide_button()
    assert page_object.check_visibility()

