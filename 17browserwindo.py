from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ops=webdriver.ChromeOptions
ops.add_argument("--disable-notifications")
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()