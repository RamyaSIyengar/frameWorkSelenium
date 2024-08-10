from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import sys
print(sys.path)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
print(driver.title)
driver.quit()

