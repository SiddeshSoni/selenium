from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element_by_id('Form_submitForm_subdomain').send_keys("naveenautomationlabs")
first_name = driver.find_element_by_id('Form_submitForm_FirstName').send_keys("Naveen")
last_name = driver.find_element_by_id('Form_submitForm_LastName').send_keys("automationlabs")
email_id = driver.find_element_by_id('Form_submitForm_Email').send_keys("naveen@gmail.com")

feature_link = driver.find_element_by_link_text('Features').click()

time.sleep(3)
driver.quit()