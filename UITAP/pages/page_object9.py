from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HiddenLayersPage:

    def __init__(self, browser):
        self.browser = browser

    def press_button(self):
        green_button = self.browser.find_element(By.ID, 'greenButton').click()
        blue_button = self.browser.find_element(By.ID, 'blueButton').click()

    def check_visibility(self):
        div_style = self.browser.find_elements(By.CLASS_NAME, "spa-view")
        return div_style[1].get_attribute('style') == "z-index: 2;"

