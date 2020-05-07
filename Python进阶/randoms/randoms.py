# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 11:42
# @FileNAme : randoms.py
# @Blog     : http://www.pr1s0n.com
# 随机模块

#import random
# print(random.sample([111,'aaa','bbb'],1))
# print(random.uniform(1,3))
# print(random.gammavariate(12,123))
# item = [1,3,4,5,7]
# random.shuffle(item)
# print(item)
#

# 验证码生成模拟


import random
res = ''
for i in range(6):
    s1 = chr(random.randint(65,90))
    s2 = str(random.randint(0,9))
    res += random.choice([s1,s2])
print(res)