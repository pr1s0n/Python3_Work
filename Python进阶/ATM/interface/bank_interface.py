# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:56
# @FileNAme : bank_interface.py
# @Blog     : http://www.pr1s0n.com
from db import db_handler
def withdraw_interface(username,money):
    # 1. 先获取用户字典
    user_dic = db_handler.select(username)
    # 检验金额是否足够
    balance = user_dic.get('balance')
    money2 = money * 1.05
    if balance >= money2:
        # 2. 修改用户字典中的金额
        user_dic['balance'] -= money2
        # 3. 再保存、更新数据
        db_handler.save(user_dic)
        return True, f'用户 {username} 提现 {money} 成功！手续费 {money2 - money} ,当前余额 {user_dic["balance"]}'
    return False,'余额不足，提现失败！'