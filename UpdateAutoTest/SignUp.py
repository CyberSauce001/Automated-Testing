from selenium import webdriver
import time, traceback, os


log = open('LogFile/SignUp_Log.txt', 'w')
error = open('LogFile/SignUp_Error.txt', 'w')
var = False

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1200,1000')
    cdrive = 'chromedriver'
    url = ''
    driver = webdriver.Chrome(cdrive, options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
except Exception:
    print('Website fail to load or is down', file=log)
    traceback.print_exc(file=error)


try:
    toPartners = driver.find_element_by_xpath('//*[@id="loginlink"]').click()
    time.sleep(5)
    pagetext = ['//*[@id="signUpTypes"]/h1','//*[@id="signUpTypes"]/div[1]',
                '//*[@id="signUpTypes"]/div[2]/a[1]/div','//*[@id="signUpTypes"]/div[2]/a[2]/div',
                '//*[@id="signUpTypes"]/div[2]/a[3]/div','//*[@id="signUpTypes"]/div[2]/a[4]/div',
                '//*[@id="signUpTypes"]/div[2]/a[5]/div']

    words = ['Start Learning New Skills Today','To sign up, select your organization type:',
             'Individual','Business','Government','Academic','Library']
    for texts in pagetext :
        checktext = driver.find_element_by_xpath(texts).text
        for w in words :
            if checktext == w :
                var = True

    time.sleep(5)
except Exception:
    print('Webpage Text has changed or page fail to load', file=log)
    traceback.print_exc(file=error)

try:
    x = 0
    links = ['//*[@id="signUpTypes"]/div[2]/a[1]','//*[@id="signUpTypes"]/div[2]/a[2]/div',
                '//*[@id="signUpTypes"]/div[2]/a[3]/div','//*[@id="signUpTypes"]/div[2]/a[4]/div',
                '//*[@id="signUpTypes"]/div[2]/a[5]/div']
    for go in links:
        pagelink = driver.find_element_by_xpath(go).click()
        x += 1
        time.sleep(5)
        if x <= 4:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
except Exception:
    print('Links are not clickable or does not redirect', file=log)
    traceback.print_exc(file=error)

log.close()
error.close()
if os.stat('LogFile/SignUp_Log.txt').st_size == 0:
    os.remove('LogFile/SignUp_Log.txt')
    os.remove('LogFile/SignUp_Error.txt')
driver.quit()
