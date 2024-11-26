from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Sauce Labs Fleece Jacket").click()
time.sleep(2)
driver.find_element(By.ID,"add-to-cart").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(2)
driver.find_element(By.ID,"checkout").click()
time.sleep(2)
#form
driver.find_element(By.ID,"first-name").send_keys("Christian")
driver.find_element(By.ID,"last-name").send_keys("Grey")
driver.find_element(By.ID,"postal-code").send_keys("455001")
time.sleep(2)
driver.find_element(By.ID,"continue").click()
time.sleep(10)
driver.find_element(By.ID,"finish").click()
time.sleep(3)
driver.find_element(By.ID,"back-to-products").click()

input()
#driver.quit()
