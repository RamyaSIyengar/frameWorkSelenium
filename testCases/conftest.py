import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install())
    #
    # driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver
