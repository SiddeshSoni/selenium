from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

Drag = driver.find_element_by_id('draggable')
Drop = driver.find_element_by_id('droppable')
act = ActionChains(driver)

#act.drag_and_drop(Drag,Drop).perform()                  #Action Chains has an In-Build Method to perform Drag and Drop Operation

act.click_and_hold(Drag).move_to_element(Drop).release().perform()  #Action Chains has yet another way of doing the same using click and hold


time.sleep(5)

driver.quit()