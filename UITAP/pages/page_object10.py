from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ClickPage:

    def __init__(self, browser):
        self.browser = browser

    def press_button(self):
        blue_button = self.browser.find_element(By.ID, 'badButton').click()


    def check_clickability(self):
        self.browser.find_element(By.ID, 'badButton').click()
        return True
