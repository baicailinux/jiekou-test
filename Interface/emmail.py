# -*- coding: utf-8 -*-
# @Author  : leizi
import smtplib, time, os, re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def load_emil_setting():  # 从配置文件中加载获取email的相关信息
    import yaml
    # data_file = open(r"./Data/email.yaml", "r")
    data_file = open(r"F:\jiekou-test\Data\email.yaml", "r")
    datas = yaml.load(data_file)
    data_file.close()
    return (
        datas['foremail'],
        datas['password'],
        datas['toeamil'],
        datas['title']
    )


def sendemali(filepath):  # 发送email
    from_addr, password, mail_to, mail_body = load_emil_setting()
    msg = MIMEMultipart()
    msg['Subject'] = '白菜接口自动化'
    msg['From'] = '白菜接口自动化测试平台'
    msg['To'] = mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    att = MIMEText(open(r'%s' % filepath[0], 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    if filepath[1] == '.xls':
        att["Content-Disposition"] = 'attachment; filename="result.xls"'
    else:
        att["Content-Disposition"] = 'attachment; filename="result.html"'
    txt = MIMEText("这是测试报告的邮件，详情见附件", 'plain', 'gb2312')
    msg.attach(txt)
    msg.attach(att)
    smtp = smtplib.SMTP()
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, mail_to, msg.as_string())
    server.quit()


if __name__ == '__main__':
    # project_path = r'..\report\pyresult.html'
    project_path = r'/Users/baicai/mytest/jiekou-python3/report/relult.html'
    sendemali(project_path)
