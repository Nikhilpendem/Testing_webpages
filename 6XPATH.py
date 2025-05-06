#defining some methods in the XPATH
#SELF,parents,etc..
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/")
driver.maximize_window()
#Self
company_name=driver.find_element(By.XPATH,"//a[contains(text(),'TD Power Systems')]/self::a").text
print(company_name)
time.sleep(2)
#Parent
pany_name=driver.find_element(By.XPATH,"//a[contains(text(),'TD Power Systems')]/parent::td").xt
print(pany_name)
#Child
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/child::td").t
print(text_msg)
#Ansecstor
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr").t
print(text_msg)
#Decendant
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/descendat::*")
print("Number of Descendants:",len(text_msg))
#Following
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/following::*")
print("Number of Following:",len(text_msg))
#Following-Sibling
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/following-sibling::*")
print("Number of Following:",len(text_msg))
#precedings
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/preceding::*")
print("Number of Preceding:",len(text_msg))
#preceding-sibling
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'TD Power Systems')]/ancestor::tr/preceding-sibling::*")
print("Number of Preceding-siblings:",len(text_msg))
driver.close()