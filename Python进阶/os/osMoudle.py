# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 21:42
# @FileNAme : osMoudle.py
# @Blog     : http://www.pr1s0n.com
import os
res = os.environ
cmd = os.system('whoami')
lists = os.listdir('../')
size = os.path.getsize('../../../')
print(os.path.dirname(r'/a/b/c.txt'))
print(os.path.basename(r'/a/b/v.txt'))
print(res)
print(cmd)
print(lists)
print(size)