# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/26 16:49
# @FileNAme : resursionFunc.py
# @Blog     : http://www.pr1s0n.com
# 递归函数的应用

nums = [1,[2,[3,[4,[5,[6,[7,8,9]]]]]]]

def recFunc(list1):
    for x in list1:
        if type(x) is list:
            recFunc(x)
        else:
            print(x)
            
recFunc(nums)

