from pages.base_page import BasePage
from pages.page_object8 import SampleAppPage


def test_sample_app(browser):
    URL = 'http://uitestingplayground.com/sampleapp'

    base_page = BasePage(browser)
    base_page.load(URL)

    sample_app_page = SampleAppPage(browser)
    sample_app_page.input_login()
    sample_app_page.input_password()
    sample_app_page.press_button()
    assert sample_app_page.check_completion()