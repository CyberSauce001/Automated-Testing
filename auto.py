import requests
import json
from urllib.request import urlopen
from selenium import webdriver
import time

driver = webdriver.Chrome('[insert path to chromedriver if using chrome, other website look up webdriver]')

driver.get('[insert url]');
time.sleep(10) #place timer so it can delay the next process and allow user to see that page 
signin = driver.find_element_by_xpath('//div[@class="header-item lonely"]//a[@class="menu-link"]').click() #link to sign in
time.sleep(3)

#pop up login
#search login username
user = driver.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input"]').send_keys('[username]') 
time.sleep(3)

#search login password
psw = driver.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input disabledAutoFillPassword"]').send_keys('[password]')

#submit input, some website does not use submit which is ( psw.submit() or .submit() can be attach to the end of psw = '')
#if website use click use the formula below    [variable] = driver.find[whatever it is]('').click()

enter = driver.find_element_by_xpath('//div[@class="form__box"]//button[@type="submit"]').click()
time.sleep(3) 


#driver.quit() #uncomment to exit chrome and program
