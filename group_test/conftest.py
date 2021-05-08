# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-04 15:17
# IDE: PyCharm
# =========================================================
import pytest
from Common.env_prepare import Setup_env
import os
import sys
print(sys.path)
from configparser import ConfigParser
from Common.exec_request import ExecHttp

def pytest_configure(config):
   config.addinivalue_line("markers", "great: this one is for cool tests.")
   config.addinivalue_line("markers", "others")
   config.addinivalue_line("markers", "square")
   config.addinivalue_line("markers", "regression")

@pytest.fixture(scope="session",autouse=True)
def get_config():
    conf = ConfigParser()
    conf.read("../Config/conf.ini")
    host = conf.get("BASE","host")
    port = conf.get("BASE","port")
    exec_http = ExecHttp(host, port)
    token = "123"
    case_file_list = conf.get("BASE","case_file_list").split(",")
    case_count = 0
    return [exec_http,case_count,case_file_list,token]

@pytest.fixture(scope="module",autouse=True)
def setup_env(get_config):
    print(get_config[1])
    case_file = get_config[2][get_config[1]]
    setup_env = Setup_env()
    data_total = setup_env.get_testcase("../data/"+case_file,sheet='sheet1')
    result = []
    exec_http = get_config[0]
    count =0
    token = get_config[-1]
    yield [data_total,result,count,token,exec_http]
    get_config[1] +=1



