# coding = utf-8
import time
from selenium import webdriver

from test1.basepage import BasePage


class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(6)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)

    def test_serch(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(1)
        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_serch()