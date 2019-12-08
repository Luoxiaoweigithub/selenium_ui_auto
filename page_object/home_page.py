# coding=utf-8
from page_object.base_page import BasePage


# 百度首页
class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # i=输入框, l=链接, im=图片, t=文字控件, d=div, lab=label
    # 新闻链接
    l_news = 'xpath,//a[@name="tj_trnews"]'
    # hao123链接
    l_hao123 = 'xpath,//a[@name="tj_trhao123"]'
    # 登陆链接
    l_login = 'xpath,//a[@name="tj_login"]'
    # 设置链接
    l_setting = 'xpath,//a[@name="tj_settingicon"]'
    # 更多产品链接
    l_more_product = 'xpath,//a[@name="tj_briicon"]'
    # 关键字输入框
    i_keyword = 'xpath,//input[@id="kw"]'
    # 关键字输入框
    b_search = 'xpath,//input[@id="su"]'

    def open_homepage(self):
        self.open('http://www.baidu.com/')

    # 点击新闻
    def click_news(self):
        self.wait_element(self.l_news)
        self.click(self.l_news)

    # 点击hao123
    def click_hao123(self):
        self.wait_element(self.l_hao123)
        self.click(self.l_hao123)

    # 输入搜索关键字
    def input_keyword(self, keys=u'星空物语'):
        self.wait_element(self.i_keyword)
        self.type(self.i_keyword, keys)

    # 点击搜索
    def click_search(self):
        self.click(self.b_search)