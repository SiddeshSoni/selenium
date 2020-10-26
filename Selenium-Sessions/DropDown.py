from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

#this is the best method to use it multiple times:
def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

element_industry = driver.find_element_by_id('Form_submitForm_Industry')
element_country = driver.find_element_by_id('Form_submitForm_Country')

select_values(element_industry, 'Education')
select_values(element_country, 'India')
print(driver.title)




#this cab be used for doing it once or twice and not multiple times:

#select = Select(element_industry)

#select.select_by_visible_text('Education')

#select.select_by_index('4')

#select.select_by_value('health')

select = Select(element_industry)
allindus = select.options

for ele in allindus:
    print(ele.text)

