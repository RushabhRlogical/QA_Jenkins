import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        # Chrome Driver Path 
        chrome_driver_path = 'D:\Software\chromedriver_win32\chromedriver.exe'
        
        # Chrome Driver Path 
        self.driver = webdriver.Chrome(chrome_driver_path)
        
        # maximize window
        self.driver.maximize_window()
        
        # Current page of title
        print("Current Page title: " + self.driver.title)

    def test_homepage_ourwork(self):
        home_page_url = "https://dev.rlogical.com/fullstackdevteams.com/"
        
        driver = self.driver
        
        # get Project URL
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
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        view_all_project_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//section[@class='section-gap portfolio-section grey-bg']//a[@class='theme_btn']"))).click()
        print("View All project Button")

        # back from browser page
        driver.back()
        time.sleep(3)

    def test_homepage_ourservices(self):
        homepage_url = "https://dev.rlogical.com/fullstackdevteams.com/"
        
        driver = self.driver

        # get Project URL
        driver.get(homepage_url)
        
        # Current page of title
        print("Current Page title: " + self.driver.title)

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

    def test_aboutus(self):
        aboutus_page_url = "https://dev.rlogical.com/fullstackdevteams.com/about-us"

        driver = self.driver

        # get Project URL
        driver.get(aboutus_page_url)
        
        # Current page of title
        print("Current Page title: " + self.driver.title)

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

    def test_services(self):
        services_page_url = "https://dev.rlogical.com/fullstackdevteams.com/services"

        driver = self.driver

        # get Project URL
        driver.get(services_page_url)
        
        # Current page of title
        print("Current Page title: " + self.driver.title)

        # Mouse hover on services menu 
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # A. Web App Development TAB

        # 1. Angular
        angulr_service = driver.find_element(By.XPATH, "//span[text()='Angular']").click()
        print("Clicked on Web App Development TAB of Angular Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Angular Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Angular page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 2. React
        react_service = driver.find_element(By.XPATH, "//span[text()='React']").click()
        print("Clicked on Web App Development TAB of React Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of React Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of React page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 3. NodeJS
        node_js_service = driver.find_element(By.XPATH, "//span[text()='NodeJS']").click()
        print("Clicked on Web App Development TAB of NodeJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of NodeJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of NodeJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 4. VueJS
        vue_js_service = driver.find_element(By.XPATH, "//span[text()='VueJS']").click()
        print("Clicked on Web App Development TAB of VueJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of VueJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of VueJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 5. PHP
        php_service = driver.find_element(By.XPATH, "//span[text()='PHP']").click()
        print("Clicked on Web App Development TAB of PHP Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of PHP Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of PHP page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 6. ASP
        asp_dot_net_service = driver.find_element(By.XPATH, "//span[text()='ASP']").click()
        print("Clicked on Web App Development TAB of ASP.NET Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of ASP Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of ASP page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 7. Java
        java_service = driver.find_element(By.XPATH, "//span[text()='Java']").click()
        print("Clicked on Web App Development TAB of Java Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Java Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Java page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 8. Python
        python_service = driver.find_element(By.XPATH, "//span[text()='Python']").click()
        print("Clicked on Web App Development TAB of Python Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Python Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Python page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 9. JavaScript
        java_script_service = driver.find_element(By.XPATH, "//span[text()='JavaScript']").click()
        print("Clicked on Web App Development TAB of JavaScript Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of JavaScript Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of JavaScript page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 10. ExpressJS
        express_js_service = driver.find_element(By.XPATH, "//span[text()='ExpressJS']").click()
        print("Clicked on Web App Development TAB of ExpressJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of ExpressJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of ExpressJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 11. MeteorJS 
        meteor_js_service = driver.find_element(By.XPATH, "//span[text()='MeteorJS']").click()
        print("Clicked on Web App Development TAB of MeteorJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of MeteorJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of MeteorJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 12. Ruby
        ruby_service = driver.find_element(By.XPATH, "//span[text()='Ruby']").click()
        print("Clicked on Web App Development TAB of Ruby Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Ruby Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Ruby page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 13. EmberJS
        ember_js_service = driver.find_element(By.XPATH, "//span[text()='EmberJS']").click()
        print("Clicked on Web App Development TAB of EmberJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of EmberJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of EmberJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # 14. GatsbyJS
        gatsby_js_service = driver.find_element(By.XPATH, "//span[text()='GatsbyJS']").click()
        print("Clicked on Web App Development TAB of GatsbyJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of GatsbyJS Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of GatsbyJS page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 1. React native
        react_native_service = driver.find_element(By.XPATH, "//span[text()='React native']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of React native Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of React native Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of React native page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 2. Flutter
        flutter_service = driver.find_element(By.XPATH, "//span[text()='Flutter']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Flutter Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Flutter Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Flutter page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 3. Vue Native
        vue_native_service = driver.find_element(By.XPATH, "//span[text()='Vue Native']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Vue Native Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Vue Native Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Vue Native page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 4. Swift
        swift_service = driver.find_element(By.XPATH, "//span[text()='Swift']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Swift Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Swift Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Swift page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 5. Ionic
        ionic_service = driver.find_element(By.XPATH, "//span[text()='Ionic']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Ionic Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Ionic Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Ionic page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 6. Xamarin
        xamarin_service = driver.find_element(By.XPATH, "//span[text()='Xamarin']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Xamarin Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Xamarin Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Xamarin page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 7. Kotlin
        kotlin_service = driver.find_element(By.XPATH, "//span[text()='Kotlin']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Kotlin Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Kotlin Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Kotlin page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # B. Mobile/Hybrid App Development TAB
        select_mobile_app_dev_tab_option = driver.find_element(By.XPATH, "//button[@id='mobileapp-tab']").click()
        time.sleep(3)

        # 8. Objective-C
        objective_c_service = driver.find_element(By.XPATH, "//span[text()='Objective-C']").click()
        print("Clicked on Mobile/Hybrid App Development TAB of Objective-C Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Objective-C Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Objective-C page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # C. UI/UX Design TAB
        select_design_tab_option = driver.find_element(By.XPATH, "//button[@id='uiuxdesign-tab']").click()
        time.sleep(3)

        # 1. Custom Web Design 
        custom_web_design_option = driver.find_element(By.XPATH, "//span[text()='Custom Web Design']").click()
        print("Clicked on UI/UX Design TAB of Custom Web Design Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Custom Web Design Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Custom Web Design page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # C. UI/UX Design TAB
        select_design_tab_option = driver.find_element(By.XPATH, "//button[@id='uiuxdesign-tab']").click()
        time.sleep(3)

        # 2. Mobile UI/UX Design Services
        mobile_design_service = driver.find_element(By.XPATH, "//span[text()='Mobile UI/UX Design Services']").click()
        print("Clicked on UI/UX Design TAB of Mobile UI/UX Design Services Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Mobile UI/UX Design Services Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Mobile UI/UX Design Services page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # C. UI/UX Design TAB
        select_design_tab_option = driver.find_element(By.XPATH, "//button[@id='uiuxdesign-tab']").click()
        time.sleep(3)

        # 3. Responsive UI/UX Design
        responsive_design_service = driver.find_element(By.XPATH, "//span[text()='Responsive UI/UX Design']").click()
        print("Clicked on UI/UX Design TAB of Responsive UI/UX Design Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Mobile UI/UX Design Services Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Mobile UI/UX Design Services page
        driver.back()
        time.sleep(3)

        # mouse hover on services TAB
        action = ActionChains(driver)
        mouse_hover_on_services_menu = driver.find_element(By.XPATH, "//a[@id='res-mega']")
        time.sleep(3)
        action.move_to_element(mouse_hover_on_services_menu).perform()
        time.sleep(3)

        # D. Desktop App
        select_desktop_app_tab_option = driver.find_element(By.XPATH, "//button[@id='desktopapp-tab']").click()
        time.sleep(3)

        # 1. ElectronJS
        electron_js_service = driver.find_element(By.XPATH, "//span[text()='ElectronJS']").click()
        print("Clicked on Desktop App TAB of ElectronJS Option")
        time.sleep(3)

        # Discuss your project button
        discuss_your_project_button = driver.find_element(By.XPATH, "//a[@class='theme_btn theme_btn-4'][text()='Discuss your Project']").click()
        time.sleep(3)

        # back from browser page of Desktop App Contact Us page
        driver.back()
        time.sleep(3)

        # back from browser page of Desktop App Service page
        driver.back()
        time.sleep(3)

        # scroll down Services page
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

    def test_casestudies(self):
        casestudies_page_url = "https://dev.rlogical.com/fullstackdevteams.com/case-studies"

        # get Project URL
        driver.get(casestudies_page_url)
        
        # Current page of title
        print("Current Page title: " + self.driver.title)

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

    def test_blog(self):
        driver = self.driver

        # get Project URL
        driver.get("https://dev.rlogical.com/fullstackdevteams.com/blog/")
        
        # Current page of title
        print("Current Page title: " + self.driver.title)


        # scroll down page
        body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        # Top 12 Website Revamping Mistakes You Should Stay Away From of Read more button
        top_12_website_read_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Get Started']")))

    def tearDown(self):
       # self.driver.close()
       # Browser Close process start
        print("Browser Start close Now")
        self.driver.close()
        # Driver Close Successfully
        print("Browser Window Successfully Close")

if __name__ == "__main__":
    unittest.main()