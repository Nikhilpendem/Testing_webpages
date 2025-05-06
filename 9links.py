#links 1)Internal 2)external 3)broken
#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
time.sleep(2)

#click on the link
#driver.find_element(By.LINK_TEXT,"Download nopCommerce").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Download").click()


#find number of links on a webpage
#links=driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print("Number of links are:",len(links))

#Print all the links in webpage
for link in links:
    print(link.text)
time.sleep(2)


# driver.close()