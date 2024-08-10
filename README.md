# frameWorkSelenium
Selenium Hybrid Framework  (Python, Selenium, PyTest, Page Object Model, HTML Reports)

Selenium Hybrid Framework 

# Step 1: Create new Project & Install Required Packages/plugins

New Project => OpenCartFramework
Create new file requirements.txt (name should be the same as python needs to recognize)
And click install packages and check in python interpreter in setting to verify

# Step 2: Create Folder Structure

Directories - configurations, logs,reports,testdata,screenshots 
Python package - pageObjects, testCases, utilities

# Step 3: Automating Register account test case
## 3.1: Create page object classes for HomePage & AccountRegistration page under "pageObjects"
		HomePage.py					AccountRegistrationPage.py
from selenium.webdriver.common.by import By

class HomePage:
   #Locators
   link_myaccount_xpath = "//span[normalize-space()='My Account']"
   link_register_linkText = "Register"
   link_login_linkText = "Login"
   
   #constructor
   def __init__(self, driver):
       self.driver = driver

   #actions
   def clickMyAcc(self):
       self.driver.find_element(By.XPATH, self.link_myaccount_xpath).click()


   def clickRegister(self):
       self.driver.find_element(By.LINK_TEXT, self.link_register_linkText).click()


   def clickLogin(self):
       self.driver.find_element(By.LINK_TEXT, self.link_login_linkText).click()




from selenium.webdriver.common.by import By


class AccountRegistration:


   #Locators
   txtbox_fname_id = "input-firstname"
   txtbox_lname_id = "input-lastname"
   txtbox_email_id = "input-email"
   txtbox_passwd_id = "input-password"
   #toggle_subscribe_id = "input-newsletter"
   check_agree_name = "agree"
   btn_continue_xpath = "//button[normalize-space()='Continue']"
   txtMsg_confirm_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

   #constructor
   def __init__(self, driver):
       self.driver = driver
      
   #actions


   def setfirstname(self, fname):
       self.driver.find_element(By.ID, self.txtbox_fname_id).send_keys(fname)


   def setlastname(self, lname):
       self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lname)


   def setemail(self, email):
       self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)


   def setpassword(self, passwd):
       self.driver.find_element(By.ID, self.txtbox_passwd_id).send_keys(passwd)


   def setPrivacyPolicy(self):
       self.driver.find_element(By.NAME, self.check_agree_name).click()


   def clickCOntinue(self):
       self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()


   def getConfirmationMsg(self):
       try:
           return self.driver.find_element(By.XPATH, self.txtMsg_confirm_xpath).text
       except:
           None

3.2: Create conftest.py under "testCases" with driver manager.

conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture()
def setup():
   driver = webdriver.Chrome(ChromeDriverManager().install())
   return driver
Fixture (setup):
The setup() function is decorated with @pytest.fixture(), which makes it a fixture in pytest. Fixtures are used to set up necessary preconditions for your tests (in this case, initializing a WebDriver).
driver = webdriver.Chrome(ChromeDriverManager().install()):
This line installs the ChromeDriver (if not already installed) and creates a new instance of the Chrome browser.
The function returns the driver, making it available to any test that uses this fixture.
webdriver_manager.chrome.ChromeDriverManager: This is used to automatically manage and download the ChromeDriver executable, making sure that the appropriate version is used.




3.3: Create AccountRegistration testcase under "testCases"
from random import random


from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistration


class Test_001_AccountReg:
   baseURL = "https://demo.opencart.com/"


   def test_account_reg(self, setup):
       self.driver = setup
       self.driver.get(self.baseURL)
       self.driver.maximize_window()


       self.home = HomePage(self.driver)
       self.home.clickMyAcc()
       self.home.clickRegister()


 self.accReg = AccountRegistration(self.driver)
       self.accReg.setfirstname("Ramya")
       self.accReg.setlastname("S")
       # self.email = randomString.random_string_generator()+'@gmail.com'
       # self.accReg.setemail(self.email)
       self.accReg.setemail("ra@gmail.com")
       self.accReg.setpassword("123")
       self.accReg.setPrivacyPolicy()
       self.confMsg = self.accReg.getConfirmationMsg()
       self.driver.close()
       if self.confMsg == "Your Account Has Been Created!":
           assert True
       else:
           assert False

3.4 Write a utility file to generate random strings for email.


import random
import string




def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
   return ''.join(random.choice(chars) for x in range(size))






Parameters
size=5:
This is a keyword argument that specifies the length of the random string to be generated.
The default value is 5, so if no size is provided when calling the function, the generated string will be 5 characters long.
chars=string.ascii_lowercase + string.digits:
This is another keyword argument that defines the pool of characters from which the random string will be generated.
string.ascii_lowercase includes all lowercase letters ('abcdefghijklmnopqrstuvwxyz').
string.digits includes all decimal digits ('0123456789').
The expression string.ascii_lowercase + string.digits concatenates these two strings, resulting in a pool of characters that includes all lowercase letters and digits ('abcdefghijklmnopqrstuvwxyz0123456789').
If no chars argument is provided when calling the function, the function will use this combined string as the pool of characters.
How It Works
Random Character Selection:
random.choice(chars) is used to randomly select a single character from the chars pool.
String Construction:
The function uses a list comprehension inside the ''.join() method to generate a string.
''.join() concatenates the randomly chosen characters into a single string.
The list comprehension iterates size times (for x in range(size)), selecting a random character each time and forming a list of these characters.
The ''.join() method then combines this list of characters into a single string.
Step 4: capture screenshot on failures
4.1.  Update AccountRegistration Test case with capture Screenshot under "testCases"
class Test_001_AccountReg:
   baseURL = "https://demo.opencart.com/en-gb?route=account/register"


   def test_account_reg(self, setup):
       self.driver = setup
       self.driver.get(self.baseURL)
       self.driver.maximize_window()


       self.accReg = AccountRegistration(self.driver)
       self.accReg.setfirstname("Ramya")
       self.accReg.setlastname("S")
       self.email = randomString.random_string_generator()+'@gmail.com'
       self.accReg.setemail(self.email)
       # self.accReg.setemail("ra346@gmail.com")
       self.accReg.setpassword("123457jU")
       self.accReg.setPrivacyPolicy()
       self.accReg.clickCOntinue()
       self.confMsg = self.accReg.getConfirmationMsg()
       print(self.confMsg)
       time.sleep(5)
       if self.confMsg == "Your Account Has Been Created!":
           assert True
           self.driver.close()
       else:              self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_account_reg.png")
           self.driver.close()
           assert False





Step 5:  Read common values from ini file.
5.1: Add "config.ini" file in "configurations" folder.
config.ini
[commonInfo]
baseURL=https://demo.opencart.com/en-gb?route=account/register

5.2: Create "readProperties.py" utility file under utilities package to read common data.
import configparser
import os


config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")


class ReadConfig:


   @staticmethod
   def getApplicationURL():
       url = config.get('commonInfo', 'baseURL')
       return url

5.3: Replace hard coded values in AccountRegistration testcase
class Test_001_AccountReg:
   # baseURL = "https://demo.opencart.com/en-gb?route=account/register"
   baseURL = ReadConfig.getApplicationURL()

Step 6: Adding logs to test case
 6.1: Add customLogger.py under the utilities package.

 6.2: Add logs to AccountRegistration test case.
                 	
Step 7:  Run Tests on Desired Browser(Cross Browser Testing)/Parallel
 
      	7.1: update contest.py with required fixtures which will accept command line argument (browser).
7.2: Pass browser name as argument in command line
 
To Run tests on desired browser
pytest -s -v .\testCases\test_001_AccountRegistration.py --browser edge
 
To Run tests parallel
pytest -s -v -n=3 .\testCases\test_001_AccountRegistration.py --browser edge
 

