# import sys
# sys.path.append("./util")


import unittest as unit

from util.OutputResult import OutputResult
# from TestCases.TestClearAndSettle import DigitalFeeReport,DepositAndDrawWithTHB,DigitalAssetReporter
from test_front import Test_BindMobile,Test_AW
from TestCases.TestTradeSystem_newkey import TestCreateOrder,TestTransactions
from TestCases.TestWebSocket import SubscribeKey


from util.HTMLTestRunner import HTMLTestRunner


def suite():
    suite = unit.TestSuite()
    loader=unit.TestLoader()
    s1=loader.loadTestsFromTestCase(Test_BindMobile)
    # s1=loader.loadTestsFromTestCase(ACCOMMDATION)
    # s2 = loader.loadTestsFromTestCase(DepositAndDrawWithTHB)
    # s3 = loader.loadTestsFromTestCase(DigitalAssetReporter)
    # case1=loader.loadTestsFromName('TestCases.TestMarketTrades.testDepth_001')
    # case2=loader.loadTestsFromName('TestCases.TestFront.testOrder_008')
    # case3 = loader.loadTestsFromName('TestMobile.TestLogin.testLogin_016')
    # case4 = loader.loadTestsFromName('TestMobile.TestLogin.testLogin_017')
    # case5=loader.loadTestsFromName('TestFront.Advertisement.testAdver_005')
    # s=[s2,s3,s1]
    suite.addTests(s1)
    # case=[case1]
    # suite.addTests(case)

    # suite.addTest("TestCases/TestTradeSystemCases(test_001)")
    # print("suite is {}".format(suite))
    # suite.addTest("TestCases/TestFront/order(test_007)")
    # suite.addTest("TestCases/TestFront/order(test_008")
    return suite

discover = unit.defaultTestLoader.discover('TestCases', pattern='Match*.py')
# print("discover is {}".format(discover))
out=OutputResult()

print("starting to create report file!")

reportfile=out.creatReportFile("html")
print("create report file successfully!")


with open(reportfile,'w') as f:

    runner = HTMLTestRunner(stream=f, title=u'order controller test of WEB', description='Func test of order controller of WEB')
    # runner = unit.TextTestRunner(stream=f,descriptions='Report_description',verbosity=1)

    if __name__ == '__main__':
        # runner.run(discover)

        runner.run(suite())

