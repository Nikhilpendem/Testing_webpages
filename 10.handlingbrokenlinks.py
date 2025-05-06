#Broken links doesnot contain any data or resorces for that links
#These are mentioned from >=400
#The less than that value are normal links
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as re
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
      res=re.head(url)
    except:
        None
        
    if res.status_code>=400:
        print(url,"is a broken link")
        count+=1
    else:
        print(url,"is valid link")
print("Total number of broken links",count)
        