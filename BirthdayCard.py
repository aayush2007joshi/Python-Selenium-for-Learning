from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mewtru.com/")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/main/div[2]/a[1]/img").click()
time.sleep(2)

#form
driver.find_element(By.NAME,"name").send_keys("Isha")
time.sleep(2)
driver.find_element(By.NAME,"age").send_keys("26")
time.sleep(2)
driver.find_element(By.NAME,"message").send_keys("Happiest Birthday Isha !!")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "mt-4").click()
time.sleep(10)
driver.find_element(By.CLASS_NAME, "p-6").click()
input()
