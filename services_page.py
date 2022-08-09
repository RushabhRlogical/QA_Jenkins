# Services Menu
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
services_page_url = "https://dev.rlogical.com/fullstackdevteams.com/services"

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

# Browser Exit process start
print("Browser Start exit Now")
driver.quit()
# Driver Quit Successfully
print("Browser Window Successfully Quit")