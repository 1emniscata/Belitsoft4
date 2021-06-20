import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.page_object4 import VisibilityPage

# from pages.result import DuckDuckGoResultPage
# from pages.search import DuckDuckGoSearchPage


# def test_basic_duckduckgo_search(browser):
#     PHRASE = 'panda'
#
#     search_page = DuckDuckGoSearchPage(browser)
#     search_page.load()
#     search_page.search(PHRASE)
#
#     result_page = DuckDuckGoResultPage(browser)
#     assert result_page.link_div_count() > 0
#     assert result_page.phrase_result_count(PHRASE) > 0
#     assert result_page.search_input_value() == PHRASE


def test_visibility(browser):
    URL = 'http://uitestingplayground.com/visibility'

    base_page = BasePage(browser)
    base_page.load(URL)

    page_object = VisibilityPage(browser)
    page_object.press_hide_button()
    assert page_object.check_visibility()


    # search_page.search(PHRASE)

    # result_page = DuckDuckGoResultPage(browser)
    # assert result_page.link_div_count() > 0
    # assert result_page.phrase_result_count(PHRASE) > 0
    # assert result_page.search_input_value() == PHRASE