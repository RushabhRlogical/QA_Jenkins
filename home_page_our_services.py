# import necessary classes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

# Chrome Driver Path 
chrome_driver_path = Service("D:\Software\chromedriver_win32\chromedriver.exe")

# Project URL
home_page_url = "https://dev.rlogical.com/fullstackdevteams.com/"

# chrome driver executable path
driver = webdriver.Chrome(service=chrome_driver_path)

# maximize window
driver.maximize_window()

# Current page of title
print("Current Page title: " + driver.title)

# get project url
driver.get(home_page_url)

# Current page of title
print("Current Page title: " + driver.title)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# wait 20 seconds before looking for element
# Using relative Xpath Button Class 
our_services = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='btn-wrap']//a[@class='theme_btn theme_btn-2']"))).click()
print("Clicked on Our Services Button")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# I. Web App Development Tab
web_app_development_tab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Web-App-Development']"))).click()
print("Clicked on Web App Development Tab")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Read more button for web app development tab
web_app_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='Web-App-Development']//a[text()='Read More']"))).click()
print("Clicked on Web App Development Read More Button")
time.sleep(3)

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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser GatsbyJS Service page
driver.back()
time.sleep(3)

# Scroll Page up side
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_UP)
time.sleep(1)

# II. Mobile App Development Tab
mobile_app_development_tab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Mobile-App-Development']"))).click()
print("Clicked on Mobile App Development Tab")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Read more button for Mobile App Development tab
mobile_app_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='Mobile-App-Development']//a[text()='Read More']"))).click()
print("Clicked on Mobile App Development Read More Button")
time.sleep(3)

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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser Mobile/Hybrid App Development page
driver.back()
time.sleep(3)

# Scroll Page up side
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_UP)
time.sleep(1)

# III. UI/UX Design Services Tab
design_services_tab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#UI-Design-Services']"))).click()
print("Clicked on UI/UX Design Services Tab")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Read more button for UI/UX Design Services tab
design_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='UI-Design-Services']//a[text()='Read More']"))).click()
print("Clicked on UI/UX Design Services Read More Button")
time.sleep(3)

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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser UI/UX Design page
driver.back()
time.sleep(3)

# Scroll Page up side
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_UP)
time.sleep(1)

# IV. Desktop App Development
desktop_app_development = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Desktop-App-Development']"))).click()
print("Clicked on Desktop App Development")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Read more button for Desktop App Development tab
desktop_app_development_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='Desktop-App-Development']//a[text()='Read More']"))).click()
print("Clicked on  Read More Button")
time.sleep(3)

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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser Desktop App Development page
driver.back()
time.sleep(3)

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

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")