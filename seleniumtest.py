from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginpassword import *
from urlslist import *
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

URL = 'http://vns.lpnu.ua/login/index.php'


def log_in(times):
    for i in range(times):
        for j in lst:
            driver = webdriver.Chrome(PATH)
            driver.get(j)
            loginField = driver.find_element_by_id('username')
            loginField.clear()
            loginField.send_keys(loginVNS)

            passwordField = driver.find_element_by_id('password')
            passwordField.clear()
            passwordField.send_keys(pswdVNS)
            passwordField.send_keys(Keys.RETURN)
            time.sleep(3)

            driver.close()

log_in(10)