# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/16 20:32
# @FileNAme : functionClass1.py
# @Blog     : http://www.pr1s0n.com

def login():
    print('login')
def register():
    print('register')
def saveMoney():
    print('SaveMoney')
def withdraw():
    print('WithDraw')

funcDict = {
    '0':['退出',None],
    '1':['登录',login],
    '2':['注册',register],
    '3':['存款',saveMoney],
    '4':['取款',withdraw]
}
while True:
    for k in funcDict:
        print(k,funcDict[k][0])
    choice = input('请输入命令编号：').strip()
    if not choice.isdigit():
        print('必须输入编号')
        continue
    if choice == '0':
        break
    if choice in funcDict:
        funcDict[choice][1]()
    else:
        print('输入指令不存在')
