# -*- coding:utf-8 -*-
from test_case import *


# 用例文件列表
def caselist():
    alltestnames = [
        baidutest.Baidu,
        youdao.Youdao
    ]

    print("success read case list!!")

    return alltestnames
