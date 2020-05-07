# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/3 16:49
# @FileNAme : lambda.py
# @Blog     : http://www.pr1s0n.com


# 匿名函数
# 临时调用一次，用后即焚
count = {
    'lihua':123,
    'lili':122,
    'wangmeimei':1444,
    'tony':999
}

# def f(k):
#     return count[k]
'''
res = max(count,key=lambda k:count[k])
# 同理sorted()同样适用
print(res)
'''
''':arg'''

# map函数
l = ['lichang','song','xue','wang']
res = map(lambda name:name+'_nice',l)
print(res.__next__())

