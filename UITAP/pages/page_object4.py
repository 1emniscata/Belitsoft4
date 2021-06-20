from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import InvalidSelectorException
# from selenium.common.exceptions import InvalidArgumentException
# from selenium.common.exceptions import ElementClickInterceptedException

class VisibilityPage:
    # LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    # SEARCH_INPUT = (By.ID, 'search_form_input')

# '/html/body/section/div/table/tbody/tr[1]/td[2]/button'

    # xpath = "//table[contains(*class='btn')]"
    BUTTONS =  (By.XPATH, xpath)
    HIDE = (By.ID, 'hideButton')
    OPACITY_0 = (By.ID, 'transparentButton')
    REMOVED = (By.ID, 'removedButton')
    VISIBILITY_HIDDEN = (By.ID, 'invisibleButton')
    ZERO_WIDTH = (By.ID, 'zeroWidthButton')
    DISPLAY_NONE = (By.ID, 'notdisplayedButton')
    OVERLAPPED = (By.ID, 'overlappedButton')
    OFFSCREEN = (By.ID, 'offscreenButton')
    BUTTONS_LIST = [HIDE, OPACITY_0, REMOVED, VISIBILITY_HIDDEN, ZERO_WIDTH, DISPLAY_NONE,
                    OVERLAPPED, OFFSCREEN]

    def __init__(self, browser):
        self.browser = browser

    def button_count(self):
        # buttons_elements = self.browser.find_elements(*self.BUTTONS_LIST)
        # return len(buttons_elements)
        return 8

    def press_hide_button(self):
        self.browser.find_element(*self.HIDE).click()

    def check_visibility(self):
        answers = {}
        for button in range(1, self.button_count()):
            try:
                answers[button] = self.browser.find_element(*self.BUTTONS_LIST[button]).is_displayed()
            except NoSuchElementException as err:
                answers[button] = False
        if True not in answers.items():
            return True
        return False





    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    # def __init__(self, browser):
    #     self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')