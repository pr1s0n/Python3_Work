# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/23 15:21
# @FileNAme : generation.py
# @Blog     : http://www.pr1s0n.com
# 生成器和迭代器
# 如何得到自定义的迭代器：
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象，生成器即自定义的迭代器

def my_range(start,stop,step=1):
    while start < stop:
        yield start
        start += step


for n in my_range(0,155,2):
    print(n)

'''
什么是可迭代对象，什么是迭代器对象
    可迭代对象都有__iter__方法
    迭代器对象既有__iter__也有__next__
    和return不同的是，yield可以多次使用
迭代器优缺点
    优点：
        1. 获得了一种不依赖索引的迭代方案
        2. 惰性计算（能够进行无限次计算但是占用极小内存）
    缺点：
        1. 一次性
for循环原理
    for x in 可迭代对象: # 可迭代对象__iter__() ->迭代器对象 ->next(迭代器对象)
        print(x)
        
如果函数体中有yield，再去调用函数，函数中的代码不会直接执行。只有在函数被调用后执行next才可以被作为生成器执行

'''
