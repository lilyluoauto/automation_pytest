# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-09 10:00
# IDE: PyCharm
# =========================================================
# coding:utf-8
import inspect
import sys

def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]

def yoyo():
    print("函数名称：%s"%get__function_name())
    print("name : %s"%sys._getframe().f_code.co_name)

class Yoyo():
    def yoyoketang(self):
        '''# 上海-悠悠 QQ群：588402570'''
        print("获取当前类名称.方法名：%s.%s" % (self.__class__.__name__, get__function_name()))

    def yoyo_1(self):
        print("函数名称：%s" % get__function_name())
        print("name : %s" % sys._getframe().f_code.co_name)
        print("llll")
if __name__ == "__main__":
    yoyo()
    Yoyo().yoyoketang()
    Yoyo().yoyo_1()