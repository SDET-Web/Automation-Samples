from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Simple Selenium test for login functionality

driver = webdriver.Chrome()  # make sure chromedriver is installed
driver.get("https://example.com/login")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("testuser")
password.send_keys("password123")
password.send_keys(Keys.RETURN)

assert "Dashboard" in driver.title

driver.quit()
