import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class HomePage:
    # Locators
    link_myaccount_xpath = "//li[@class='list-inline-item'][2]"
    link_wishlist_xpath = "//span[normalize-space()='Wish List (0)']"
    link_register_linkText = "Register"
    # link_register_xpath = "(//div[@class='dropdown'])[2]/ul/li[1]"
    link_login_linkText = "Login"

    # constructor
    def __init__(self, driver):
        self.driver = driver

        self.myWait = WebDriverWait(self.driver, 10, ignored_exceptions=[NoSuchElementException, TimeoutException]
                               ,poll_frequency=2)

    # actions
    def clickMyAcc(self):
        element =WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_wishlist_xpath)))




    def clickRegister(self):
        register_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.link_register_linkText))
        )
        print(register_element.text)
        register_element.click()



    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linkText).click()

