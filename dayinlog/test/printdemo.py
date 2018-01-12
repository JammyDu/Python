# coding = utf-8
import time
from selenium import webdriver
import logging
from printLog import logger

mylogger = logger.Logger.getlog(__file__)


class TestMyLog(object):
    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.debug("打开浏览器")
        driver.maximize_window()
        mylogger.warning("最大化浏览器")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        mylogger.warning("打开百度首页")
        time.sleep(1)
        mylogger.warning("暂停一秒")
        driver.quit()
        mylogger.warning("关闭浏览器")
        print(logging.debug('debug message'))
        print(logging.info('info message'))
        print(logging.warning('warning message'))


testlog = TestMyLog()
testlog.print_log()
