# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/7 21:39
# @FileNAme : 进程池与线程池.py
# @Blog     : http://www.pr1s0n.com
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os
pool = ThreadPoolExecutor(5)
'''
船舰一个线程池，并定义初始池中的线程数量为5
这五个线程不会出现重复创建和销毁的过程

'''
# nu = min(32, (os.cpu_count() or 1) + 4)
# print(nu)  # 20

def tesk(n):
    print(f'我是tesk执行的第{n}次\n')
    time.sleep(3)
    return n


# pool.submit(desk, 1)  # 朝池子中提交任务  异步提交
# print('主')
t_list = []
for i in range(20):  # 朝池子中提交20个任务
    res = pool.submit(tesk, i)
    # print(res.result())  # 拿到异步返回的结果  同步提交
    t_list.append(res)
pool.shutdown()
for t in t_list:
    print('>>>>', t.result())