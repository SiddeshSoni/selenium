from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
elif browserName == "opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    print("Please pass the corect browser name:"+browserName)

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element_by_id('username').send_keys("sonisiddesh@gmail.com")
driver.find_element_by_id('password').send_keys("Test@123")
driver.find_element_by_id('loginBtn').click()

print(driver.title)

time.sleep(4)
driver.quit()