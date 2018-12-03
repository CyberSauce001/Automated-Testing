import requests
import json
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


cdrive = ''
start = time.time()
url = ''
driver = webdriver.Chrome(cdrive)
driver.get(url)
driver.maximize_window()
time.sleep(3)


All_Courses = driver.find_element_by_xpath('"]').click()
time.sleep(3)
check = driver.find_element_by_xpath('//span[contains(. , "")]')
if check:
    Go_2_Course = driver.find_element_by_xpath('/"]').click()
time.sleep(3)
check2 = driver.find_element_by_xpath('//h1[contains(text(), "")]')
if check2:
    check3 = driver.find_element_by_xpath('//"]')
    check4 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]")]')
    check5 = driver.find_element_by_xpath('//i[@class="fa fa-lock"]")]')
    if check3 and check4 and check5:
        lock_test = driver.find_element_by_xpath('//span[contains(. , "")]').click()
time.sleep(3)
check6 = driver.find_element_by_xpath('//input[@rel=""]')
check7 = driver.find_element_by_xpath('//input[@rel=""]')
check8 = driver.find_element_by_xpath('//input[@rel="c]')
time.sleep(5)
print('CheckPoint #1')
if check6 and check7 and check8:
    #the container that encapsulate the webpage
    source1 = driver.find_element_by_id('invitationWindow')
    action = ActionChains(driver)
    # move element by x,y coordinates on the screen
    action.move_to_element_with_offset(source1,5, 5)
    action.click()
    action.perform()
    time.sleep(3)
intro = driver.find_element_by_xpath('//span[contains(. , "")]').click()
time.sleep(5)
check9 = driver.find_element_by_xpath('//*[@id="i"]')
if check9:
    expand = driver.find_element_by_xpath('//*[@id="c"]/div[5]/button[2]').click()
    time.sleep(5)
    unexpand = driver.find_element_by_xpath('//*[@id="c"]/div[5]/button[2]')
    if unexpand:
        unexpand = driver.find_element_by_xpath('//*[@id=""]/div[5]/button[2]').click()
        time.sleep(3)
        print('CheckPoint #1.5')
signin = driver.find_element_by_xpath('//div[@class=""]').click()
time.sleep(3)
user = driver.find_element_by_xpath('//div[@class="form__box"]//input[@class="form__input"]').send_keys('')
time.sleep(3)
psw = driver.find_element_by_xpath('//div[@class="form__box"]//input[@id="password"]').send_keys('')
enter = driver.find_element_by_xpath('//div[@class="form__box"]//button[@type="submit"]').click()
time.sleep(15)
driver.execute_script("window.history.go(-1)")
time.sleep(15)

hiring = driver.find_element_by_xpath('//*[@id=""]').click()
time.sleep(15)
driver.get("")
time.sleep(10)
check10 = driver.find_element_by_xpath('//*[@id=""]')
if check10:
    print('CheckPoint #2')
else:
    print('Error')
######################################################################################
#Check to see if user can take test, if they can its error, since course has not been passed
time.sleep(5)
check_test = driver.find_element_by_xpath('//*[@id="c"]/a[1]').click()
check_alert = driver.find_element_by_xpath('//*[@id=""]')
time.sleep(5)

if check_alert:
    close_alert = driver.find_element_by_id('')
    actions = ActionChains(driver)
    # move element by x,y coordinates on the screen
    actions.move_to_element_with_offset(close_alert, 5, 5)
    actions.click()
    actions.perform()
    time.sleep(5)
print('Check Test Pass')

#Check to see if taking one course matches what it should read. 1/14 and should have 7% completion
mylearn = driver.find_element_by_xpath('//*[@id=""]/div[2]/span[2]/a').click()
time.sleep(5)
chosen_course = driver.find_element_by_xpath('//*[@id=""]').click()
time.sleep(5)
show_more = driver.find_element_by_xpath('//*[@id=""]/div/div[11]/div/a').click()
time.sleep(5)
check11 = driver.find_element_by_xpath('//*[@id=""]/div[4]').text
check12 = driver.find_element_by_xpath('//*[@id=""]/div[3]/span').text
if check11 == '' and check12 == '':
    print('CheckPoint #3')
else:
    print('Error')

#####################################################################################
#Pass all course
link_2_course = driver.find_element_by_xpath('//*[@id=""]/div[7]/div/a').click()
time.sleep(10)
pass_all = driver.find_element_by_xpath('//*[@id=""]/a[2]').click()
time.sleep(5)

source1 = driver.find_element_by_id('')
action2 = ActionChains(driver)
# move element by x,y coordinates on the screen
action2.move_to_element_with_offset(source1,5, 5)
action2.click()
action2.perform()
time.sleep(5)
print('')
#########################################################################################
#Check and see if all course are passed
mylearn2 = driver.find_element_by_xpath('//*[@id="usermenu"]/div[2]/span[2]/a').click()
time.sleep(5)
chosen_course2 = driver.find_element_by_xpath('//*[@id="b"]').click()
time.sleep(5)
show_more2 = driver.find_element_by_xpath('//*[@id=""]/div/div[11]/div/a').click()
time.sleep(5)
check13 = driver.find_element_by_xpath('//*[@id=""]/div[4]').text
check14 = driver.find_element_by_xpath('//*[@id=""]/div[3]/span').text
if check13 == '' and check14 == '':
    print('CheckPoint #4')
else:
    print('Error')
time.sleep(5)
#####################################################################################
#take test and fail, then take test and pass

take_test = driver.find_element_by_xpath('//*[@id=""]/div[7]/div/a').click()
time.sleep(5)
accept_button = driver.find_element_by_xpath('//*[@id=""]/div/div[2]/input[1]').click()
time.sleep(5)
lenOfPage = driver.execute_script('window.scrollTo(0, 11794)')
time.sleep(7)

#Fail Test
fail_submit = driver.find_element_by_xpath('//*[@id=""]/div[4]').click()
time.sleep(10)
fail_text = driver.find_element_by_xpath('//*[@id="t"]/div[1]/div/div[2]/div[7]/div[2]').text
if fail_text == 'You did not pass.':
    exit_quiz = driver.find_element_by_xpath('//*[@id=""]/div[1]/div/div[2]/div[7]/div[3]').click()
    print('CheckPoint #5')
    time.sleep(10)

chosen_course3 = driver.find_element_by_xpath('//*[@id=""]').click()
time.sleep(5)
show_more3 = driver.find_element_by_xpath('//*[@id=""]/div/div[11]/div/a').click()
time.sleep(5)
text_check = driver.find_element_by_xpath('//*[@id=""]/div[7]/div').text

if text_check == 'take test (1/5)':
    take_test2 = driver.find_element_by_xpath('//*[@id=""]/div[7]/div/a').click()
    time.sleep(5)
accept_button2 = driver.find_element_by_xpath('//*[@id=""]/div/div[2]/input[1]').click()
time.sleep(5)
print('CheckPoint #5.5')
############################################################################################
#Pass test
answer_all = driver.find_element_by_xpath('//*[@id=""]/div[2]/div[4]').click()
time.sleep(5)
exit_quiz2 = driver.find_element_by_xpath('//*[@id=""]/div[1]/div/div[2]/div[6]/div[3]').click()
time.sleep(10)
chosen_course3 = driver.find_element_by_xpath('//*[@id=""]').click()
time.sleep(5)
show_more3 = driver.find_element_by_xpath('//*[@id=""]/div/div[11]/div/a').click()
time.sleep(5)
"]/div[7]/div').text
if text_check2 == ':
    print('')
time.sleep(5)
clear_progress = driver.find_element_by_xpath('//*[@id=""]/div[9]/a/i').click()
time.sleep(7)
print('Course Cleared')
#####################################################################################
check_box = driver.find_element_by_xpath('//*[@id=""]/label/input').click()
time.sleep(3)
done = driver.find_element_by_xpath('//*[@id=""]/div/div[2]/input[1]').click()
time.sleep(3)
end = time.time()
print('Runtime:', end - start)
driver.close()
