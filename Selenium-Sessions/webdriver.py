from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)

driver.find_element_by_name('q').send_keys("naveen_automationlabs")
optionList = driver.find_elements_by_css_selector('ul.erkvQe li span')
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break


time.sleep(5)
driver.quit()