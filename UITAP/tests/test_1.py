import allure

from pages.base_page import BasePage
from pages.page_object import OnlinerPage


def test_accoradance(browser):
    URL = 'https://www.onliner.by/'

    base_page = BasePage(browser)
    base_page.load(URL)
    base_page.load("https://catalog.onliner.by/")

    elements_page = OnlinerPage(browser)
    first_part = elements_page.go_to_catalog_elemenent()


    with allure.step("Test3: scrollbars"):
        assert elements_page.find_price_through_search(first_part), f"It's possible to see one or more buttons"
