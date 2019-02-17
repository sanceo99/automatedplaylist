import time
import keys
import data_procces
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

yt_playlist = []

try:
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com')
    time.sleep(3)
    print("YT Driver started")
except:
    print("Error starting YT Driver")


try:
    driver.find_element_by_xpath("//ytd-button-renderer[@class='style-scope ytd-masthead style-blue-text size-default']/a[@class='yt-simple-endpoint style-scope ytd-button-renderer' and 1]/paper-button[@id='button' and @class='style-scope ytd-button-renderer style-blue-text size-default' and 1]/yt-formatted-string[@id='text' and @class='style-scope ytd-button-renderer style-blue-text size-default' and 1]").click()
    driver.find_element_by_class_name("Xb9hP").click()
    time.sleep(1)
    driver.find_element_by_class_name("whsOnd").send_keys(keys.yt_login)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(2)
    driver.find_element_by_class_name("Xb9hP").click()
    time.sleep(1)
    driver.find_element_by_class_name("whsOnd").send_keys(keys.yt_pass)
    time.sleep(2)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(3)
    print("YT login successful")
except:
    print("YT login error")


for i in range(len(data_procces.songs)):
    try:
        driver.find_element_by_xpath("//input[@id='search']").click()
        driver.find_element_by_xpath("//input[@id='search']").clear()
        driver.find_element_by_xpath("//input[@id='search']").send_keys(data_procces.songs[i])
        driver.find_element_by_xpath("//button[@id='search-icon-legacy']").click()
        time.sleep(2)
        element_to_hover_over = driver.find_element_by_tag_name("ytd-video-renderer")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='hover-overlays']/ytd-thumbnail-overlay-toggle-button-renderer/yt-icon").click()
        time.sleep(2)
        yt_playlist.append(str(data_procces.songs[i] + " ok"))
        print("Song" + " " + str(data_procces.songs[i]) + " added successful")
    except:
        print("Song" + " " + str(data_procces.songs[i]) + "not added")
