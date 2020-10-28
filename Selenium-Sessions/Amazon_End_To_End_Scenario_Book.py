from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)
time.sleep(1)

driver.get('http://www.amazon.in')
time.sleep(3)

firstLevelMenu = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)

secondLevelMenu = driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

SignIn_ele = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
SignIn_ele.send_keys('8104661943')
time.sleep(3)

cont = driver.find_element(By.XPATH, '//*[@id="continue"]')
cont.click()
time.sleep(3)

Password_ele = driver.find_element_by_xpath('//*[@id="ap_password"]')
Password_ele.send_keys("Suitsbreaking@19")
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)


Search_Button = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
Search_Button.send_keys('Software Automation Testing Tools for Beginners')
time.sleep(1)

Find_Button = driver.find_element(By.XPATH, '//*[@id="nav-search"]/form/div[3]/div')
Find_Button.click()
time.sleep(1)

My_book = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div/h2/a/span')
My_book.click()
time.sleep(1)


driver.switch_to.window(driver.window_handles[1])

Buy_now = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
Buy_now.click()
time.sleep(1)

Account_final = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
action.move_to_element(Account_final).perform()
time.sleep(1)

logout = driver.find_element(By.XPATH, '//*[@id="nav-item-signout"]/span')
logout.click()

driver.quit()