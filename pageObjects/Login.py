from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:

    # Locators
    txtbox_email_id = "input-email"
    txtbox_passwd_id = "input-password"
    button_login_xpath = "//button[normalize-space()='Login']"
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setPasswd(self, passwd):
        self.driver.find_element(By.ID, self.txtbox_passwd_id).send_keys(passwd)

    def clickLogin(self, reties=3):
        for i in range(reties):
            self.button = (WebDriverWait(self.driver, 10)
                           .until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))))
            # Scroll to the element
            self.driver.execute_script("arguments[0].scrollIntoView();", self.button)

            # Optionally, you can add a sleep to see the scroll action
            self.button.click()

    def clickLogin(self, retries=3):
        # Wait until the button is clickable
        self.button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        self.button.click()



    def isMyAccVisible(self):
        try:
            # Wait until the element is visible
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.msg_myaccount_xpath))
            )
            return element.is_displayed()
        except (NoSuchElementException, StaleElementReferenceException):
            return False



