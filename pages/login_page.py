from utils.selenium_wrapper import SeleniumWrapper
from locators.locators import *
from utils.get_test_data import get_test_data

class LoginPage(SeleniumWrapper):

	def __init__(self, context):
		super().__init__(context)
		self.context = context
		self.testdata = get_test_data(context)

	def visit_login_page(self):
		self.driver.get(self.context['baseurl'])

	def login(self):
		self.assert_text(home_page['login_logo_text'], self.testdata["login_page_logo_text"])
		self.type(home_page['username_field'], self.context['login'])
		self.type(home_page['password_field'], self.context['secret'])
		self.click(home_page['login_btn'])
		self.assert_text(home_page['home_page_main_heading_txt'], self.testdata["home_page_logo_text"])
