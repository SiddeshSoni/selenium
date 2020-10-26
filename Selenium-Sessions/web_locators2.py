from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(5)
driver.get("https://classic.crmpro.com/")

first = driver.find_element(By.NAME, 'username')
second = driver.find_element(By.NAME, 'password')
third = driver.find_element_by_xpath("//input[@value='Login']")

first.send_keys("batchautomation")
second.send_keys("Test@12345")
third.click()

