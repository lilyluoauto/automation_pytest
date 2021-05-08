# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-04 20:59
# IDE: PyCharm
# =========================================================
import pytest

@pytest.fixture(scope='class', autouse=True)
def login():
   print('登录系统')


def test_01():
   print('这个是类外面的用例')

class TestCase1:
   def test_02(self):
       print('测试用例2')
   def test03(self):
       print('测试用例3')

class TestCase2:
   def test_04(self):
       print('测试用例4')
   def test05(self):
       print('测试用例5')
