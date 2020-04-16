def login():
    print('login')
def register():
    print('register')
def saveMoney():
    print('SaveMoney')
def withdraw():
    print('WithDraw')

funcDict = {
    '1':login,
    '2':register,
    '3':saveMoney,
    '4':withdraw
}
while True:
    print("""
        请输入指定命令
        0 退出
        1 登录
        2 注册
        3 存款
        4 取款
    """)
    choice = input().strip()
    if not choice.isdigit():
        print('必须输入编号')
        continue
    if choice == '0':
        break
    if choice in funcDict:
        funcDict[choice]()
    else:
        print('输入指令不存在')
