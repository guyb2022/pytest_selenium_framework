from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser == 'firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):
    # get the value from the cli/ hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    # return the Browser value to setup method
    return request.config.getoption("--browser")

############# pytest html reports ###################
def pytest_configure(config):
    config._metadata['Project Name'] = 'Intel Workday'
    config._metadata['Module Name'] = 'Users'
    config._metadata['Tester'] = 'G.B Tester'

@pytest.mark.optionalhook
def pytest_metatada(metadata):
    pass
    # metadata.pop("somthing", None)
####################################################
