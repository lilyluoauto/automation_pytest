# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-04 16:57
# IDE: PyCharm
# =========================================================
import pandas as pd
import pytest
from Common.env_prepare import Setup_env
from Common.exec_request import ExecHttp
import configparser
import profile

class TestDemo:
    @pytest.fixture(autouse=True)
    def get_input_data(self,setup_env):
        data = dict(input =  setup_env[0].iloc[setup_env[2]][3],
        method = setup_env[0].iloc[setup_env[2]][1],
        url = setup_env[0].iloc[setup_env[2]][2])
        headers = {"Application":"json","token":setup_env[3]}
        yield [data,setup_env[1],setup_env[2],headers]
        # setup_env[1].append()
        setup_env[2] += 1
        print("append result")
        setup_env[1].append(self.res)

    @pytest.mark.regression
    def test_001(self,get_input_data):
        print(get_input_data[0])
        print('测试用例一')
        self.res = "this is test_001"
        get_input_data[-1] = self.res
        # get_input_data[1].append(["this is test_001"])

    def test_02(self,get_input_data):
        print(get_input_data)
        self.res = 'this is test02'
        print('测试用例2')

    def test03(self,get_input_data):
        print(get_input_data)
        self.res = 'this is test03'
        print('测试用例3')
