# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/3 21:26
# @FileNAme : 守护进程.py
# @Blog     : http://www.pr1s0n.com
from threading import Thread
import time
import os
def task(name):
    print('%s is running ' % name)
    time.sleep(1)
    print('%s is over ' % name)

def test():
    time.sleep(3)
    print('over')

if __name__ == '__main__':
    t = Thread(target=task,args=('lichang',))
    test = Thread(target=test)

    t.daemon = True # 开启守护线程
    t.start()
    test.start()
    print('主')
'''
主线程运行结束之后程序不会立刻结束，会等待所有其他非守护进程结束之后才会结束
因为主线程的结束意味着所在的进程的结束
'''