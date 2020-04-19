# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/19 17:09
# @FileNAme : grammerSugar.py
# @Blog     : http://www.pr1s0n.com
# import time
# def outter(func):
#     # func = index
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
# @outter # 相当于完成了 index = outter(index)
# def index(w,x,y,z):
#     time.sleep(2)
#     print('index %s %s %s %s' % (w,x,y,z))
#     return w+x+y+z
# @outter # 相当于完成了 home = outter(home)
# def home(name):
#     print('Welcome %s ' %name)
#     time.sleep(1)
#
#
# # index = outter(index)
# print(index(1,2,3,4))
# home('lichang')

# print(index(1,2,3,4))


def war1(func):
    print("war1")
    def inner(*args, **kwargs):
        print("======war1 start=====")
        func(*args, **kwargs)  # inner
        print("======war1 end=====")
    return inner
def war2(func):
    print("war2")
    def inner(*args, **kwargs):
        print("======war2 start=====")
        func(*args, **kwargs)
        print("======war2 end=====")
    return inner

@war1
@war2
def f():
    print("****self****")
f()
# f()相当于 war1(war2(f))()