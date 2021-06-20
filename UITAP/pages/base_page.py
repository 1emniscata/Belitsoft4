class BasePage:

  def __init__(self, browser):
    self.browser = browser

  def load(self, url):
    self.browser.get(url)
