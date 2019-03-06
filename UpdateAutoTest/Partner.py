from selenium import webdriver
import time, traceback, os


log = open('LogFile/Partner_Log.txt', 'w')
error = open('LogFile/Partner_Error.txt', 'w')
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
    time.sleep(5)
except Exception:
    print('Website fail to load or is down', file=log)
    traceback.print_exc(file=error)


try:
    toPartners = driver.find_element_by_xpath('//*[@id="footer"]/div[1]/div[2]/div/a[7]').click()
    time.sleep(10)

    pagetext = ['//*[@id="content"]/div/div[1]/div/h1',
                '//*[@id="content"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/p/span',
                '//*[@id="content"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/p/span',
                '//*[@id="content"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[3]/p/span',
                '//*[@id="content"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[4]/p/span']

    words= ['Channel Partners','Extensive Support - ','Partnership Rewards - ',
            'Marketing Assistance - ','Multiple Solutions - ']

    for texts in pagetext:
        checktext = driver.find_element_by_xpath(texts).text
        for w in words:
            if checktext == w:
                var = True
except Exception:
    print('Webpage Text has changed or page fail to load', file=log)
    traceback.print_exc(file=error)

try:
    button = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div/div[2]/a').click()
    time.sleep(10)
    fill = ['//*[@id="company"]','//*[@id="name_f"]','//*[@id="name_l"]','//*[@id="position"]',
            '//*[@id="phone"]','//*[@id="email"]','//*[@id="site"]','//*[@id="description"]',
            '//*[@id="interest"]','//*[@id="comments"]','//*[@id="company_address"]',
            '//*[@id="company_address_second"]','//*[@id="city"]','//*[@id="zip"]','//*[@id="company_address2"]',
            '//*[@id="company_address_second2"]','//*[@id="city2"]','//*[@id="state2"]','//*[@id="zip2"]']
    for i in fill :
        fillin = driver.find_element_by_xpath(i).send_keys('Test')
        time.sleep(5)
except Exception:
    print('Button does not work or field does not exist or cannot input into field', file=log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('ogFile/Partner_Log.txt').st_size == 0:
    os.remove('LogFile/Partner_Log.txt')
    os.remove('LogFile/Partner_Error.txt')

driver.quit()
