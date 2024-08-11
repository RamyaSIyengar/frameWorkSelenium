import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountRegistration:

    # Locators
    txtbox_fname_id = "input-firstname"
    txtbox_lname_id = "input-lastname"
    txtbox_email_id = "input-email"
    txtbox_passwd_id = "input-password"
    # toggle_subscribe_id = "input-newsletter"
    check_agree_name = "agree"
    button_continue_xpath = "//button[normalize-space()='Continue']"

    txtMsg_confirm_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    # constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # actions
    def setfirstname(self, fname):
        fnamebox = self.wait.until(EC.presence_of_element_located((By.ID, self.txtbox_fname_id)))
        fnamebox.send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lname)

    def setemail(self, email):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setpassword(self, passwd):
        self.driver.find_element(By.ID, self.txtbox_passwd_id).send_keys(passwd)

    def setPrivacyPolicy(self, retries=3):
        # self.driver.find_element(By.NAME, self.check_agree_name).click()
        for i in range(retries):
            try:
                self.driver.find_element(By.NAME, self.check_agree_name).click()
                return
            except ElementClickInterceptedException:
                time.sleep(1)

    def clickCOntinue(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_continue_xpath))
        )
        button.click()

    def getConfirmationMsg(self):
        try:
            confirm = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtMsg_confirm_xpath)))
            print(confirm.text)
            return confirm.text
        except:
            None









