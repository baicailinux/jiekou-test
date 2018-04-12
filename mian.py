# encoding: UTF-8
import re
from main import create_Xls
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = re.search('hello','world!hello')

if match:
    # 使用Match获得分组信息
    print('ok')
    print(match.group())

create_Xls()