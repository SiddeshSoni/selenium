from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')





















driver.quit()