from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.jd.com')
sleep(2)
driver.find_element_by_class_name('link-login').click()
sleep(2)
driver.find_element_by_class_name('QQ-icon').click()
sleep(2)
f=driver.find_element_by_id('ptlogin_iframe')
driver.switch_to.frame(f)
sleep(2)
driver.find_element_by_link_text('帐号密码登录').click()
sleep(2)
driver.find_element_by_name('u').send_keys("2677436593")
sleep(2)
driver.find_element_by_name('p').send_keys("xll322322")
sleep(2)
driver.find_element_by_id('login_button').click()
sleep(2)

input('please input any key to exit!')