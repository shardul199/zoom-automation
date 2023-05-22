import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the Zoom admin credentials and the ID to search for
admin_email = "sales-admin@criodo.com"
admin_password = "Crio@123"
search_id = "ping+mentor-6@criodo.com"

# Set the path to the Chrome WebDriver executable
webdriver_path = "path/to/chromedriver"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the Zoom login page
driver.get("https://zoom.us/signin")
time.sleep(5)
# Wait for the email field to be visible and enter the admin email
email_field = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "email"))
)
email_field.send_keys(admin_email)

# Enter the admin password and submit the form
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(admin_password)
password_field.submit()

# Wait for the user management system to load and navigate to it
user_management_link = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//a[@data-id='UserManagement']"))
)
user_management_link.click()

# Wait for the search input field to be visible and enter the search ID
search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchBar"))
)
search_input.send_keys(search_id)

# Click the search button
search_button = driver.find_element(By.ID, "searchBtn")
search_button.click()

# Wait for the search results to load and click the export button for the desired user
export_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, f"//button[@data-jid='{search_id}']"))
)
export_button.click()

# Wait for the export modal to open and click the export button
export_modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "export-user-modal"))
)
export_button = export_modal.find_element(By.XPATH, "//button[text()='Export']")
export_button.click()

# Wait for the export to finish and close the browser
WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(1))
driver.quit()


