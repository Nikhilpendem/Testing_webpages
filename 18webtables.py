from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# ops=webdriver.ChromeOptions
# ops.add_argument("--disable-notifications")
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1)Count number of rows and columns

noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print("Number of rows :",noOfRows)
print("Number of columns",noOfColumns)

#2)Read specific data
print("Reading specific data")

data=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
#print(data)

#3)Read all the rows and columns data
print("Printing all the rows and columns data......")

for r in range(2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        data=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="      ")
    print(data)
    
    
#4)Read data based on condition(List Books name whose author is Mukesh)
for r in range(2,noOfRows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["  +str(r)+  "]/td[1]").text
        Price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["  +str(r)+  "]/td[4]").text
        print(bookname,"         ",authorName,"            ",Price)

driver.close()