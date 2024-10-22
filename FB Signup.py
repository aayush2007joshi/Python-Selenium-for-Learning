from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Facebook signup page
driver.get("https://www.facebook.com/r.php")
driver.maximize_window()
time.sleep(2)

# Fill in the signup form
first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Doe")

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("johndoe@example.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("your_secure_password")

# Select birthdate
driver.find_element(By.NAME, "birthday_day").send_keys("15")
driver.find_element(By.NAME, "birthday_month").send_keys("Mar")
driver.find_element(By.NAME, "birthday_year").send_keys("1990")

# Select gender
driver.find_element(By.XPATH, "//input[@value='2']").click()  # Female
# driver.find_element(By.XPATH, "//input[@value='1']").click()  # Male

# Click the signup button
driver.find_element(By.NAME, "websubmit").click()

# Wait for a while to observe the result (optional)
time.sleep(5)

input()