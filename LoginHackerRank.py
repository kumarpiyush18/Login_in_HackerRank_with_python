from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver=webdriver.Chrome()
driver.get('https://www.hackerrank.com/')
userID='your_user_id'               #replace the string with user id
pass_w='your_password'    #replace the string with password
element=driver.find_element_by_link_text('Log In')
element.click()
time.sleep(10)

ele=driver.find_element_by_id('login')#first search that container(div){by their id/class/} in which both placed
login_user=ele.find_element_by_name('login')
login_user.send_keys(userID)

elem=ele.find_element_by_name('password')
elem.send_keys(pass_w)
elem.send_keys(Keys.ENTER)


