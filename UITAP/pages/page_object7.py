from selenium.webdriver.common.by import By


class TablePage:

    def __init__(self, browser):
        self.browser = browser

    def find_div_number(self):
        div_number = 0
        for i in range(1, 5):
            consumer = self.browser.find_element(By.XPATH, f'/html/body/section/div/div/'
                                                           f'div[3]/div[{i}]/span[1]').text
            if consumer == 'Chrome':
                div_number = i
                break

        for i in range(1, 5):
            value = self.browser.find_element(By.XPATH, f'/html/body/section/div/'
                                                        f'div/div[3]/div[{div_number}]/span[{i}]').text
            if value[-1] == '%':
                return value

    def chrome_cpu(self):
        indeed_value = self.browser.find_element(By.CLASS_NAME, 'bg-warning').text[-4:]
        return indeed_value




