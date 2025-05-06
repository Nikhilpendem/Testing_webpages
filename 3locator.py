#Two type of locatores
#1.Locators 2.Customized Locators
#1.Locators{Classname,Name,Id,Partiallinktext/Linktext,tagname}
#2.Customized Locators{1.CSS selectors,2.XPATH}
#1.CSS{a.Tag and Id,b.Tag and Class,c.Tag and attribute,d.Tag,class and attribute}
#2.XPATH{a.Absolute XPATH,b.Relative XPATH}
#Dont run need some modofications go and check before execution
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop ")
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
#driver.find_element(By.CLASS_NAME,"search-box-button").click()
time.sleep(2)
slider=driver.find_elements(By.CLASS_NAME,"")
print(len(slider))
Tags=driver.find_elements(By.TAG_NAME,"a")
print(len(Tags))
#driver.quit()
driver.close()




