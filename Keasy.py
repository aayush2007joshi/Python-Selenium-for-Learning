from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bcforguy-437583-react.b437583.dev.eastus.az.svc.builder.cafe")
time.sleep(2)

# Login Start

driver.find_element(By.NAME, "email").send_keys("vendor@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Hello@1234")
driver.find_element(By.NAME, "rememberMe").click()
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/form/div/button").click()
time.sleep(3)
# Login complete

# Work Order start
driver.get("https://bcforguy-437583-react.b437583.dev.eastus.az.svc.builder.cafe/PortfolioManagement")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "new-property").click()

#driver.find_element(By.ID,"mui-44").click()


input()