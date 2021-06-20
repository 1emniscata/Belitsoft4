from pages.base_page import BasePage
from pages.page_object5 import ClassAttributePage


def test_button(browser):
    URL = 'http://uitestingplayground.com/classattr'

    base_page = BasePage(browser)
    base_page.load(URL)

    class_attribute_page = ClassAttributePage(browser)
    assert class_attribute_page.check_button()