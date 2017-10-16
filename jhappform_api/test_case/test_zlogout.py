#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Date:12-10-2017
#Author:jhinno
#Version=.3

import sys
sys.path.append("..")
from tools.get_access_token import * 
from tools.tools import *
import unittest



class TestLogout(unittest.TestCase):
    """测试 appform 注销 case："""

    def setUp(self):
        print("开始测试注销【logout api】 ...")
     

    def actions(self, arg1, arg2):
        data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
        datas = Tools().readi_test_data(data_json)
        self.url = datas['other_param'][0]['baseUrl'] + "logout?token=" + arg1 
        self.result = Tools().access_web(self.url)
        if arg2 == "0":
            self.assertEqual(self.result['result'],'failed', msg = "appform logout case 测试失败！")
        else:
            self.assertEqual(self.result['result'],'success', msg = "appform logout case 测试失败！")


    @staticmethod
    def getTestFunc(arg1, arg2, arg3):
        def func(self):
            self.actions(arg1, arg2)
        return func

    def tearDown(self):
        print("【logout api】 访问的URL地址为：")
        print(self.url)
        print("【logout api】 测试返回值：")
        print(self.result)
        print("【logout api】 测试结束...")


def generateTestCases():
    t = Tools()
    data_json = os.path.join(os.path.abspath('..'), "jhappform_api/test_data/data.json")
    data_case = Tools().readi_test_data(data_json)
    arglists = []
    lenth = len(data_case['logout'][0])
    for i in range(lenth):
        no  = "_no_" + str(i) 
        cse = "case" + str(i + 1)
        tkn = data_case['logout'][0][cse][0]['data']['token']
        ext = str(data_case['logout'][0][cse][0]['data']['expect'])
        arglists.append((tkn, ext, no))
    arglists.append((t.read_token(), 1, "_" + str(lenth)))
    for args in arglists:
        setattr(TestLogout, 'test_logout_{1}_{1}{2}'.format(args[0] , args[1], args[2]), TestLogout.getTestFunc(*args) )


s = generateTestCases()



if __name__ == '__main__':
	unittest.main()

