# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/16 20:33
# @FileNAme : insertFunction.py
# @Blog     : http://www.pr1s0n.com
# 函数的嵌套

def max2(x,y):
    if x > y:
        return x
    else:
        return y
def max4(a,b,c,d):
    res1 = max2(a,b)
    res2 = max2(res1,c)
    res3 = max2(res2,d)
    return res3
res = max4(1,2,3,4)
print(res)