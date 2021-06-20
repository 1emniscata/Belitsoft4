from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.common.exceptions import NoSuchElementException


class DelayPage:

    def __init__(self, browser):
        self.browser = browser

    def press_button(self):
        self.browser.find_element(By.ID, "ajaxButton").click()

    def wait_for_text(self):
        wait = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))
        message = self.browser.find_element(By.CLASS_NAME, "bg-success").text
        return message == "Data calculated on the client side."

