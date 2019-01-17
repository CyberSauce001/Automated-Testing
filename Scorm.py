import requests, json
from urllib.request import urlopen
import hashlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time , os , traceback

log = open(, 'w')
error = open(, 'w')

api_url = ''
acc_id = ''
scorm_cloud = ''
pwd = ''
var = False
def get_auth_token():
    try:
        parse = {
            'usertype' : '',
            'portal_id' : '',
            'username' : '',
            'password' : ''
        }
        response = requests.post(api_url, data = parse)
        tok = response.json()["response"]['token']
        login(api_url,acc_id,tok)
    except Exception:
        print('Cannot access or log into account. May be due to response not getting token', file=log)
        traceback.print_exc(file=error)

def login(api_url, acc_id, tok):
    try:
        url = ''
        ext_url = ('{}' + acc_id +'=' + tok).format(url)
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
        
        half_hashing = 
        full_hashing = 
        user = full_hashing
        studentid = students[0]
        remove_user(user, url, studentid, tok)
    except Exception:
        print('Cannot grab response of student id -> User does not exist', file=log)
        traceback.print_exc(file=error)
def remove_user(user,url,studentid, tok):
    #Calls and grab student user name
    try:
        check_name = ('{}' + acc_id +'' + studentid +
                      '?'
                      + tok).format(url)
        response = requests.get(check_name)
        response = urlopen(check_name)
        r = response.read().decode('utf-8')
        r_obj = json.loads(r)
        store_studentid = r_obj
        ext_url = ('{}' + acc_id +''+ studentid + '='+tok).format(url)
        response = requests.post(ext_url)
    except Exception:
        print('Unable to delete user', file=log)
        traceback.print_exc(file=error)


def scormtest():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('window-size=1680,1050')
        cdrive = 'r'
        url = 'https://cloud.scorm.com/sc/guest/SignInForm'
        driver = webdriver.Chrome(cdrive, options=options)
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
    except Exception:
        print('Unable to access Scorm Cloud',file=log)
        traceback.print_exc(file=error)

    try:
        user = driver.find_element_by_xpath('//*[@id="email"]').send_keys(scorm_cloud)
        psw = driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
        enter = driver.find_element_by_xpath('//*[@id="signin_form"]/input[6]').click()
        time.sleep(5)
        add_content = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li/a').click()
        time.sleep(1)
        import_scorm = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li/ul/li[1]/a').click()
        time.sleep(5)
        choose_file = driver.find_element_by_xpath('//*[@id="lib_importForm_fileToImport"]').send_keys(os.getcwd()+)
        time.sleep(1)
        import_course = driver.find_element_by_xpath('//*[@id="startImportButton"]').click()
        time.sleep(10)
        main = driver.current_window_handle
    except Exception:
        print('Unable to log in', file=log)
        traceback.print_exc(file=error)
    try:
        launch = driver.find_element_by_xpath('//*[@id="libraryWrapper"]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div').click()
        time.sleep(15)
        popup = driver.window_handles
        driver.switch_to.window(popup.pop())
        time.sleep(5)
        check = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/p').text
        if check == :
            var = True
        else:
            var = False
            print('Cannot detect text: ', var, file=log)
    except Exception:
        print(, file=log)
        traceback.print_exc(file=error)
    try:
        intro = driver.find_element_by_xpath('//*[@id="title-watch-0f4248ad-557a-4b4c-8804-18deaaadab0d"]').click()
        time.sleep(36)
        lesson_one = driver.find_element_by_xpath('//*[@id="title-watch-6de9780c-82e2-45c1-99ad-a2b77101969c"]').click()
        time.sleep(26)
    except Exception:
        print('Lesson is not playable', file = log)
        traceback.print_exc(file=error)
    try:
        checkpoint = driver.find_element_by_xpath('//*[@id="course-lessons"]/div[3]/div/a[2]').click()
        time.sleep(10)
        check1 = driver.find_element_by_id('watched-0f4248ad-557a-4b4c-8804-18deaaadab0d')
        check2 = driver.find_element_by_id('watched-6de9780c-82e2-45c1-99ad-a2b77101969c')
        if check1.is_displayed() and check2.is_displayed():
            var = True
        else :
            var = False
            print('Cannot detect mark: ',var, file=log)
    except Exception:
        print('Checkmark on lesson did not pass', file=log)
        traceback.print_exc(file=log)
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
    if os.stat(').st_size == 0 :
        os.remove()
        

scormtest()
get_auth_token()
