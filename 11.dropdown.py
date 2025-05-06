from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.opencart.com/")
driver.maximize_window()
time.sleep(2)
#drpcountry=driver.find_element(By.XPATH,"//*[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))


#select option for the dropdown
#drpcountry.select_by_visible_text("India")# Mostly we use this method
#drpcountry.select_by_value("10")
#drpcountry.select_by_index(13)  #Index

#Capture all the options and print them
alloptions=drpcountry.options
print("Total no. of options",len(alloptions))

for opt in alloptions:
    print(opt.text)
    
#Select option from the dropdown without using built in method
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break
    
#If select option not there use this  method   
alloptions=driver.find_element(By.XPATH,"//*[@id='input-coutry']/option")
print(len(alloptions))