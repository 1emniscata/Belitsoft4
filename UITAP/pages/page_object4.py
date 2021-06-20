from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class VisibilityPage:

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
        return len(self.BUTTONS_LIST)

    def press_hide_button(self):
        self.browser.find_element(*self.HIDE).click()

    def check_visibility(self):
        answers = {}
        for button in range(1, self.button_count()):
            try:
                answers[button] = self.browser.find_element(*self.BUTTONS_LIST[button]).is_displayed()
            except NoSuchElementException:
                answers[button] = False
        if True not in answers.items():
            return True
        return False

