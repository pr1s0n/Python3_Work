# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/3 21:42
# @FileNAme : 线程互斥锁.py
# @Blog     : http://www.pr1s0n.com
from threading import Thread, Lock
import time
money = 100
mutex = Lock()
def task():
    global money
    mutex.acquire()
    tmp = money
    time.sleep(0.1)
    money = tmp - 1
    mutex.release()

if __name__ == '__main__':
    # mutex = Lock()

    t_list = []

    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print(money)

'''数据错乱，加锁处理'''
