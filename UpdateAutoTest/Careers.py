from selenium import webdriver
import time, traceback, os


log = open('LogFile/Career_Log.txt', 'w')
error = open('LogFile/Career_Error.txt', 'w')


try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1200,1000')
    cdrive = '/chromedriver'
    url = ''
    driver = webdriver.Chrome(cdrive, options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
except Exception:
    print('Website fail to load or is down', file=log)
    traceback.print_exc(file=error)

try:
    toCareer = driver.find_element_by_xpath('//*[@id="footer"]/div[1]/div[2]/div/a[6]').click()
    time.sleep(5)

    pagetext = ['//*[@id="content"]/div[1]/div/h1','//*[@id="content"]/div[1]/div/div[1]',
                '//*[@id="content"]/div[1]/div/div[3]/div[1]','//*[@id="content"]/div[1]/div/div[3]/div[2]']

    words = ['']
    for texts in pagetext:
        checktext = driver.find_element_by_xpath(texts).text
        for w in words:
            if checktext == w:
                var = True
except Exception:
    print('Webpage Text has changed or page fail to load', file=log)
    traceback.print_exc(file=error)

try:
    f = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[2]/span').click()
    time.sleep(5)
    links = ['//*[@id="careers-enum"]/div/div[1]/div/div[3]/a','//*[@id="careers-enum"]/div/div[2]/div/div[3]/a',
             '//*[@id="careers-enum"]/div/div[3]/div/div[3]/a','//*[@id="careers-enum"]/div/div[4]/div/div[3]/a',
             '//*[@id="careers-enum"]/div/div[5]/div/div[3]/a','//*[@id="careers-enum"]/div/div[6]/div/div[3]/a',
             '//*[@id="careers-enum"]/div/div[7]/div/div[3]/a']
    for view in links:
        careerlink = driver.find_element_by_xpath(view).click()
        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(5)
except Exception:
    print('', file=log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('LogFile/Career_Log.txt').st_size == 0:
    os.remove('LogFile/Career_Log.txt')
    os.remove('LogFile/Career_Error.txt')
driver.quit()
