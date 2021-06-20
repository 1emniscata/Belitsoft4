from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import ElementClickInterceptedException

class ClassAttributePage:

    def __init__(self, browser):
        self.browser = browser

    def check_button(self):
        time.sleep(2)
        # class_name = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
        # xpath = "/html/body/section/div/button[2]"
        class_name = "//button[contains(@class, 'btn-primary')]"
        self.browser.find_element(By.CLASS_NAME, class_name).click()
        # self.browser.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        self.browser.switchTo().alert().accept()
        try:
            self.browser.find_element(By.CLASS_NAME, class_name)
        except NoSuchElementException as err:
            return False
        return True

    # "<button class="btn btn-primary btn-test">"
    #     "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]" ' '

    '/html/body/section/div/div/div[3]/div[2]/span[4]'
    '/html/body/section/div/div/div[3]/div[2]/span[4]'
    '/html/body/section/div/div/div[3]/div[3]/span[4]'
    '/html/body/section/div/div/div[3]/div[2]/span[2]'

    '/html/body/section/div/div/div[2]/div/span[2]'
    '/html/body/section/div/div/div[3]/div[2]/span[1]'
