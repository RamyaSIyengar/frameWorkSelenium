import time
import os
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistration
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen  # for logging





class Test_001_AccountReg:
    # baseURL = "https://demo.opencart.com/en-gb?route=account/register"
    baseURL = ReadConfig.getApplicationURL() + "/en-gb?route=account/register"
    logger = LogGen.loggen()  # for logging
    print(logger)

    def test_account_reg(self, setup):
        self.logger.info("***Test_001_AccountRegistration started***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("***Launching Application***")
        self.driver.maximize_window()

        # self.home = HomePage(self.driver)
        # self.home.clickMyAcc()
        # self.home.clickRegister()

        self.accReg = AccountRegistration(self.driver)
        self.logger.info("***Providing required information to register***")
        self.accReg.setfirstname("Ramya")
        # self.accReg.setlastname("S")
        # self.email = randomString.random_string_generator()+'@gmail.com'
        # self.accReg.setemail(self.email)
        # # self.accReg.setemail("ra346@gmail.com")
        # self.accReg.setpassword("123457jU")
        # self.accReg.setPrivacyPolicy()
        # self.accReg.clickCOntinue()
        # self.confMsg = self.accReg.getConfirmationMsg()
        # print(self.confMsg)
        # time.sleep(5)
        # if self.confMsg == "Your Account Has Been Created!":
        #     self.logger.info("***Account registration passed***")
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_account_reg.png")
        #     self.logger.info("***Account registration failed***")
        #
        #     self.driver.close()
        #     assert False
        #
        # self.logger.info("***Test_001_AccountRegistration finished***")
        #
        #

