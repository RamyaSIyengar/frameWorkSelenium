import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def pytest_addoption(parser):  # Hook - this will get the valur from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup
    return request.config.getoption("--browser")


# ----- pytest Html Report  --------

# it is a hook for adding Environment.info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'Registration'
    config._metadata['Tester'] = 'Ramya'


# It is a hook for delete/modify environment info in HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.abspath(os.curdir) + "//reports//" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                              + ".html")



"""
1.Hook Function: pytest_addoption
pytest_addoption(parser) is a hook function that allows you to add custom command-line options to pytest.
In this case, the --browser option is added, which can be used to specify the browser you want to test
 with (e.g., Chrome, Firefox).
 
2.Fixture: browser(request)
The browser fixture retrieves the value of the --browser command-line option 
using request.config.getoption("--browser").
This fixture can then be used in your test setup or test cases to get the
specified browser type.

"""

# driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install())
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install())
