from selenium.webdriver.common.by import By


class SampleAppPage:

    def __init__(self, browser):
        self.browser = browser

    def input_login(self):
        login_field = self.browser.find_element(By.NAME, 'UserName')
        login_field.click()
        login_field.send_keys('Alex')

    def input_password(self):
        password_field = self.browser.find_element(By.NAME, 'Password')
        password_field.click()
        password_field.send_keys('pwd')

    def press_button(self):
        login_button = self.browser.find_element(By.ID, 'login').click()

    def check_completion(self):
        successful_message = self.browser.find_element(By.ID, 'loginstatus').text
        return successful_message[:8] == 'Welcome,'
