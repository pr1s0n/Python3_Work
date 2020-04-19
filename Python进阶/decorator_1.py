# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/19 16:09
# @FileNAme : decorator_1.py
# @Blog     : http://www.pr1s0n.com

# 使用闭包实现装饰器，在不修改被修饰函数的情况下通过外部操作完成功能的添加
import time
def index(w,x,y,z):
    time.sleep(2)
    print('index %s %s %s %s' % (w,x,y,z))
    return w+x+y+z
def outter(func):
    # func = index
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        stop = time.time()
        print(stop - start)
        return res
    return wrapper
index = outter(index)

print(index(1,2,3,4))
# wrapper(111,222,333,444)
