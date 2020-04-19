# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/19 15:51
# @FileNAme : argsAndKwargs.py
# @Blog     : http://www.pr1s0n.com
import time
def index(w,x,y,z):
    time.sleep(2)
    print('index %s %s %s %s' % (w,x,y,z))

def wrapper(*args,**kwargs):
    start = time.time()
    index(*args,**kwargs)
    stop = time.time()
    print(stop - start)
wrapper(111,222,333,444)