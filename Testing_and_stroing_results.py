from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up ChromeDriver Service
serv_obj = Service("")
driver = webdriver.Chrome(service=serv_obj)

# Specify the path where the report will be saved
report_file_path = "D://Fullstack//test_report.txt"  # Update this path as needed

# Prepare the report file
with open(report_file_path, "w") as report_file:
    try:
        # Log start of the test
        report_file.write("Test started\n\n")
        
        # Open the page
        driver.get("https://www.saucedemo.com/v1/")
        driver.maximize_window()
        report_file.write("Opened the page: https://www.saucedemo.com/v1/\n")
        
        # Login Test
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Wait for login to complete
        report_file.write("Login Test: Passed\n")

        # Add item to cart
        driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button").click()
        report_file.write("Item added to cart: Passed\n")

        # Go to cart
        driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").click()
        report_file.write("Navigated to cart: Passed\n")

        # Proceed to checkout
        driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]").click()
        report_file.write("Proceeded to checkout: Passed\n")

        # Cancel the checkout
        driver.find_element(By.LINK_TEXT, "CANCEL").click()
        report_file.write("Checkout canceled: Passed\n")

        # Remove item from cart
        driver.find_element(By.XPATH, "//button[normalize-space()='REMOVE']").click()
        report_file.write("Item removed from cart: Passed\n")

        # End of test
        report_file.write("\nTest completed successfully\n")
    
    except Exception as e:
        # Log any exceptions that occurred during the test
        report_file.write(f"Test Failed: {str(e)}\n")
    finally:
        driver.quit()

print("Test report saved as test_report.txt")
