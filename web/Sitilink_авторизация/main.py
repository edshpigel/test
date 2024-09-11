import time
import Login
import Password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from art import tprint


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='D:\\python\\Selenium\\chromedriver.exe', options=options)
try:
    driver.get('https://www.citilink.ru/')
    time.sleep(1)
    entrance = driver.find_element_by_class_name('ekyeari0').click()
    time.sleep(1)
    login = driver.find_element_by_name('login')
    login.clear()
    login.send_keys(Login.login)
    time.sleep(2)
    password = driver.find_element_by_name('pass')
    password.clear()
    password.send_keys(Password.password)
    time.sleep(2)
    password.send_keys(Keys.ENTER)
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    tprint(
        'The    software    has    finished    working'
        )


