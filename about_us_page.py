from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

# Chrome Driver Path 
chrome_driver_path = Service("D:\Software\chromedriver_win32\chromedriver.exe")



# Project URL
about_us_page_url = "https://dev.rlogical.com/fullstackdevteams.com/about-us"

# chrome driver executable path
driver = webdriver.Chrome(service=chrome_driver_path)

# maximize window
driver.maximize_window()

# Current page of title
print("Current Page title: " + driver.title)

# get project url
driver.get(about_us_page_url)

# Current page of title
print("Current Page title: " + driver.title)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# our_vision
our_vision = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-history"))).click()
time.sleep(1)

# our_values
our_values = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-business"))).click()
time.sleep(1)

# our_approach
our_approach = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-team"))).click()
time.sleep(1)

# our_mission
our_mission = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-mission"))).click()
time.sleep(1)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Ready to start your dream project?
# Let's Get Started form fill

your_full_name = "Yash N. Vithalani"
your_email_address = "qatest12@rlogical.com"
your_phone = "7016278352"
write_message = "Project Description"

fullname_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "fname"))).send_keys(your_full_name)

email_address_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(your_email_address)

phone_number_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "mobile_no"))).send_keys(your_phone)

message_description = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='description']"))).send_keys(write_message)

send_message_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='theme_btn contact_us_send']"))).click()

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")
