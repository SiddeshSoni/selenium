from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

click_ele = driver.find_element(By.XPATH, "//span[text() ='right click me']")
act = ActionChains(driver)

act.context_click(click_ele).perform()

right_click_opt = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')

for ele in right_click_opt:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break
