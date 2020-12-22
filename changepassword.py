from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""
newpassword = ""

browser = webdriver.Chrome()
browser.get ("https://twitter.com/settings/password")
time.sleep(1)

usernameİnput = browser.find_element_by_name("session[username_or_email]")
usernameİnput.send_keys(username)

passwordİnput = browser.find_element_by_name("session[password]")
passwordİnput.send_keys(password)
passwordİnput.send_keys(Keys.ENTER)
time.sleep(4)

nowpasswordİnput = browser.find_element_by_name("current_password")
nowpasswordİnput.send_keys(password)
newpasswordİnput = browser.find_element_by_name("new_password")
newpasswordİnput.send_keys(newpassword)
newpasswordConfirmationİnput = browser.find_element_by_name("password_confirmation")
newpasswordConfirmationİnput.send_keys(newpassword)
newpasswordConfirmationİnput.send_keys(Keys.ENTER)
time.sleep(2)
browser.close()














