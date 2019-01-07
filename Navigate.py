from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, traceback

#global
i=0
x=0

cdrive = ''
#create log file
log = open('', 'w')
error = open('', 'w')

#Execute Chrome
def chrome():
    #call timer
    def timer():
        time.sleep(10)
    #controls windows tab [0] = original [1] = second open tab
    def win_handler():
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        timer()
    #set to true to turn on Headless Chrome
    try:
        headless = True
        start = time.time()
        #default url
        url = ''
        #option is a set parameters that enables headless chrome when it is True
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('window-size=1200,1000')
        options.add_argument('--disable-gpu')

        #Open Chrome
        driver = webdriver.Chrome(cdrive, options=options)
        driver.get(url)
        driver.maximize_window()
        timer()
        #print(driver2.title) #debugging
    except Exception:
        print("Error going to Portal Link",file=log)

    try:
        check =[]
        for checking in check:
            checks = driver.find_element_by_xpath(checking)
            timer()
        Home =  driver.find_element_by_xpath().click()
        timer()
        var = driver.find_element_by_xpath().click()
        timer()
    except Exception:
        print(,file=log)

    try:
        global x
        Scan =[]
        for items in Scan:
            scanned = driver.find_element_by_link_text(items).click()
            x+=1
            timer()
            if x == 8:
                driver.execute_script("window.history.go(-1)")
                timer()
            if x == 9:
                links = driver.find_element_by_xpath(items).click()
                timer()
            if x>= 13 and x <19:
                other_links = driver.find_element_by_xpath(items).click()
                timer()
                win_handler()
            if x >=19:
                lang = driver.find_element_by_link_text(items).click()
                timer()
    except Exception:
        print(file=log)
        traceback.print_exc(file=error)
chrome()
