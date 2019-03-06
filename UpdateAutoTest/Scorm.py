import requests, json
from urllib.request import urlopen
import hashlib
from selenium import webdriver
import time , os , traceback


log = open('LogFile/Scorm_Log.txt', 'w')
error = open('LogFile/Scorm_Error.txt', 'w')

api_url = ''
acc_id = ''
scorm_cloud = ''
pwd = ''
def get_auth_token():
    # noinspection PyBroadException
    try:
        parse = {
            'usertype' : '',
            'portal_id' : '',
            'username' : '',
            'password' : '6'
        }
        response = requests.post(api_url, data = parse)
        tok = response.json()["response"]['token']
        login(tok)
    except Exception:
        print('Cannot access or log into account. May be due to response not getting token', file=log)
        traceback.print_exc(file=error)

def login(tok):
    # noinspection PyBroadException
    try:
        url = ''
        ext_url = ('{}' + acc_id +'' + tok).format(url)
        response = requests.get(ext_url)
        response = urlopen(ext_url)
        r = response.read().decode('utf-8')
        r_obj = json.loads(r)
        #check student ID
        i = 0
        students = []
        for item in r_obj['response']:
            #print("ID #{i}: {item}".format(i = i, item = item['id'])) #debug purpose
            students.append("{item}".format(item = item['id']))
            i +=1
        #md5($accountId . md5($studentId)); php code
        studentid = students[0]
        remove_user()
    except Exception:
        print('Cannot grab response of student id -> User does not exist', file=log)
        traceback.print_exc(file=error)
def remove_user():
    #Calls and grab student user name
    # noinspection PyBroadException
    try:
        ext_url = ('{}' + acc_id +'////'+ studentid + '/?_method=delete&token='+tok).format(url)
        response = requests.post(ext_url)
    except Exception:
        print('Unable to delete user', file=log)
        traceback.print_exc(file=error)


def scormtest():
    # noinspection PyBroadException
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('window-size=1680,1050')
        cdrive = 'chromedriver'
        url = 'https://cloud.scorm.com/sc/guest/SignInForm'
        driver = webdriver.Chrome(cdrive, options=options)
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
    except Exception:
        print('Unable to access Scorm Cloud',file=log)
        traceback.print_exc(file=error)
    # noinspection PyBroadException
    try:
        user = driver.find_element_by_xpath('//*[@id="email"]').send_keys(scorm_cloud)
        psw = driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
        enter = driver.find_element_by_xpath('//*[@id="signin_form"]/input[6]').click()
        time.sleep(5)
        add_content = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li/a').click()
        time.sleep(1)
        import_scorm = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li/ul/li[1]/a').click()
        time.sleep(5)
        choose_file = driver.find_element_by_xpath('//*[@id="lib_importForm_fileToImport"]').send_keys(os.getcwd()+'/.zip')
        time.sleep(1)
        import_course = driver.find_element_by_xpath('//*[@id="startImportButton"]').click()
        time.sleep(10)
        main = driver.current_window_handle
    except Exception:
        print('Unable to log in', file=log)
        traceback.print_exc(file=error)
    # noinspection PyBroadException
    try:
        launch = driver.find_element_by_xpath('//*[@id="libraryWrapper"]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div').click()
        time.sleep(15)
        popup = driver.window_handles
        driver.switch_to.window(popup.pop())
        time.sleep(5)
        check = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/p').text
        if check == 'Learn to keep your employees motivated and satisfied with their job.':
            var = True
        else:
            var = False
            print('Cannot detect text: ', var, file=log)
    except Exception:
        print('Did not launch correctly', file=log)
        traceback.print_exc(file=error)
    # noinspection PyBroadException
    try:
        intro = driver.find_element_by_xpath('//*[@id="title-watch-0f4248ad-557a-4b4c-8804-18deaaadab0d"]').click()
        time.sleep(36)
        lesson_one = driver.find_element_by_xpath('//*[@id="title-watch-6de9780c-82e2-45c1-99ad-a2b77101969c"]').click()
        time.sleep(26)
    except Exception:
        print('Lesson is not playable', file = log)
        traceback.print_exc(file=error)
    # noinspection PyBroadException
    try:
        checkpoint = driver.find_element_by_xpath('//*[@id="course-lessons"]/div[3]/div/a[2]').click()
        time.sleep(10)
        check1 = driver.find_element_by_id('watched-0f4248ad-557a-4b4c-8804-18deaaadab0d')
        check2 = driver.find_element_by_id('watched-6de9780c-82e2-45c1-99ad-a2b77101969c')
        if check1.is_displayed() and check2.is_displayed():
            var = True
        else:
            var = False
            print('Cannot detect mark: ',var, file=log)
    except Exception:
        print('Checkmark on lesson did not pass', file=log)
        traceback.print_exc(file=log)
    # noinspection PyBroadException
    try:
        driver.close()
        driver.switch_to.window(main)
        time.sleep(10)
        logout = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/p[2]/a[2]').click()
        time.sleep(10)
    except Exception:
        print('Did not log out successfully', file=log)
        traceback.print_exc(file=error)
    log.close()
    error.close()
    if os.stat('LogFile/Scorm_Log.txt').st_size == 0 :
        os.remove('Scorm_Log.txt')
        os.remove('LogFile/Scorm_Error.txt')
    driver.quit()

scormtest()
get_auth_token()
