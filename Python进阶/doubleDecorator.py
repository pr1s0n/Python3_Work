# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/23 17:39
# @FileNAme : doubleDecorator.py
# @Blog     : http://www.pr1s0n.com

def deco1(func1):
    def wrapper1(*args,**kwargs):
        print('正在运行==>deco1.wrapper1')
        res = func1(*args,**kwargs)
        return res
    return wrapper1

def deco2(func2):
    def wrapper2(*args,**kwargs):
        print('正在运行==>deco2.wrapper2')
        res = func2(*args,**kwargs)
        return res
    return wrapper2

def deco3(x):
    def outter(func3):
        def wrapper3(*args,**kwargs):
            print('正在运行==>deco3.outter.wrapper3')
            res = func3(*args,**kwargs)
            return res
        return wrapper3
    return outter

@deco1          # ==> index=deco1(wrapper2的内存地址)    -> index == wrapper1的内存地址
@deco2          # ==> index=deco2(wrapper3的内存地址)    -> index == wrapper2的内存地址
@deco3(1)       # ==> @outter -> index=outter(index)    -> index == wrapper3的内存地址
def index(x,y):
    print('index %s%s' %(x,y))
index(1,2)

'''
加载顺序：自下而上
执行顺序：自上而下
'''