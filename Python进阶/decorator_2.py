# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/21 18:09
# @FileNAme : decorator_2.py
# @Blog     : http://www.pr1s0n.com

# 装饰器模板
#
def outter(func):
    def wrapper(*args,**kwargs):

        #装饰器新增功能区

        name = input('Please input your username:')
        password = input('Please input your password:')
        if name == 'pr1s0n' and password == 'pr1s0n':
            res = func(*args,**kwargs)
            return res
        else:
            print('Sorry,you are wrong.')
    return wrapper
@outter
def index():
    print('Welcome')
index()