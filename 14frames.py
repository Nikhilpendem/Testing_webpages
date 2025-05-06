#Frames divide the web page to different catogiries and these way we can access them
#switch_to.frame(name of the frame,id,webelement,index number) Selenium 4 syntax
#switch_to.defaut_content()
#switch_to_frame("")selenium 3 syntax
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
frame1=driver.find_element(By.XPATH,"/html")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//input[@name='mytext1']").send_key("Welcome")
driver.switch_to.default_content()
driver.switch_to.frame("//frameset//frameset//frame[1]")
driver.find_element(By.NAME,"mytext2").send_keys("Some")