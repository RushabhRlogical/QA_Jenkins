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
our_work = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='theme_btn theme_btn-4']"))).click()
print("Our Work Button Click Event")
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# Using relative Xpath using text
get_started = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Get Started']"))).click()
print("On Get Started Button Clicking fired Successfully")

# scroll down page 
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Contact us page field of data 
first_name = "Yash"
email_id = "qatest123@rlogical.com"
code = "+91"
phone = "7016278352"
company_name = "Rlogical"
category_text = "Mobile App Development"
description_text = "Hello Rlogical Team, Very Good morning"

# Name field elemnet find using relative Xpath 
name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='fname']"))).send_keys(first_name)

# Email field elemnet find using relative Xpath
email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email address']"))).send_keys(email_id)

# Country code drop down box field elemnet find using relative Xpath
country_code = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='iti__selected-flag']"))).click()

# Select Country code field elemnet find using relative Xpath
select_code = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='iti__country iti__standard']//span[text()='"+code+"']"))).click()

# Phone Number field elemnet find using relative Xpath
your_phone_no = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "countries_code"))).send_keys(phone)

# Company field elemnet find using relative Xpath
company = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='company_name']"))).send_keys(company_name)

# Category field elemnet find using relative Xpath
category_open = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='category']//option[text()='"+category_text+"']"))).click()

# Description field elemnet find using relative Xpath and send data in field
description = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='description']"))).send_keys(description_text)

body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Send Message button elemnet find using relative Xpath
send_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='row']//button[@class='blue_theme_btn contact_us_send']"))).click()
print("clicked on Send Message button") 
time.sleep(2)

# Home page redirection text link
home_page_text_url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Home Page']"))).click()
print("Home page redirection text link")
time.sleep(2)

# scroll down page 
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# learn more button on about us section 
learn_more_about_us = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='about_content']//a[@class='theme_btn']"))).click()
print("learn more button on about us section ")
time.sleep(2)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body"))) 
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# full stack mobile app development
full_stack_mobile_app_dev_link_text = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='about_content']//a[text()='full stack mobile app development']"))).click()
print("full stack mobile app development")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body"))) 
body.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# The Top-Tier Web and App Development Agency
check_out_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='about_content']//a[text()='Check Out More']"))).click()
print("The Top-Tier Web and App Development Agency check out more button")
time.sleep(2)

# back from browser page
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

# Web App Development Section
webapp_dev_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='service-box-link']//h3[text()='Web App ']"))).click()
print("Web App Development Section")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# Mobile/Hybrid App Development Section
mobile_app_dev_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='service-box-link']//h3[text()='Mobile/Hybrid ']"))).click()
print("Mobile/Hybrid App Development Section")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# UI/UX Design Services Development Section
design_services_dev_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='service-box-link']//h3[text()='UI/UX Design ']"))).click()
print("UI/UX Design Services Development Section")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# Desktop App Development Section
desktop_app_dev_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='service-box-link']//h3[text()='Desktop App Development']"))).click()
print("Desktop App Development Section")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# our vision tab
our_vision = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-history"))).click()
print("our vision tab Section")
time.sleep(1)

# our values tab
our_values = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-business"))).click()
print("our values tab Section")
time.sleep(1)

# our approach tab
our_approach = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-team"))).click()
print("our approach tab Section")
time.sleep(1)

# our mission tab
our_mission = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "nav-mission"))).click()
print("our mission tab Section")
time.sleep(1)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Let’s Talk Button 
lets_talk_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='theme_btn'][text()='Let’s Talk']"))).click()
print("Let’s Talk Button")
time.sleep(2)

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

# back from browser page
driver.back()
time.sleep(3)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Ready to start your dream project?
# Let's Get Started form fill
your_full_name = "Yash N. Vithalani"
your_email_address = "qatest12@rlogical.com"
your_phone = "7016278352"
write_message = "Project Description"

# full_name_field
fullname_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "fname"))).send_keys(your_full_name)
print("full_name_field")
time.sleep(2)

# email_address_field
email_address_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(your_email_address)
print("email_address_field")
time.sleep(2)

# phone_number_field
phone_number_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "mobile_no"))).send_keys(your_phone)
print("phone_number_field")
time.sleep(2)

# message_description_field
message_description = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='description']"))).send_keys(write_message)
print("message_description_field")
time.sleep(2)

# send_message_button
send_message_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='theme_btn contact_us_send']"))).click()
print("send_message_button")
print("Ready to start your dream project? Let's Get Started")
time.sleep(2)

# clicking on website logo
logo = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='header-nav']//*[@id='Layer_1']"))).click()
print("clicked on website logo")
time.sleep(2)

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

view_all_project_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@class='section-gap portfolio-section grey-bg']//a[@class='theme_btn']"))).click()
print("View All project Button")
time.sleep(2)

# back from browser page
driver.back()
time.sleep(3)

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")