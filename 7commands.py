#Check the program before execution
#we have 5 commands 1)Application 2)conditional 3)browser 4)navigational 5)wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


##### implicit wait#######
#driver.implicitly_wait(10) 
#single statement
#Performance will not be reduced.(If the element is available within the time mentioned it proceed to execute further statements.)
#Dis ADV of implicit wait if the element is not available within the time mentioned there is a chance of getting the exception



#Explicit wait
#mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisisbleExecption,Exception])
#Simply using of Exception will not required in mention of other exceptions ,it will cover every exception
#we used this conditin at the last
driver.get("https://opensource-demo.orangehrmlive.com/")


#1)Application commends are used below
print(driver.title)
print(driver.current_url)
print(driver.page_source)


#2) Conditional commands are used below
searchbar=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
print("Status of searchbar : ",searchbar.is_displayed())
print("Status of searchbar : ",searchbar.is_enabled())
checkbox1=driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input'][normalize-space()='Admin']")
checkbox2=driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input'][normalize-space()='ESS']")
print("Status of checkbox1 : ",checkbox1.is_selected())
print("Status of checkbox2 : ",checkbox2.is_selected())
checkbox2.click()#Radio buttons are also used in same way u can check experimenting



#3)Browser commands are used below are close and quit functions
# close is used to close single window(Where driver focused)
#quit is used to close multiple windows(Kil the process)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()


#Navigational commands are used below back,forward and refresh
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")
driver.back()#snapdeal
driver.forward()#Amazon
driver.refresh()#Refresh the current page


#difference between find element and find elements
#find element returns single web element

#1) Locator matching with single webelement
element=driver.find_element("By.XPATH,//input[@id='small-searchterms']")
element.send_keys("apple macbook pro")

#2) locator matching with multiple webelements
element=driver.find_element("By.XPATH,//div[@class='footer']//a")
print(element.text)#prints first link from the footer

#3) element not available then throw NoSuchElementException
login_element=driver.find_element(By.LINK_TEXT,"Log")
login_element.click()


#Find elements locator

#1) Locator matching with single webelement
elements=driver.find_elements("By.XPATH,//input[@id='small-searchterms']")
print(len(elements))
elements[0].send_keys("apple macbook pro")

#2)Locator matching with multiple webelements
elements=driver.find_elements("By.XPATH,//div[@class='footer']//a")
print(len(elements))
print(elements[0].text)#returns first element that too in list
for ele in elements:
    print(ele.text)

#3)Element not available - zero
elements=driver.find_elements(By.LINK_TEXT,"Log")
print(len(elements))#returns zero


#text and get attribute('value')

#text -----> returns inner text of the element
#get attribute('value')----> returns value of the attribute of the element
#<input id="123" name="xyz">Email: </input>  -----> Email is inner text here
button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in]")
print("Results of text :",button.text)#prints Log in
print("Results of get_attribute :",button.get_attribute('value'))


#Wait commands used in solving of synchronisation issue
#synchronisation problem occur  is nothing but when the application we run is slow than the code we wrote 
#so we use wait commands to wait for the element to be visible or clickable or present on the screen
#we have two wait command 1)Implicit and 2)Explicit

#1)Implicit wait
#Implicit wait is used to define a time duration that the webdriver will wait before throwing a "NoSuch element is found"
searchbox=driver.find_element(By.NAME,'q')#google
searchbox.send_keys("selenium")
searchbox.submit()
time.sleep(2)
#Only 1 ADV for time.sleep is simple to use
#1)using time.sleep(time in seconds) reduces the performence of the script
#2)if the element is not recognised within the time mentioned,still there is chance of getting exception.
driver.find_element(By.XPATH,"//h3[text()='Selenium]").click()

#Using of Explicit wait
#ADV Works more effectively
#Dis ADV is 1)Need to use multiple times 2) feel some difficulty
#searchlink=mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='Selenium']"))
#searchlink.click()

driver.close()
