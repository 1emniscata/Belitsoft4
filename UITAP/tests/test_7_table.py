from pages.base_page import BasePage
from pages.page_object7 import TablePage


def test_sample_app(browser):
    URL = 'http://uitestingplayground.com/dynamictable'

    base_page = BasePage(browser)
    base_page.load(URL)

    sample_app_page = TablePage(browser)
    assert sample_app_page.find_div_number() == sample_app_page.chrome_cpu()