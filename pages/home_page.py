from utils.selenium_wrapper import SeleniumWrapper
from locators.locators import *
from utils.get_test_data import get_test_data


class HomePage(SeleniumWrapper):

    def __init__(self, context):
        super().__init__(context)
        self.context = context
        self.testdata = get_test_data(context)

    def verify_home_page(self):
        self.assert_text(
            home_page['home_page_main_heading_txt'], self.testdata["home_page_logo_text"])
