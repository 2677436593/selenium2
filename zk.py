from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def tearDown(self):
        self.driver.quit()
    def test01(self):     #登录业务
        self.driver.get('https://www.ctrip.com/')
        sleep(2)
        self.driver.refresh()    #浏览器刷新
        sleep(2)
        self.driver.find_element_by_class_name('set-text').click()   #点击登录
        sleep(2)
        self.driver.find_element_by_class_name('icon-qq').click()    #选择qq登录
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])      #窗口切换
        sleep(2)
        f=self.driver.find_element_by_id('ptlogin_iframe')       #iframe框架
        self.driver.switch_to.frame(f)
        self.driver.implicitly_wait(5)       #隐式等待
        WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.LINK_TEXT,"帐号密码登录"))).click()       #选择登录方式
        sleep(2)
        self.driver.find_element_by_name('u').send_keys('2677436593')        #输入账号
        sleep(2)
        self.driver.find_element_by_name('p').send_keys('xll322322')         #输入密码
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()     #确认登录
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
        dy1=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/ul/li[1]').text       #断言
        self.assertIn('境内',dy1)
    def test_02(self):      #酒店搜索
        self.driver.get('https://www.ctrip.com/')
        sleep(2)
        s=Select(self.driver.find_element_by_id('J_roomCountList'))
        s.select_by_index(1)         #选择房间数
        sleep(2)
        s1=Select(self.driver.find_element_by_name('Star'))
        s1.select_by_value("5")     #选择酒店级别
        sleep(2)
        self.driver.find_element_by_name('CityName').send_keys('哈尔滨',Keys.ENTER)   #输入目的地
        sleep(2)
        self.driver.find_element_by_class_name('s_btn').click()     #点击搜索
        sleep(2)
        dy2=self.driver.find_element_by_id('logintitle').text     #断言
        self.assertIn('账号登录',dy2)

    def test_03(self):
        self.driver.get('https://www.ctrip.com/')
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 下滑到底部
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,0)')  # 滑动到顶部
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,500)')  # 滑动500像素
        sleep(2)
        self.driver.find_element_by_partial_link_text('三亚').click()        #选择三亚
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])    #窗口切换
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,500)')  # 滑动500像素
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[8]/div[1]/div[1]/div/div/div[1]/img').click()   #选择团队
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 窗口切换
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,800)')  # 滑动800像素
        sleep(2)
        self.driver.find_element_by_class_name('res_btn').click()    #点击立即预定
        sleep(2)
        dy3=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]/p').text      #断言
        self.assertEqual('商家推荐',dy3)
    def test_04(self):      #自由行
        self.driver.get('https://www.ctrip.com/')
        sleep(2)
        self.driver.find_element_by_link_text('自由行').click()        #点击自由行
        sleep(2)
        self.driver.find_element_by_class_name('search_txt').send_keys('珠穆朗玛峰')     #输入珠穆朗玛峰
        sleep(2)
        self.driver.find_element_by_class_name('main_search_btn').click()       #点击搜索
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[8]/div[1]/div/div/div[1]/img').click()      #选择团队
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
        self.driver.execute_script('window.scrollTo(0,800)')  # 滑动800像素
        sleep(2)
        self.driver.find_element_by_class_name('res_btn').click()  # 点击立即预定
        sleep(2)
        dy4=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]/p').text      #断言
        self.assertEqual('线路班期',dy4)
if __name__ == '__main__':
    unittest.main(verbosity=2)