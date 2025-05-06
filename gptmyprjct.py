from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver Service
serv_obj = Service("path/to/your/chromedriver")  # Specify path if needed
driver = webdriver.Chrome(service=serv_obj)

try:
    # Open the page
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()

    # Implicit wait
    driver.implicitly_wait(10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add item to cart
    driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button").click()

    # Go to cart
    driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").click()

    # Proceed to checkout
    driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]").click()

    # Cancel the checkout
    driver.find_element(By.LINK_TEXT, "CANCEL").click()

    # Remove item from cart
    driver.find_element(By.XPATH, "//button[normalize-space()='REMOVE']").click()

    # Wait for the item to be removed and confirm removal (optional)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[normalize-space()='REMOVE']"))
    )
    print("Item removed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
