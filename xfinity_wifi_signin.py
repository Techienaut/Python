#!/usr/bin/env python3
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException as TE

chrome_options = webdriver.ChromeOptions()
#dcaps_eager = DesiredCapabilities().CHROME
#dcaps_eager["pageLoadStrategy"] = "eager"
chrome_options.set_capability("pageLoadStrategy","none")
chrome_options.add_argument("--user-data-dir=/home/vagrant/.config/google-chrome/Profile 2")

#Chromeoptions = webdriver.ChromeOptions()
#Chromeoptions.add_argument('user-data-dir=/home/vagrant/.config/google-chrome/Profile 2')
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/bin/chromedriver')
browser.get('http://192.0.2.1')

#browser.get('https://wifilogin.xfinity.com/portal_captive.php?h=o%2BsDOz4P9hpp7nb1nc6UhG%2FVCRzEWAiMd4g%2BpQN9lkWO1nZF7zdd4OJOdrLVP1JXYg7e%2FLLG%2F1mf9%2BTxzpsEYvfXgQUkA2l4Z3lQKKY4845JAuzkWAk8hiJbUCO7Oh4ebe7YyBSeAXVOdJPwLy48mg%3D%3D')
gettingStarted_bttn = WebDriverWait(browser,15).until(EC.presence_of_element_located((By.ID,'amdocs_signup')))
gettingStarted_bttn.click()

hourpass =  WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'offersFreeList1')))
hourpass.click()
continue_hourpass = browser.find_element_by_id('continueButton')
continue_hourpass.click()
try:
    upgradeOffer_cancel_bttn = WebDriverWait(browser,3).until(EC.presence_of_element_located((By.ID,'upgradeOfferCancelButton')))
    upgradeOffer_cancel_bttn.click()
except TE as te:
    print("No offer upgrade")
letters = string.ascii_letters + string.digits
username_str = ''.join(random.choice(letters) for i in range(14))
email_str = username_str + "@kj.kj"
first_name_str = 'kj'
last_name_str = 'kj'
zipCode_str = '61820'

first_name_textbox = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'registerFirstName')))
last_name_textbox = browser.find_element_by_id('registerLastName')
email_textbox = browser.find_element_by_id('registerEmail')
zipCode_textbox = browser.find_element_by_id('registerZipCode')
first_name_textbox.send_keys(first_name_str)
last_name_textbox.send_keys(last_name_str)
email_textbox.send_keys(email_str)
zipCode_textbox.send_keys(zipCode_str)

continue_register_bttn = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,'registerContinueButton')))
continue_register_bttn.click()

#username_textbox = browser.find_element_by_id('userName')
username_textbox = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="userName"]')))
username_textbox.send_keys(username_str)
secrect_question_select = browser.find_element_by_id('dk0-secretQuestion')
secrect_question_select.click()
whatIsFavMovie_select = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.ID,'dk0-What-is your favorite movie?')))
whatIsFavMovie_select.click()
secret_answer_str = 'jiwioajo iowefwiojaw'
secret_answer_textbox = browser.find_element_by_id('secretAnswer')
secret_answer_textbox.send_keys(secret_answer_str)
password_str = 'weuofwaFE1!'
password_textbox = browser.find_element_by_id('password')
password_textbox.send_keys(password_str)
passwordRetype = browser.find_element_by_id('passwordRetype')
passwordRetype.send_keys(password_str)
submitPassword_bttn = browser.find_element_by_id('submitButton')
submitPassword_bttn.click()

continue_register_bttn = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,'registerContinueButton')))
continue_register_bttn.click()

confirm_activation_pass_bttn = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID, '_orderConfirmationActivatePass')))
confirm_activation_pass_bttn.click()
print('hello world')