from selenium import webdriver
import time, os, traceback

error = open('LogFile/FAQ_Error.txt', 'w')
log = open('LogFile/FAQ_Log.txt', 'w')

var = False

#Headless Option
options = webdriver.ChromeOptions()
options.add_argument('window-size=1200,1000')
options.add_argument('--headless') #comment this line to see browser
cdrive = 'chromedriver'
url = ''

#Start Chrome
driver = webdriver.Chrome(cdrive, options=options)
driver.get(url)
time.sleep(7)

#Navigating to FAQ and check page
try:
    FAQ_page = driver.find_element_by_xpath('//*[@id="usermenu"]/div[1]/div[2]/span[1]/a[3]').click()
    time.sleep(3)
    check = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text
    if check == 'Frequently Asked Questions':
        var = True
    else:
        var = False
        print('Fail at Header', file=log)
    cat1 = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/div[1]').text
    cat2 = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/div[1]').text
    cc = cat2.replace("\n"," ")
    cat3 = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[3]/div[1]').text
    if (cat1 == 'Learning Library Questions & Answers' and cc == 'LMS Questions & Answers'
        and cat3 == 'Custom Content Questions & Answers'):
        var = True
    else:
        var = False
        print('Fail at SubHeader', file=log)
    time.sleep(5)
except Exception:
    var = False
    if not var:
        print('FAQ Link/Page: Failed', file=log)
        traceback.print_exc(file=error)

#Check Column 1
try:
    column_1 =['//*[@id="content"]/div/div[2]/div/div/div[1]/div[2]/div[1]',
           '//*[@id="content"]/div/div[2]/div/div/div[1]/div[2]/div[2]/p[2]/a',
           '//*[@id="content"]/div/div[2]/div/div/div[1]/div[3]/div[1]',
           '//*[@id="content"]/div/div[2]/div/div/div[1]/div[4]/div[1]',
           '//*[@id="content"]/div/div[2]/div/div/div[1]/div[4]/div[2]/p/a',
            '//*[@id="content"]/div/div[2]/div/div/div[1]/div[5]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[6]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[6]/div[2]/p[2]/a',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[7]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[8]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[8]/div[2]/p/a',
               '//*[@id="content"]/div/div[2]/div/div/div[1]/div[9]/div[1]']
    x = 0
    for i in column_1:
        test = driver.find_element_by_xpath(i).click()
        time.sleep(5)
        x += 1
        if x == 2 or x == 5 or x == 8 or x == 11:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    var = False
    if not var:
        print('Column 1: Failed', file=log)
        traceback.print_exc(file=error)
        pass
#Check Column 2
try:
    column_2 = ['//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[2]/p[2]/a',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[3]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[4]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[5]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[6]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[7]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[8]/div[1]',
                '//*[@id="content"]/div/div[2]/div/div/div[2]/div[9]/div[1]']
    x = 0
    for i in column_2:
        test = driver.find_element_by_xpath(i).click()
        x += 1
        time.sleep(5)
        if x == 2:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    var = False
    if not var:
        print('Column 2: Failed', file=log)
        traceback.print_exc(file=error)
        pass
#Check Column 3
try:
    column_3 =['//*[@id="content"]/div/div[2]/div/div/div[3]/div[2]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[2]/div[2]/p[2]/a',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[2]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[4]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[4]/div[2]/p[2]/a',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[5]/div[1]',
               '//*[@id="content"]/div/div[2]/div/div/div[3]/div[6]/div[1]']
    x = 0
    for i in column_3:
        test = driver.find_element_by_xpath(i).click()
        time.sleep(5)
        x += 1
        if x == 2 or x== 5:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    print('Column 3: Failed', file=log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('LogFile/FAQ_Log.txt').st_size == 0:
    os.remove('LogFile/FAQ_Log.txt')
    os.remove('LogFile/FAQ_Error.txt')
driver.quit()

