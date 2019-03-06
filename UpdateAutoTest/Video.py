from selenium import webdriver
import time, traceback, os


i = 0
x = 0
j = 0
m = 0
log = open('LogFile/Video_Log.txt', 'w')
error = open('LogFile/Video_Error.txt', 'w')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('window-size=1200,1000')
cdrive = 'chromedriver'
url = ''
driver = webdriver.Chrome(cdrive, options=options)
driver.get(url)
driver.maximize_window()
time.sleep(5)

try:
    All_Courses = driver.find_element_by_xpath('//span[@class="library-icon-wrapper"]').click()
    time.sleep(3)

    courses =['//span[contains(. , "Managing Remote Employees")]',
              '//h1[contains(text(), "Managing Remote Employees")]']
    for course in courses:
        check = driver.find_element_by_xpath(course)
        i += 1
        if i == 1:
            Go_2_Course = driver.find_element_by_xpath('//span[@href="/en/library/51005/business/course/managing-remote-employees/"]').click()
            time.sleep(3)
        if i == 2:
            check1 = driver.find_element_by_xpath('//i[@id="watched-f3ee981f-7493-4cc0-a597-1b5d6f8431f6"]')
            check2 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]/following::span[contains(., "Hiring the Right Employees")]')
            check3 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]/following::span[contains(., "Onboarding")]')
            if check1 and check2 and check3:
                lock_test = driver.find_element_by_xpath('//span[contains(. , "Hiring the Right Employees")]').click()
            time.sleep(3)
except Exception:
    print('Video Link has changed or no longer exist or fail to load',file=log)
    traceback.print_exc(file=error)
try:
    next_check = ['//input[@rel="join"]',
                '//input[@rel="login"]',
                '//input[@rel="closeOk"]']
    for checking in next_check:
        input_check = driver.find_element_by_xpath(checking)
        x += 1
        time.sleep(3)
        if x == 3:
            driver.refresh()
            time.sleep(3)
except Exception:
    print('Join Popup failed to show',file=log)
    traceback.print_exc(file=error)


#Log into account
try:
    signin = driver.find_element_by_xpath('//div[@class="header-item lonely"]//a[@class="menu-link"]').click()
    time.sleep(3)
    user = driver.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input"]').send_keys('')
    time.sleep(3)
    psw = driver.find_element_by_xpath('//div[@class="form__box"]//input[@id="loginform-password"]').send_keys('')
    enter = driver.find_element_by_xpath('//div[@class="form__box"]//button[@type="submit"]').click()
    time.sleep(15)
    driver.execute_script("window.history.go(-1)")
    time.sleep(15)
except Exception:
    print('Unable to Sign in',file=log)
    traceback.print_exc(file=error)
################################################################################################
try:
    hiring = driver.find_element_by_xpath('//*[@id="title-watch-cbe096ef-6312-4cc1-b52f-a38f26d59980"]').click()
    time.sleep(15)
    driver.get("")
    time.sleep(10)
    check10 = driver.find_element_by_xpath('//*[@id="watched-cbe096ef-6312-4cc1-b52f-a38f26d59980"]')
    if check10:
        var = True
    else:
        var = False
        print('Failed on going to lesson: ', var, file=log)
except Exception:
    print('Fail cannot access lesson', file=log)
    traceback.print_exc(file=error)
##################################################################
try:
    time.sleep(5)
    check_test = driver.find_element_by_xpath('//*[@id="course-controls"]/a[1]').click()
    check_alert = driver.find_element_by_xpath('//*[@id="alertWindow"]')
    time.sleep(5)

    if check_alert:
        driver.refresh()
        time.sleep(5)
except Exception:
    print('Fail at alert', file=log)
    traceback.print_exc(file=error)

#Check to see if taking one course matches what it should read. 1/14 and should have 7% completion
try:
    mylearn = driver.find_element_by_xpath('//*[@id="usermenu"]/div[2]/span[2]/a').click()
    time.sleep(5)
    chosen_course = driver.find_element_by_xpath('//*[@id="bookmark-chosen"]').click()
    time.sleep(5)
    check11 = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[4]').text
    check12 = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[3]/span').text
    if check11 == '1/14' and check12 == '7%':
        var = True
    else:
        var = False
        print('Failed at (1/14) lesson completion: ', var, file=log)
except Exception:
    print('Fail at checking incomplete lesson', file=log)
    traceback.print_exc(file=error)
#####################################################################################
#Pass all course
try:
    link_2_course = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[7]/div/a').click()
    time.sleep(10)
    pass_all = driver.find_element_by_xpath('//*[@id="course-controls"]/a[2]').click()
    time.sleep(10)

    driver.refresh()
    time.sleep(10)
except Exception:
    print('Fail at clicking on All course passing', file=log)
    traceback.print_exc(file=error)
#########################################################################################
#Check and see if all course are passed
try:
    mylearn2 = driver.find_element_by_xpath('//*[@id="usermenu"]/div[2]/span[2]/a').click()
    time.sleep(5)
    chosen_course2 = driver.find_element_by_xpath('//*[@id="bookmark-chosen"]').click()
    time.sleep(5)
    check13 = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[4]').text
    check14 = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[3]/span').text
    if check13 == '14/14' and check14 == '100%':
        var = True
    else:
        var = False
        print('Failed at (14/14) lesson completion: ', var, file=log)
    time.sleep(5)
except Exception:
    print('Fail at 100% course completed', file=log)
    traceback.print_exc(file=error)
#####################################################################################
#take test and fail, then take test and pass
try:
    take_test = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[7]/div/a').click()
    time.sleep(5)
    accept_button = driver.find_element_by_xpath('//*[@id="confirmWindow"]/div/div[2]/input[1]').click()
    time.sleep(5)
    lenOfPage = driver.execute_script('window.scrollTo(0, 11800)')
    time.sleep(7)

    #Fail Test
    fail_test = ['//*[@id="quiz_qnum25"]/div[4]',
                 '//*[@id="quiz_quiz-content"]/div[1]/div/div[2]/div[7]/div[2]',
                 '//*[@id="bookmark-chosen"]',
                 '//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[7]/div',
                 '//*[@id="confirmWindow"]/div/div[2]/input[1]']

    for fail in fail_test:
        failed = driver.find_element_by_xpath(fail).click()
        time.sleep(10)
        j+=1
        if j == 2:
            fail_text = driver.find_element_by_xpath(fail).text
            if fail_text == 'You did not pass.':
                exit_quiz = driver.find_element_by_xpath('//*[@id="quiz_quiz-content"]/div[1]/div/div[2]/div[7]/div[3]').click()
                time.sleep(7)
        if j == 2:
            if fail_text == 'take test (1/5)':
                take_test2 = driver.find_element_by_xpath('//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[7]/div/a').click()
                time.sleep(7)
except Exception:
    print('Fail at failing test', file=log)
    traceback.print_exc(file=error)
############################################################################################
#Pass test
try:
    pass_test = ['//*[@id="quiz_quiz-content"]/div[2]/div[4]',
                 '//*[@id="quiz_quiz-content"]/div[1]/div/div[2]/div[6]/div[3]',
                 '//*[@id="bookmark-chosen"]',
                 '//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[7]/div',
                 '//*[@id="course_row_4088ca71-7154-4a20-bb8b-54ef08f0e618_BUS1259"]/div[9]/a/i',
                 '//*[@id="modal__text"]/label/input',
                 '//*[@id="confirmWindow"]/div/div[2]/input[1]']
    for passer in pass_test:
        passed = driver.find_element_by_xpath(passer).click()
        m += 1
        time.sleep(10)
        if m == 4:
            pass_text = driver.find_element_by_xpath(passer).text
            if pass_text == 'passed 100%':
                time.sleep(5)
except Exception:
    print('Fail at passing test or unable to clear progress', file=log)
    traceback.print_exc(file=error)
log.close()
error.close()
if os.stat('LogFile/Video_Log.txt').st_size == 0:
    os.remove('LogFile/Video_Log.txt')
    os.remove('LogFile/Video_Error.txt')
driver.quit()


