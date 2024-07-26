import pytest
import logging
from utils.get_env_details import get_env_details
from pages.home_page import HomePage
from pages.login_page import LoginPage
from time import sleep

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

'''This is a boiler place test script, we can use this script to replicate other test script files'''


@pytest.fixture(scope="session")
def global_setup(request):

    logger.info("Global Setup section")

    '''context will contain all env variables & env specific data stored in configs/env_data'''
    context = get_env_details(request)

    '''create an object of HomePage class & add it in context so that it can be shared within test cases'''
    homepage = HomePage(context)
    loginpage = LoginPage(context)

    context['homepage'] = homepage
    context['loginpage'] = loginpage

    yield context

    logger.info("Global Teardown section")
    homepage.close_browser()


# Test-specific setup and teardown (function scope)
@pytest.fixture()
def test_setup():
    logger.info("\nTest Setup section")
    yield
    logger.info("\nTest Teardown section")


def test_login_and_verify_product_homepage(global_setup, test_setup):
    ''' IMPORTANT, test case name must start with "test" '''

    '''home page object was initialized in global_setup() fixture and the reference 
    is passed as global setup
    which is the first argument to this test case method
    '''
    homepage = global_setup['homepage']
    loginpage = global_setup['loginpage']

    '''will visit the home page as per env, baseurl would be taken from configs/env_data'''
    loginpage.visit_login_page()
    loginpage.login()

    '''will login and check few basic assertions on the page'''
    homepage.verify_home_page()

    '''sleep is added just so you can see the browser a bit more'''
    sleep(2)
