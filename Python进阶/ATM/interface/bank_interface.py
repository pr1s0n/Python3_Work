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
        # 3. 记录流水
        flow = f'用户 {username} 提现 {money} 成功！手续费 {money2 - money} ,当前余额 {user_dic["balance"]}'
        user_dic['flow'].append(flow)
        # 4. 再保存、更新数据
        db_handler.save(user_dic)
        return True, flow

    return False,'余额不足，提现失败！'

def repay_interface(username,money):
    user_dic = db_handler.select(username)
    user_dic['balance'] += money
    flow = f'用户[{username}]还款[{money}]成功！当前额度为[{user_dic["balance"]}]'
    user_dic['flow'].append(flow)
    db_handler.save(user_dic)
    return True,flow

def transfer_interface(login_user,to_user,money):
    '''
    1. 获取当前用户信息
    2. 获取目标用户数据
    3. 获取转账金额
    :param login_user:当前用户
    :param to_user: 目标用户
    :param money: 转账金额
    :return: bool
    '''
    # 获取当前用户字典
    login_user_dic = db_handler.select(login_user)

    # 获取目标用户字典
    to_user_dic = db_handler.select(to_user)

    #判断目标用户是否存在
    if not to_user_dic:
        return False,'目标用户不存在！'

    # 判断余额是否足够
    if login_user_dic['balance'] >= money:
        # 当前账户减钱
        login_user_dic['balance'] -= money

        # 目标账户加钱
        to_user_dic['balance'] += money

        # 流水记录

        login_user_flow = f'用户[{login_user}]向[{to_user}转账[{money}元]成功！'
        login_user_dic['flow'].append(login_user_flow)
        to_user_flow = f'用户[{to_user}]接收[{login_user}]转账[{money}元]成功！'
        to_user_dic['flow'].append(to_user_flow)
        # 保存两个用户的数据

        db_handler.save(login_user_dic)
        db_handler.save(to_user_dic)
        return True,login_user_flow
    return False,'当前账户余额不足！'

# 查看流水接口
def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('flow')
 
# 修改用户额度
def change_balance_interface(username,money):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False,'用户不存在，请重新输入！'
    user_dic['balance'] = int(money)
    db_handler.save(user_dic)
    return user_dic.get('balance')

def pay_interface(username,cost):
    user_dic = db_handler.select(username)
    if user_dic.get('balance') >= cost:
        user_dic['balance'] -= cost
        flow = f'用户消费金额：[{cost}]'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True

    return False