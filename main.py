# -*- coding: utf-8 -*-
# @Author  : leizi
import os, time, unittest, datetime
from Case.ceshiyongli import Testinface

'''
这里你可以分开执行上面你case里面包含的用例。也可以单独执行里面
的某一个的测试用例
'''
from Public.py_Html import createHtml
from Interface import emmail
import time

if __name__ == '__main__':
    print('----------开始测试----------')
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(Testinface("testinterface"))

    me = Testinface()

    list_fail, \
    list_pass, \
    list_json, \
    listurls, \
    listkeys, \
    listconeents, \
    listfangshis, \
    listqiwangs, \
    listids, \
    listrelust, \
    listnames \
        = me.testinterface()

    filepath = r'./report/relult.html'

    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
        # f = open(filepath, 'w')
        # f.close()

    endtime = datetime.datetime.now()

    createHtml(titles='白菜的测试报告',
               filepath=filepath,
               starttime=starttime,
               endtime=endtime,
               passge=list_pass,
               fail=list_fail,
               id=listids,
               name=listnames,
               key=listkeys,
               coneent=listconeents,
               url=listurls,
               meth=listfangshis,
               yuqi=listqiwangs,
               json=list_json,
               relusts=listrelust)

    print('----------测试成功----------')
    project_path = r'/Users/baicai/mytest/jiekou-python3/report/relult.html'
    emmail.sendemali(project_path)
