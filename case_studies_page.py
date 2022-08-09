# Case Studies Page
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
services_page_url = "https://dev.rlogical.com/fullstackdevteams.com/case-studies"

# chrome driver executable path
driver = webdriver.Chrome(service=chrome_driver_path)

# maximize window
driver.maximize_window()

# Current page of title
print("Current Page title: " + driver.title)

# get project url
driver.get(services_page_url)

# Current page of title
print("Current Page title: " + driver.title)

# scroll down page
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# 1. reserve my seat case studies

action = ActionChains(driver)
reserve_myseat_option = driver.find_element(By.XPATH, "//div[@class='thumb bg-img-c']")
time.sleep(3)
action.move_to_element(reserve_myseat_option).perform()
time.sleep(3)

select_reserve_myseat_option = driver.find_element(By.XPATH, "//h4[text()='ReserveMySeat']")
time.sleep(3)

# hover over element and click
action.move_to_element(select_reserve_myseat_option).click().perform()
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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser page of reserve my seat case studies
driver.back()
time.sleep(3)

# 2. clean my motor cycle case studies

select_clean_my_motor_cycle_option = driver.find_element(By.XPATH, "//h4[text()='CleanMymotorCycle']")
time.sleep(3)

# hover over element and click
action.move_to_element(select_clean_my_motor_cycle_option).click().perform()
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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser page of clean my motor cycle of case studies
driver.back()
time.sleep(3)

# 3. Employer case studies

select_employer_option = driver.find_element(By.XPATH, "//h4[text()='Employerr']")
time.sleep(3)

# hover over element and click
action.move_to_element(select_employer_option).click().perform()
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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser page of Employer of case studies
driver.back()
time.sleep(3)

# scroll down page 
body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# 4. Legal Counsel Community case studies

select_legal_counsel_community_option = driver.find_element(By.XPATH, "//h4[text()='Legal Counsel Community']")
time.sleep(3)

# hover over element and click
action.move_to_element(select_legal_counsel_community_option).click().perform()
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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser page of Legal Counsel Community of case studies
driver.back()
time.sleep(3)

# 5. Megacity Empower Management case studies

select_megacity_empower_management_option = driver.find_element(By.XPATH, "//h4[text()='Megacity Empower Management']")
time.sleep(3)

# hover over element and click
action.move_to_element(select_megacity_empower_management_option).click().perform()
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
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# back from browser page of  Megacity Empower Management of case studies
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

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")