#autotest through faq page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, datetime, traceback

log = open('FAQ_log.txt', 'w')

#Headless Option
options = webdriver.ChromeOptions()
options.add_argument('window-size=1200,1000')
#options.add_argument('--headless') #comment this line to see browser
cdrive = ''
url = ''

#Start Chrome
driver = webdriver.Chrome(cdrive, options=options)
driver.get(url)
time.sleep(7)

#Grab time
t = time.time()
clock = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

#Navigating to FAQ and check page
try:
    FAQ_page = driver.find_element_by_xpath('').click()
    time.sleep(3)
    check = driver.find_element_by_xpath(').text
    if check == ':
        print(d [', clock,']\n',file = log)
    cat1 = driver.find_element_by_xpath(').text
    cat2 = driver.find_element_by_xpath(').text
    cc = cat2.replace("\n"," ")
    cat3 = driver.find_element_by_xpath().text
    if ():
        print( [',clock,']\n',file = log)
    time.sleep(5)
except Exception:
    traceback.print_exc(file=log)

#Check Column 1
try:
    column_1 =[]
    x = 0
    for i in column_1:
        test = driver.find_element_by_xpath(i).click()
        time.sleep(5)
        x += 1
        if x == 2 or x == 5 or x == 8 or x == 11:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    traceback.print_exc(file=log)
print('Column 1: Done [',clock,']\n',file=log)

#Check Column 2
try:
    column_2 = []
    x = 0
    for i in column_2:
        test = driver.find_element_by_xpath(i).click()
        time.sleep(5)
        x += 1
        if x == 2:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    traceback.print_exc(file=log)
print('Column 2: Done [',clock,']\n',file=log)

#Check Column 3
try:
    column_3 =[]
    x = 0
    for i in column_3:
        test = driver.find_element_by_xpath(i).click()
        time.sleep(5)
        x += 1
        if x == 2 or x== 5:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    traceback.print_exc(file=log)
print('Column 3: Done [',clock,']\n',file=log)
