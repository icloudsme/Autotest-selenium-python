# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import time
# 导入测试模块
# 使用这个方法，只需要在执行的all_tests中写入from test_case import *就可以
# from test_case import *
# from test_case import baidutest
# import allcase_list

list_case = "C:\\Users\\PCPC\\pyobject\\test_case\\test_case"


def creatsuitel():
    testunit = unittest.TestSuite()
    # discover方法定义
    discover = unittest.defaultTestLoader.discover(list_case,
                                                   pattern='start_*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit


alltestnames = creatsuitel()

# 创建测试套件
# testunit = unittest.TestSuite()
# 获取数组方法

'''
# 将用例组装数组
alltestnames =[
    baidutest.Baidu,
    youdao.Youdao
]
'''
# 循环读取数组中的用例
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))

# testunit.addTest(unittest.makeSuite(baidutest.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

# 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)
# 取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
filename = "E:\\" + now + 'result1.html'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：'
)

# 执行测试用例
runner.run(alltestnames)
