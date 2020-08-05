# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/8 19:54
# @FileNAme : 序列化和反序列化.py
# @Blog     : http://www.pr1s0n.com

# 序列化

# import json
# json_res = json.dumps([1,'aaa',True,False])
# with open('test.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)



# 反序列化
import json
with open('test.json',mode='rt',encoding='utf-8') as f:
    json_res = f.read()
    l = json.loads(json_res)
    print(l,type(l))