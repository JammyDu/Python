# coding = utf-8

class BasePage(object):
    """主要是把常用的几个Selenium方法封装到BasePage这个类，
    演示以下几个方法
    """
    def __init__(self, driver):
        """写一个构造函数，有一个参数driver"""
        self.driver = driver

    def back(self):
        """浏览器后退按钮"""
        self.driver.forward()

    def open_url(self, url):
        """打开url站点"""
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()