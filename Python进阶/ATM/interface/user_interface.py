# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:57
# @FileNAme : user_interface.py
# @Blog     : http://www.pr1s0n.com
from db import db_handler

def register_interface(username,password,balance=15000):
    user_dic = {
        'username': username,
        'password': password,
        'banlance': balance,
        'flow': [],
        'shop_car':{},
        'locked':False
    }
    db_handler.save(user_dic)
    return True, f'{username} 注册成功！'



def login_interface():
    pass

