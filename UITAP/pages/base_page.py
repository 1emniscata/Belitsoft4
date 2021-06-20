from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
  # URL = 'http://uitestingplayground.com/'

  # SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

  def __init__(self, browser):
    self.browser = browser

  def load(self, url):
    self.browser.get(url)

  # def search(self, phrase):
  #   search_input = self.browser.find_element(*self.SEARCH_INPUT)
  #   search_input.send_keys(phrase + Keys.RETURN)

  # def go_to_link(self, url):
  #     self.browser.get(url)