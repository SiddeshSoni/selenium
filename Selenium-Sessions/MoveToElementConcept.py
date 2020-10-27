from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.spicejet.com/')
time.sleep(3)

login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')

act_chains = ActionChains(driver)                          #To perform action we need to use ActionChains class

act_chains.move_to_element(login_ele).perform()            #.perform() method is imp to make sure the action is performed


spice_club_member = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')

act_chains.move_to_element(spice_club_member).perform()


member_login_ele = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login_ele.click()

time.sleep(5)
