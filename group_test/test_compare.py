# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-04 14:32
# IDE: PyCharm
# =========================================================
import pytest

@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100
   flag = "passed" if num>=100 else "failed"
   print("input:{},{}".format(num,flag))
   num = 99
   assert num >= 100
   flag = "passed" if num >= 100 else "failed"
   print("input:{},{}".format(num, flag))
   num = 122
   flag = "passed" if num >= 100 else "failed"
   print("input:{},{}".format(num, flag))


@pytest.mark.others
def test_less():
   num = 100
   assert num < 200