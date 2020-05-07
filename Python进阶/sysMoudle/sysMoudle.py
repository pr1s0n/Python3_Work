# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 22:22
# @FileNAme : sysMoudle.py
# @Blog     : http://www.pr1s0n.com

# sys模块

# import sys
# res = input(sys.argv)
# print(res)

# 进度条模拟
'''
import time
res = ''
for i in range(50):
    res += '+'
    time.sleep(0.1)
    print('\r[%-50s]' % res,end='')
    # \r代表不换行，每次都从第一个字符开始,-50的意思是从左边开始，宽度50
'''
import time

def progress(precent):
    if precent > 1:
        precent = 1

    res = int(50 * precent) * '#'
    print('\r[%-50s] %d%%' % (res,int(100*precent)),end='')


recv_size = 0
total_size = 10201132
while recv_size < total_size:
    time.sleep(0.001)
    recv_size += 1024
    precent = recv_size / total_size
    progress(precent)