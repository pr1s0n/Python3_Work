# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/6/30 22:01
# @FileNAme : processCreate.py
# @Blog     : http://www.pr1s0n.com
from multiprocessing import Process
import time

# 类创建
# class processCreate(Process):
#     def run(self):
#         print('The process is running.')
#         time.sleep(10)
#         print('The process is stoped.')
#
# if __name__ == '__main__':
#     p = processCreate()
#     p.start()
#     print('process.')

# 函数式
def task(name,n):
    print('The Process %s is running.' %name)
    time.sleep(n)
    print('The Process %s is stoped.' %name)
    
if __name__ == '__main__':
    '''
    基本形式
    p = Process(target=task,args = ('lichang',1))
    p1 = Process(target=task,args=('pr1s0n',2))
    p2 = Process(target=task,args=('lanlan',3))
    start_time = time.time()
    p.start()
    p1.start()
    p2.start()

    p.join()
    p1.join()
    p2.join()
    '''

    # for循环中的进程等待实现方法
    start_time = time.time()
    p_list = []
    for i in range(1,4):
        p = Process(target=task,args = (i,i))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()


    print('main',time.time()-start_time)
