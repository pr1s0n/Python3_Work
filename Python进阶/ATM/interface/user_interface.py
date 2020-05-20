# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:57
# @FileNAme : user_interface.py
# @Blog     : http://www.pr1s0n.com
from db import db_handler
from lib import common
def register_interface(username,password,balance=15000):
    password = common.get_pwd_md5(password)
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car':{},
        'locked':False
    }
    db_handler.save(user_dic)
    return True, f'{username} 注册成功！'

def login_interface(username,password):
    # 1. 判断用户是否存在
    user_dic = db_handler.select(username)

    if user_dic:
        password = common.get_pwd_md5(password)
        if password == user_dic.get('password'):
            return True,f'用户[{username}]登录成功！'
        else:
            return False,'用户名或密码错误！'

    return False,'用户不存在，请重新输入！'

def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']
