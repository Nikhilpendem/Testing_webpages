from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
outershell=driver.find_element(By.XPATH,"//body//section")
driver.switch_to.frame(outershell)
inner=driver.find_element(By.XPATH,"//div[@class='container']")
driver.switch_to.frame(inner)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
driver.switch_to.parent_frame()
