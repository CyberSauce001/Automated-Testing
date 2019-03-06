from selenium import webdriver
import time, traceback, os

var = False
log = open('LogFile/Contact_Log.txt', 'w')
error = open(LogFile/Contact_Error.txt', 'w')


try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1200,1000')
    cdrive = 'chromedriver'
    url = ''
    driver = webdriver.Chrome(cdrive, options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
except Exception:
    print('Website fail to load or is down', file=log)
    traceback.print_exc(file=error)

try:
    contact_us = driver.find_element_by_link_text('Contact Us').click()
    time.sleep(10)
    textcheck = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text
    textcheck2 = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/p').text
    if textcheck == 'Let’s Connect!' and textcheck2 == 'Send Us a Message':
        var = True
    else:
        var = False
        print('Contact Page is not loaded or have changed: ',var, file=log)
except Exception:
    print('Contact Page cannot be access: ', var, file=log)
    traceback.print_exc(file=error)

try:
    fill = ['//*[@id="requestform-name-f"]', '//*[@id="requestform-name-l"]','//*[@id="requestform-phone"]',
            '//*[@id="requestform-website"]','//*[@id="requestform-email"]', '//*[@id="requestform-company"]',
            '//*[@id="requestform-message"]']
    for i in fill:
        fillin = driver.find_element_by_xpath(i).send_keys('Test')
        time.sleep(7)
except Exception:
    print('Unable to fill in field boxes: ', file=log)
    traceback.print_exc(file=error)
time.sleep(10)
log.close()
error.close()
if os.stat('LogFile/Contact_Log.txt').st_size == 0:
    os.remove('LogFile/Contact_Log.txt')
    os.remove('LogFile/Contact_Error.txt')
driver.quit()
