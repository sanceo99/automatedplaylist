import time
import keys
from selenium import webdriver


# STARTING DRIVER

try:
    driver = webdriver.Chrome()
    driver.get('https://www.shazam.com/myshazam')
    time.sleep(3)
    window_before = driver.window_handles[0]
    time.sleep(1)
    print("Shazam Driver starter")
except:
    print("Error starting Shazam driver")


# LOGIN SHAZAM

try:
    driver.find_element_by_xpath("//a[@class='shz-text-btn fblogin ']").click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.find_element_by_id("email").send_keys(keys.fb_login)
    driver.find_element_by_id("pass").send_keys(keys.fb_pass)
    driver.find_element_by_id("loginbutton").click()
    print("Shazam Login successful")
except:
    print("Shazam Login error")


# GETTING DATA

try:
    driver.switch_to.window(window_before)
    time.sleep(5)
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    print("Data stored")
except:
    print("Data not stored")
