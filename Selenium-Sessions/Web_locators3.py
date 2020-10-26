from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")

print(driver.title)

first = driver.find_element_by_xpath("//input[@id='username']")
second = driver.find_element_by_xpath("//input[@id='password']")
third = driver.find_element_by_class_name('login-submit')
fourth = driver.find_element_by_link_text('Sign up')

first.send_keys("sonsiddesh@gmail.com")
second.send_keys("Test@12345")
third.click()
fourth.click()

print("this is the git")