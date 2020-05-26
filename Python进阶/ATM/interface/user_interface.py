# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:57
# @FileNAme : user_interface.py
# @Blog     : http://www.pr1s0n.com
from db import db_handler
from lib import common
user_logger = common.get_logger('user')
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
    msg = f'{username} 注册成功！'
    user_logger.info(msg)
    return True, msg

def login_interface(username,password):
    # 1. 判断用户是否存在
    user_dic = db_handler.select(username)

    if user_dic:
        if user_dic['locked'] == False:
            password = common.get_pwd_md5(password)
            if password == user_dic.get('password'):
                msg = f'用户[{username}]登录成功！'
                user_logger.info(msg)
                return True,msg
            else:
                msg = '用户名或密码错误！'
                user_logger.warn(msg)
                return False,msg
        else:
            return False,'该用户已锁定，请联系管理员！'
    return False,'用户不存在，请重新输入！'

def admin_login_interface(username,password):
    user_dic = db_handler.select(username)
    try:
        if user_dic:
            password = common.get_pwd_md5(password)
            if user_dic['is_admin']:
                if password == user_dic.get('password'):
                    msg = f'管理员[{username}]登录成功！'
                    user_logger.info(msg)
                    return True, msg
                else:
                    msg = '用户名或密码错误！'
                    user_logger.warn(msg)
                    return False, msg
    except KeyError:
        return False, '该用户不是管理员！请重新输入'
    return False,'用户不存在，请重新输入！'

def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']

# 锁定账号

def lock_users_interface(username):
    user_dic = db_handler.select(username)
    user_dic['locked'] = True
    db_handler.save(user_dic)

    return user_dic['locked']
