# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/22 23:16
# @FileNAme : admin.py
# @Blog     : http://www.pr1s0n.com
from lib import common
from interface import user_interface
from interface import bank_interface
from core import src
admin_key = None
def admin_login():
    while True:
        username = input('请输入管理员账号：').strip()
        password = input('请输入管理员密码：').strip()

        flag,msg = user_interface.admin_login_interface(
            username,password
        )
        if flag:
            print(msg)
            global admin_key
            admin_key = username
            break

        else:
            print(msg)

# 添加账户
@common.login_admin
def add_users():
    src.register()

# 修改用户额度
@common.login_admin
def change_balance():
    username = input('请输入要操作的用户名：').strip()
    money = input('请输入修改的额度：').strip()
    if not money.isdigit():
        print('额度必须为数值！')
        change_balance()
    else:
        balance = bank_interface.change_balance_interface(username,money)

        print(f'用户[{username}]额度修改成功，当前额度为[{balance}]元！')


@common.login_admin
def lock_user():
    username = input('请输入要锁定的账户名：').strip()
    lock_status = user_interface.lock_users_interface(username)
    if lock_status:
        print(f'用户[{username}]已被锁定！')
    else:
        print(f'用户[{username}]锁定失败，请重试！')
        lock_user()

admin_func = {
    '1': admin_login,
    '2': add_users,
    '3': change_balance,
    '4': lock_user,
}

def run():
    while True:
        print(
            '''
            1. 管理登录
            2. 添加账户
            3. 修改额度
            4. 冻结账户
            '''
        )
        choice = input('请输入管理员功能编号：').strip()
        if choice not in admin_func:
            print('请输入正确的编号！')
            continue
        admin_func.get(choice)()
