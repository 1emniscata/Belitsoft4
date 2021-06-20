from selenium.webdriver.common.by import By


class ScrollbarsPage:

    def __init__(self, browser):
        self.browser = browser

    def scroll(self):
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # time.sleep(5)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollWidth);')
        # time.sleep(5)

    def check_button_visibility(self):
        button_visibilty = self.browser.find_element(By.ID, "hidingButton").is_enabled()
        self.browser.find_element(By.ID, "hidingButton").click()
        return button_visibilty

