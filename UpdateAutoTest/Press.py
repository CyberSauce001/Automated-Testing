import cgitb
cgitb.enable()
from selenium import webdriver
import time, traceback, os


log = open('LogFile/Press_Log.txt', 'w')
error = open(LogFile/Press_Error.txt', 'w')
var = False

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1200,1000')
    cdrive = 'chromedriver'
    url = '
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
except Exception:
    print('Website fail to load or is down', file=log)
    traceback.print_exc(file=error)


try:
    toPartners = driver.find_element_by_xpath('//*[@id="footer"]/div[1]/div[2]/div/a[8]').click()
    time.sleep(5)

    pagetext =['//*[@id="content"]/div[1]/div/h1','//*[@id="content"]/div[1]/div/div',
               '//*[@id="content"]/section/div/div/div[1]/h3/a','//*[@id="content"]/section/div/div/div[2]/h3/a',
               '//*[@id="content"]/section/div/div/div[3]/h3/a']

    words =['']
    for texts in pagetext:
        checktext = driver.find_element_by_xpath(texts).text
        for w in words:
            if checktext == w:
                var = True
except Exception:
    print('Webpage Text has changed or page fail to load', file=log)
    traceback.print_exc(file=error)
time.sleep(5)
try:
    pagelink = ['//*[@id="content"]/section/div/div/div[1]/div[3]/a',
                '//*[@id="content"]/section/div/div/div[2]/div[3]/a',
                '//*[@id="content"]/section/div/div/div[3]/div[3]/a']

    for links in pagelink:
        checklink = driver.find_element_by_xpath(links).click()
        time.sleep(5)
        back = driver.find_element_by_xpath('//*[@id="content"]/section/div/div/div[2]/a').click()
        time.sleep(5)
except Exception:
    print('Webpage Links has changed or page fail to load', file=log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('LogFile/Press_Log.txt').st_size == 0:
    os.remove('LogFile/Press_Log.txt')
    os.remove('LogFile/Press_Error.txt')
driver.quit()
