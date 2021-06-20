from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class ScrollbarsPage:

    def __init__(self, browser):
        self.browser = browser

    def scroll(self):
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5);')
        # time.sleep(5)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollWidth/1.5);')
        # time.sleep(5)

    def check_button_visibility(self):
        button_visabilty = self.browser.find_element(By.ID, "hidingButton").is_enabled()
        self.browser.find_element(By.ID, "hidingButton").click()
        return button_visabilty

