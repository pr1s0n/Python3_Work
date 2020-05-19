# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 10:37
# @FileNAme : common.py
# @Blog     : http://www.pr1s0n.com
'''
存放公共方法
'''
import hashlib
# md5加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '兔子先生'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()

# 登录装饰器

def login_auth(func):
    from core import src
    def inner(*args,**kwargs):
        if src.login_user:
            res = func(*args,**kwargs)
            return res
        else:
            print('用户还没有登录喔！')
            src.login()
            
    return inner
