
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils.base_driver import BaseDriver

class SeleniumWrapper(BaseDriver):

    def __init__(self, context):
        super().__init__(context)

    # to navigate to any url
    def visit(self, url):
        self.driver.get(url)

    # using css selector as default locator strategy
    def click(self, selector):
        if selector.startswith('//'):
            self.driver.find_element(By.XPATH, selector).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, selector).click()

    def type(self, selector, text):
        if selector.startswith('//'):
            self.driver.find_element(By.XPATH, selector).send_keys(text)
        else:
            self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(text)

    def get_text(self, selector):
        if selector.startswith('//'):
            return self.driver.find_element(By.XPATH, selector).get_attribute("textContent")
        else:
            # import pdb;pdb.set_trace()
            return self.driver.find_element(By.CSS_SELECTOR, selector).get_attribute("textContent")

    def assert_text(self, selector, expected):
        actual = self.get_text(selector)
        assert expected == actual, f"Element text is not as expected. Expected: '{expected}', Actual: '{actual}'"

