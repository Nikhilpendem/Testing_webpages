#Datepicker are two types 1)Standard 2)Non standard(customised)
#This example is for standard datepicker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


#Creating the frame 
#frame1=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
#driver.switch_to.frame(frame1)
driver.switch_to.frame(0)

#MM/DD/YY
#Approach 1
#driver.find_element(By.ID,"datepicker").send_keys("12/24/2024")
driver.find_element(By.ID,"datepicker").click()
# time.sleep(2)

Month="March"
date="22"
Year="2023"

#Approach2
while True:
    Mon=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[1]").text
    Yr=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[2]").text
    if Mon==Month and Yr==Year:
        break;
    else:
       # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  #Next arrow
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  #Back arrow

#Select date
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//tbody/tr/td/a")
# time.sleep(2)

for ele in dates:
    if ele.text==date:
        ele.click()
        break;
time.sleep(2)
    
        
    

