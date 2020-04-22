# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/4/22 22:19
# @FileNAme : argsDecorator.py
# @Blog     : http://www.pr1s0n.com
# 有参装饰器实例
def auth(db_type):
    def outter(func):
        def wrapper(*args,**kwargs):
            name = input('your name ->> ').strip()
            password = input('your password >>>:').strip()
            if db_type == 'file':
                print('基于文件的验证')
                if name == 'pr1s0n' and password == 'admin':
                    print('验证成功')
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('you are wrong.')
            elif db_type == 'mysql':
                print('基于数据库验证')
            elif  db_type == 'ldap':
                print('基于ldap验证')
        return wrapper
    return outter

@auth(db_type='file') # @outter -> index=outter(index) -> index=wrapper
def index(x,y):
    print('index->>%s %s' % (x,y))
@auth(db_type='mysql') # @outter -> home=outter(index) -> home=wrapper
def home(name):
    print('home->>%s' % name)
@auth(db_type='ldap') # @outter -> transfer=outter(index) -> transfer=wrapper
def transfer():
    print('transfer')

index(1,2)
home('pr1s0n')
transfer()

