# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 11:00
# @FileNAme : time.py.py
# @Blog     : http://www.pr1s0n.com

# time模块

import time

print(time.asctime())
# 按格式显示时间
print(time.time())
print(time.strftime('%Y-%m-%d'))

# 结构化的时间
res = time.localtime()
print(res)
print(res.tm_year)
print(res.tm_hour)


# datetime 模块
import datetime
res = datetime.datetime.now()
print(res)
