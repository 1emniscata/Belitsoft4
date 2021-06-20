from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ClassAttributePage:

    def __init__(self, browser):
        self.browser = browser

    def check_button(self):
        xpath = "//button[contains(@class, ' btn-primary ')]"
        self.browser.find_element(By.XPATH, xpath).click()
        self.browser.switch_to.alert.accept()
        try:
            self.browser.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True