import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type")
    parser.addoption("--env", action="store", default="QA", help="Environment")
    parser.addoption("--login", action="store", default="standard_user", help="Username")
    parser.addoption("--secret", action="store", default="secret_sauce", help="Password")
    parser.addoption("--headless", action="store", default="false", help="true|false")
    parser.addoption("--testdata", action="store", default="testdata/example_test_data.json", help="Pass data file")
