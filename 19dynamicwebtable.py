from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-input--active").send_keys("admin123")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-button--medium").click()
time.sleep(2)
#Frame1=driver.find_element(By.XPATH,"//nav[@aria-label='Sidepanel']")
#driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]").click()
#driver.switch_to.default_content()
#frame2=driver.find_element(By.XPATH,"//div[@class='oxd-layout-context']")
#driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
time.sleep(2)
rows=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print("Total number of rows : ",rows)

for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status=="enabled":
        count=count+1
print("Total Number of users:",rows)
print("Number of enabled users:",count)
print("Number of disabled users:",(rows-count))
driver.close()