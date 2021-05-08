# coding:utf-8
# !/usr/bin/python
# ========================================================
# Project: automationTest
# Creator: lilyluo
# Create time: 2021-05-04 22:32
# IDE: PyCharm
# =========================================================

from unittest import TestCase
import pytest
import allure
from Common.env_prepare import Setup_env
import os

class Test_BindMobile(TestCase):
    '''bind mobile phone'''
    @classmethod
    def setUpClass(cls):
        configfile = u'../Config/conf.ini'
        print("run setup_class")
        # test cases with trade fee
        testCaseFile = '../Data/testcaseFront.xlsx'
        sheet = u'bindMobile'
        # cls.user='yongli.luo@lbank.info'
        # cls.password='lbanktest1'
        # cls.comm = Common(configfile)
        # cls.input = cls.comm.getInputData(testCaseFile,sheet)
        # cls.expResult = cls.comm.getExpResult(testCaseFile, sheet)
        # cls.urls = cls.comm.getUrls(testCaseFile,sheet)
        # cls.methods = cls.comm.getMethods(testCaseFile,sheet)
        # # cls.log = LoginF(configfile)
        # # cls.token = cls.log.getToken(cls.user,cls.password)
        # cls.exeHttp=ExecHttpF(configfile)
        # cls.testresult =TestResult()
        cls.setup_env = Setup_env()
        cls.setup_env.clean_dir(os.path.abspath("./report"))


    @classmethod
    def tearDownClass(cls):
        print("class tear down {}".format(cls.__name__))
        pass

    def setUp(self):

        print("run the {}".format(self._testMethodName))

    def tearDown(self):
        # if self.result:
        #     print("the actual test result is {}".format(self.result))

        print("teardown {}".format(self._testMethodName))

    @allure.feature("BindMobile")
    @allure.story("001")
    def test_BindMobile_001(self):
        '''bind mobile successfully without 2FA'''
        s = self._testMethodName
        print(s)

    @allure.feature("BindMobile")
    @allure.story("002","003")
    def test_BindMobile_002(self):
        '''bind mobile successfully without 2FA'''
        s = self._testMethodName
        print(s)


class Test_AW(TestCase):
    '''bind mobile phone'''

    @classmethod
    def setUpClass(cls):
        configfile = u'../Config/conf.ini'
        print("run setup_class")
        # test cases with trade fee
        testCaseFile = '../Data/testcaseFront.xlsx'
        sheet = u'bindMobile'
        # cls.user='yongli.luo@lbank.info'
        # cls.password='lbanktest1'
        # cls.comm = Common(configfile)
        # cls.input = cls.comm.getInputData(testCaseFile,sheet)
        # cls.expResult = cls.comm.getExpResult(testCaseFile, sheet)
        # cls.urls = cls.comm.getUrls(testCaseFile,sheet)
        # cls.methods = cls.comm.getMethods(testCaseFile,sheet)
        # # cls.log = LoginF(configfile)
        # # cls.token = cls.log.getToken(cls.user,cls.password)
        # cls.exeHttp=ExecHttpF(configfile)
        # cls.testresult =TestResult()
        # cls.station=cls.comm.getWebStation()

    @classmethod
    def tearDownClass(cls):
        print("class tear down {}".format(cls.__name__))
        pass

    def setUp(self):
        print("run the {}".format(self._testMethodName))

    def tearDown(self):
        # if self.result:
        #     print("the actual test result is {}".format(self.result))

        print("teardown {}".format(self._testMethodName))

    @pytest.mark.regression
    @allure.feature("AW")
    @allure.story("001")
    def test_AW_001(self):
        '''bind mobile successfully without 2FA'''
        s = self._testMethodName


    def test_AW_002(self):
        '''bind mobile successfully without 2FA'''
        s = self._testMethodName


