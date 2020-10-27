from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME, 'proceed').click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()                                             #To accept the alert
#alert.dismiss()                                            #To directly dismiss the alert

time.sleep(3)
driver.quit()