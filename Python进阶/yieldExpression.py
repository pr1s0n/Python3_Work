# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/23 21:31
# @FileNAme : yieldExpression.py
# @Blog     : http://www.pr1s0n.com

# yield表达式
def dog(name):
    print('The dog %s want to eat.' % name)
    while True:
        x = yield # 先把收到的值赋值给x,yield后是有返回值的
        print('The dog %s ate %s' %(name,x))

g = dog('tom')
g.send(None) #等同于next(g)
g.send('brade')
g.send('apple')
g.close() #关闭后无法再传值
