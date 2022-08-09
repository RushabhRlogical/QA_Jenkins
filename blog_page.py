# import necessary classes
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

# Project URL
blog_page_url = "https://dev.rlogical.com/fullstackdevteams.com/blog/"

# chrome driver executable path
driver = webdriver.Chrome(executable_path="D:\Software\chromedriver_win32\chromedriver.exe")

# maximize window
driver.maximize_window()

# Current page of title
print("Current Page title: " + driver.title)

# get project url
driver.get(blog_page_url)

# Current page of title
print("Current Page title: " + driver.title)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Top 12 Website Revamping Mistakes You Should Stay Away From of Read more button
top_12_website_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Get Started']")))

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")