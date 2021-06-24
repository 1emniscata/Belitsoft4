from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


from selenium.webdriver.common.keys import Keys


class OnlinerPage:

    def __init__(self, browser):
        self.browser = browser

    def go_to_catalog_elemenent(self):
        catalog_element = self.browser.find_element(By.CSS_SELECTOR, "[data-id='2']")
        catalog_element.click()

        notebooks_section_xpath = "/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[2]/" \
                                  "div[1]/div/div[1]/div[1]"
        notebooks_section = self.browser.find_element(By.XPATH, notebooks_section_xpath)
        hover = ActionChains(self.browser).move_to_element(notebooks_section)
        hover.perform()

        link_to_notebooks_xpath = '/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/' \
                                  'div/div[1]/div[2]/div/a[1]'
        link_to_notebooks = self.browser.find_element(By.XPATH, link_to_notebooks_xpath).click()


        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight/2);')

        self.browser.execute_script('window.scrollTo(document.body.scrollHeight/2,document.body.scrollHeight);')


       #ADD FUNCTIONALITY FOR USING DIFFERENT PRODUCTS
        random_laptop = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/"
                         "div[1]/div[4]/div[3]/div[4]/div[7]/div/div[3]/div[2]/div[1]/a").get_attribute('href')
        self.browser.get(random_laptop)

        price_xpath = "/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/div[1]/" \
                      "div[2]/div[5]/div[1]/div/a"
        price = self.browser.find_element(By.XPATH, price_xpath).text

        laptop_title_xpath = "/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[4]/h1"
        laptop_title = self.browser.find_element(By.XPATH, laptop_title_xpath).text
        return [laptop_title, price]


    def find_price_through_search(self, func):
        search_field = self.browser.find_element(By.CLASS_NAME, "fast-search__input")
        search_field.send_keys(func[0])
        search_field.send_keys(Keys.ENTER)

        wait(self.browser, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.browser.find_element_by_xpath("//iframe[@class='modal-iframe']")))

        search_price_xpath = "/html/body/div[1]/div[2]/ul/li/div/div/div[1]/div/div[1]/a/span"
        search_price = self.browser.find_element(By.XPATH, search_price_xpath).text
        return search_price == func[1]





