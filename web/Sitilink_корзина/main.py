import time
from art import tprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='D:\\python\\Selenium\\chromedriver.exe', options=options)


try:
    driver.get('https://www.citilink.ru/')
    time.sleep(3)


    src = driver.find_element_by_class_name('e1ys5m360').click()
    time.sleep(3)


    buttom = driver.find_element_by_class_name('e1j9birj0').click()
    time.sleep(1)


    buttom_cash = driver.find_element_by_link_text('Перейти в корзину').click()
  


    capture_path = 'D:\python\Sitilink_v2\Selenium_before.png'
    driver.save_screenshot(capture_path)


    buttom_clear = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[1]/div[2]/section/div[1]/div[2]/div/div/div[6]/div/div[4]/div/div').click()
    time.sleep(1)


    capture_path = 'D:\python\Sitilink_v2\Selenium_after.png'
    driver.save_screenshot(capture_path)


    come_back = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div[1]/div[2]/div/a').click()
    time.sleep(2)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    tprint(
        'The    software    has    finished    working'
    )




