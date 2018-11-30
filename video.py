import requests
import json
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

cdrive = '[path to your chromedriver]'
#see runtime
start = time.time()
url = '[insert url]'
driver = webdriver.Chrome(cdrive)
driver.get(url)
driver.maximize_window()
time.sleep(5)


variable1 = driver.find_element_by_xpath('//span[@class="library-icon-wrapper"]').click()
time.sleep(5)
check = driver.find_element_by_xpath('//span[contains(. , "[text]")]')
if check:
    varaible2 = driver.find_element_by_xpath('//span[@href="[insert href]"]').click()
time.sleep(5)
check2 = driver.find_element_by_xpath('//h1[contains(text(), "[tex]")]')
if check2:
    check3 = driver.find_element_by_xpath('//i[@id="[id]"]')
    check4 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]/following::span[contains(., "[text]")]')
    check5 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]/following::span[contains(., "[text]")]')
    if check3 and check4 and check5:
        end = time.time()
        print(end -start)
