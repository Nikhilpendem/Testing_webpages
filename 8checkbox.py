from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation" )
driver.maximize_window()
#1)select specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday]").click()

#2)select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

#approach1

for i in range(len(checkboxes)):
    checkboxes[i].click()

#approach2
for checkbox in checkboxes:
    checkbox.click()
    

#3) select multiple checkboxes by choices
for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday':
        checkbox.click()
        
        
#4) select last 2 checkboxes
#total number of elements -2
for i in range(len(checkboxes)-2),len(checkboxes):
    checkboxes[i].click()
    
#5)select first 2 checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
        
time.sleep(5)
#6)Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected:
        checkbox.click()
        
        
        

        

