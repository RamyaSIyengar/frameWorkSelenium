import os.path
import time

from pageObjects.Login import LoginPage
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig


class Test_Login:
        # you cant directly read url from config.ini => through utility->readproperty
        baseURL = ReadConfig.getApplicationURL() + "/en-gb?route=account/login"

        logger = LogGen.loggen()  # to log messages
        email = ReadConfig.getEmail()
        password = ReadConfig.getpasswd()

        def test_login(self, setup):
            self.logger.info("*** Test_002_Login Started***")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.loginn = LoginPage(self.driver)
            self.loginn.setEmail(self.email)
            self.loginn.setPasswd(self.password)
            self.loginn.clickLogin()
            time.sleep(3)
            self.targetPage = self.loginn.isMyAccVisible()
            print(self.targetPage)
            if self.targetPage:
                self.logger.info("*** Test_002_Login Passed***")
                assert True

            else:
                self.driver.save_screenshot(filename=os.path.abspath(os.curdir)+"//screenshots//"+"login.png")
                self.logger.info("*** Test_002_Login Failed***")

                assert False


            self.driver.close()
            self.logger.info("*** Test_002_Login Finished***")


