from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def select_values(Optionlist,value):
    if not value[0] == 'all':

        for ele in drop_down_list:                  #for more than two element selection
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        for ele in drop_down_list:                 #for all element selection
            ele.click()
    #if ele.text == value:                         #for only one element selection
                #ele.click()
                #break

driver = webdriver.Chrome(ChromeDriverManager().install())


#note : There is no select tag available in this page.

driver.implicitly_wait(10)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

multi_select = driver.find_element_by_id("justAnInputBox").click()

time.sleep(3)

drop_down_list = driver.find_elements_by_css_selector('span.comboTreeItemTitle')

#values_list = ['choice 2','choice 3','choice 6 2 1']             #To select the particular choice
value_list = ['all']                                              #To select all the choices
select_values(drop_down_list,value_list)                          #Function call





#select_values(drop_down_list, 'choice 3')                        #If we want to select a particular choice in the list
#select_values(drop_down_list, 'choice 6 2 1')                    #Same as above











driver.implicitly_wait(5)









driver.quit()