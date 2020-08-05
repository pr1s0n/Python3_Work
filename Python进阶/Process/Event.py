# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/5 22:29
# @FileNAme : Event.py
# @Blog     : http://www.pr1s0n.com

from threading import Thread, Event
import time
event = Event()

def light():
    print('红灯亮了')
    time.sleep(3)
    print('绿灯亮了')
    event.set()

def car(name):
    print('%s 车正在等红灯...' %name)
    event.wait()
    print('%s 车起飞，芜湖~\n' %name)

if __name__ == '__main__':
    t = Thread(target=light)
    t.start()
    for i in range(20):
        t = Thread(target=car, args=('%s' %i, ))
        t.start()
