# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 10:25
# @FileNAme : src.py
# @Blog     : http://www.pr1s0n.com

from interface import user_interface
from lib import common
from interface import bank_interface
from interface import shop_interface
login_user = None
#
# 1. 注册功能
def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        if password == re_password:
            flag,msg = user_interface.register_interface(
                username,password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)

# 2. 登录功能
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        flag,msg = user_interface.login_interface(
            username,password
        )

        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)

# 3. 查看余额
@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(
        login_user
    )
    print(f'用户{login_user} 账户余额为 {balance}')



# 4. 提现功能
@common.login_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额：').strip()
        if not input_money.isdigit():
            print('必须输入数值！')
            continue
        input_money = int(input_money)
        flag,msg = bank_interface.withdraw_interface(
            login_user,input_money
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 5. 还款功能
@common.login_auth
def repay():
    while True:
        input_money = input('请输入需要还款的金额：').strip()
        if not input_money.isdigit():
            print('请输入正确的金额！')
            continue
        input_money = int(input_money)
        if input_money >0:
            # 调用还款接口
            flag,msg = bank_interface.repay_interface(
                login_user,input_money
            )
            if flag:
                print(msg)
                break
        else:
            print('输入的金额不能小于0!')


# 6. 转账功能
@common.login_auth
def transfer():
    while True:
        to_user = input('请输入目标账户：').strip()
        money = input('请输入转账金额：').strip()
        if not money.isdigit():
            print('请输入正确的金额！')
            continue
        money = int(money)

        if money >0 :
            flag,msg = bank_interface.transfer_interface(
                login_user,to_user,money
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('转账金额不能小于零！')

# 7. 查看流水
@common.login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(login_user)
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('当前用户还没有流水信息！')
# 8. 购物功能
@common.login_auth
def shopping():
    shop_list = [
        ['oppo v480',3899],
        ['vivo X200',3999],
        ['iphone 123', 99999],
        ['xiaomi 100',10000],
    ]
    shopping_car = {} # 初始化购物车,格式为{'商品名称':['单价','数量']}
    while True:
        for index,shop in enumerate(shop_list):
            shop_name ,shop_price = shop
            print(f'商品编号为：{index}',
                  f'商品名称：{shop_name}',
                  f'商品价格：{shop_price}'
            )
        choice = input('请输入商品编号：(输入y or n选择是否结账)').strip()
        # 输入y进入支付
        if choice == 'y':
            if not shopping_car:
                print('购物车是空的，请选择至少一个商品进行支付！')
                continue
            flag,msg = shop_interface.shopping_interface(login_user,shopping_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        # 输入n添加商品到购物车
        elif choice == 'n':
            if not shopping_car:
                print('请至少选择一个商品！')
                continue
            flag,msg = shop_interface.add_shop_car_interface(
                login_user,shopping_car
            )
            if flag:
                print(msg)
                break


        if not choice.isdigit():
            print('请输入正确的商品编号！')
            continue
        choice = int(choice)
        if choice not in range(len(shop_list)):
            print('未找到您搜索的商品的编号，请重新输入！')
            continue

        shop_name ,shop_price = shop_list[choice]
        if shop_name in shopping_car:
            shopping_car[shop_name][1] += 1
        else:
            shopping_car[shop_name] = [shop_price,1]


        print('当前购物车：',shopping_car)

# 9. 查看购物车
@common.login_auth
def check_shop_car():
    order = shop_interface.show_shop_car_interface(login_user)
    print(order)

# 10.管理员功能
# 另外新建了入口文件


# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
}

# 视图层主程序
def run():
    while True:
        print(
            '''
            1. 注册功能
            2. 登录功能
            3. 查看余额
            4. 提现功能
            5. 还款功能
            6. 转账功能
            7. 查看流水
            8. 购物功能
            9. 查看购物车
            '''
        )
        choice = input('请输入功能编号：').strip()
        if choice not in func_dic:
            print('请输入正确的编号！')
            continue
        func_dic.get(choice)()






