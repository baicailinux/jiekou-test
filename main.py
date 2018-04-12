# -*- coding: utf-8 -*-
# @Author  : leizi
import os, unittest, datetime
from Case.ceshiyongli import Testinface
from Public.pyreport_excel import create_xls
from Interface.emmail import sendemali
from Public.py_Html import createHtml

'''
这里你可以分开执行上面你case里面包含的用例。也可以单独执行里面
的某一个的测试用例
'''
starttime = datetime.datetime.now()
suite = unittest.TestSuite()
suite.addTest(Testinface("testinterface"))
me = Testinface()
now = str(starttime).split('.')[0].split('\t')[0].split(' ')[0]


def create_Html():
    filepath = './report/' + now + '-relult.html'
    code = filepath.split('relult')[1]
    endtime = datetime.datetime.now()
    if os.path.exists(filepath) is True:
        os.remove(filepath)
    if os.path.exists(filepath) is False:
        f = open(filepath, 'w')
        f.close()

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
    return filepath, code


def create_Xls():
    filepath = './report/' + now + '-relult.xls'
    code = filepath.split('relult')[1]
    if os.path.exists(filepath) is True:
        os.remove(filepath)
    create_xls(filename=filepath,
               list_pass=list_pass,
               list_fail=list_fail,
               listids=listids,
               listnames=listnames,
               listkeys=listkeys,
               listconeents=listconeents,
               listurls=listurls,
               listfangshis=listfangshis,
               listqiwangs=listqiwangs,
               list_json=list_json,
               listrelust=listrelust
               )
    return filepath, code


def send_report(file):
    try:
        print('---------正在发送邮件--------')
        sendemali(file)
        print("---------邮件已发送---------")
    except Exception as e:
        print('发送失败原因:%s' % e)


if __name__ == '__main__':
    print('----------测试开始----------')
    try:
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
    except Exception as e:
        print('测试失败原因:%s' % e)
    # send_report(create_Xls())
    send_report(create_Html())
    print('----------测试结束----------')
