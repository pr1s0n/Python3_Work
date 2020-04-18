# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/18 11:20
# @FileNAme : clostuefunc.py
# @Blog     : http://www.pr1s0n.com
'''
 闭包函数 = 名称空间与作用域+函数嵌套+函数对象
 核心点：名字的查找关系是以函数定义阶段为准
 
 什么是闭包函数：
    “闭”函数指的该函数是内嵌函数
    “包”函数指的是该函数包含对外层函数作用域名字的引用（不是对全局作用域）。
'''
def f1():
    x = 123123123
    def f2():
        print('函数f2',x)
    return f2
f = f1()
def foo():
    x = 2222
    f()
foo()