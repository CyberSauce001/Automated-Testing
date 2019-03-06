from selenium import webdriver
import time, traceback, os

#global
i=0
x=0

cdrive = ''
#create log file
log = open('LogFile/Navigate_Log.txt', 'w')
error = open('LogFile/Navigate_Error.txt', 'w')

#Execute Chrome
def chrome():
    #call timer
    def timer():
        time.sleep(7)
    #controls windows tab [0] = original [1] = second open tab
    def win_handler():
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        timer()
    #set to true to turn on Headless Chrome
    try:
        headless = True
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
        traceback.print_exc(file=error)

    try:
        check =['//h1[contains(text(), "")]','//h5[contains(text(), "Learning Library")]',
                '//h5[contains(text(), "")]','//h5[contains(text(), "Custom Courses")]']
        for checking in check:
            checks = driver.find_element_by_xpath(checking)
            timer()
        Home =  driver.find_element_by_xpath('//a[@href="/en/"]').click()
        timer()
        KC_Logo = driver.find_element_by_xpath('//a[@class="header__logo-wrapper"]//img[@class="header__logo"]').click()
        timer()
    except Exception:
        print("Error Home Page has been modify, does not load, or does not match the original Home Page",file=log)
        traceback.print_exc(file=error)


    global x
    Scan =['Certification', 'FAQ','About Us','Contact Us','Learning Library','','Custom Courses',
            'Sign Up','Home','Careers','Partners','Press Release']
    Scan2 =['//a[@class="follow-us__link facebook"]','//a[@class="follow-us__link google"]',
            '//a[@class="follow-us__link twitter"]','//a[@class="follow-us__link linkedin"]',
            '//a[@class="follow-us__link blog"]','//a[@class="follow-us__link youtube"]','//img[@class="bbb"]']

    for items in Scan:
        try :
            scanned = driver.find_element_by_link_text(items).click()
            x+=1
            #print(x)
            timer()
            if x == 8:
                driver.execute_script("window.history.go(-1)")
                timer()
            if x == 9:
                links = driver.find_element_by_xpath('//span[@class="library-icon-wrapper"]').click()
                timer()
        except Exception :
            print('Scan: There one or more of the links are not working properly.Please check Navigate_Error.txt. Link: ', items , file=log)
            traceback.print_exc(file=error)
            pass
    for items2 in Scan2:
        try:
                other_links = driver.find_element_by_xpath(items2).click()
                timer()
                win_handler()
        except Exception :
            print('Scan2: There one or more of the links are not working properly.Please check Navigate_Error.txt. Link:', items2, file=log)
            traceback.print_exc(file=error)
            pass
    log.close()
    error.close()
    if os.stat('LogFile/Navigate_Log.txt').st_size == 0:
        os.remove('LogFile/Navigate_Log.txt')
        os.remove('LogFile/Navigate_Error.txt')
    driver.quit()

chrome()
