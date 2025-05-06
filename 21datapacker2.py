from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Buy Ticket')]").click()
driver.find_element(By.XPATH,"//input[@id='dob']").click()

#Selecting the month
Month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
Month.select_by_visible_text("Mar")

#Selecting a year
Year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
Year.select_by_visible_text("2023")

#Selecting a day
days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for day in days:
    if day.text=="22":
        day.click()
        break;
time.sleep(2)
 