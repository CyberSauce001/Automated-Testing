from selenium import webdriver
import time, traceback, os

error = open('LogFile/Cert_Error.txt', 'w')
log = open('LogFile/Cert_Log.txt', 'w')

var = False


def win_handler():
    driver.execute_script("window.history.go(-1)")
    time.sleep(5)

try:
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1200,1000')
    options.add_argument('--headless')
    cdrive = 'chromedriver'
    url = ''
    driver = webdriver.Chrome(cdrive, options=options)
    driver.get(url)
    time.sleep(5)
    cert = driver.find_element_by_xpath('//*[@id="usermenu"]/div[1]/div[2]/span[1]/a[2]').click()
    time.sleep(5)
except Exception:
    print('Website is down or fail to load or Certificate Link fail to load', file = log)
    traceback.print_exc(file=error)

try:
    checking =['//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[1]/h2',
               '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[1]/p',
               '//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[1]/h2']
    text = ['User’s Name','Certificates will display the user’s name when the course is successfully completed.',
            'Course Name']
    for i in checking:
        checktext = driver.find_element_by_xpath(i).text
        if checktext in text:
            var = True
except Exception:
    print('WebPage has change text near the certificate image', file =log)
    traceback.print_exc(file=error)

try:
    checking2 =['//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[1]/p',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[2]/h2',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[2]/p',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[2]/h2',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[2]/p',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[3]/h2',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div[3]/p',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[3]/h2',
                '//*[@id="content"]/div[1]/div[3]/div/div/div/div[3]/div[3]/p']

    text2 = ['']

    for m in checking2:
        checkertext2 = driver.find_element_by_xpath(m).text
        cc = checkertext2.replace("\n", " ")  #bypass <br> in the paragraph
        if cc in text2:
            var = True
except Exception:
    print('WebPage has change text near the certificate image', file =log)
    traceback.print_exc(file=error)

try:
    checking3 = ['//*[@id="content"]/div[2]/div/div[2]/p/a',
                 '//*[@id="content"]/section/div/div[2]/div[1]/p/a',
                 '//*[@id="content"]/section/div/div[2]/div[2]/p/a',
                 '//*[@id="content"]/section/div/div[2]/div[3]/p/a']

    testlink = ['']

    for link in checking3:
        time.sleep(5)
        checklink = driver.find_element_by_xpath(link).click()
        time.sleep(5)
        linktest = driver.find_element_by_tag_name('h1').text
        if linktest in testlink:
                win_handler()
                time.sleep(5)
except Exception:
    print('Links on this page does not work or have been changed', file =log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('LogFile/Cert_Log.txt').st_size == 0:
    os.remove('LogFile/Cert_Log.txt')
    os.remove('LogFile/Cert_Error.txt')

driver.quit()

