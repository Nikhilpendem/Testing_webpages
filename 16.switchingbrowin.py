#switch_to.window(windowid)
#current_window_handle #Return windowId of single browser window
#window_handles       #Return window ID's of multiple browser windows
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
#Approach2
WindowIds=driver.window_handles
parentId=WindowIds[0]
childId=WindowIds[1]

driver.switch_to.window(childId)
print(driver.title)

driver.switch_to.window(parentId)
print(parentId)
for wind in WindowIds:
    driver.switch_to.window(wind)
    print(driver.title )