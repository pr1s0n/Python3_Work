# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:57
# @FileNAme : shop_interface.py
# @Blog     : http://www.pr1s0n.com
'''
购物商城接口
'''
from db import db_handler
# 结算接口
def shopping_interface(username,shopping_car):
    # 1.计算消费总额
    cost = 0
    # 购物车格式{'商品名称':[]}
    for price_number in shopping_car.values():
        price,number = price_number
        cost += (price * number)

    from interface import bank_interface
    flag = bank_interface.pay_interface(username,cost)
    if flag:
        return True,'支付成功，正在准备发货！'
    return False,'支付失败，金额不足'

def add_shop_car_interface(username,shopping_car):
    # 1.获取当前用户的购物车
    user_dic = db_handler.select(username)

    # 2.添加购物车
    # 判断当前用户选择的商品是否存在
    for shop_name,price_number in shopping_car.items():
        # 遍历出商品名称、金额、数量


        number = price_number[1]
        # 判断商品是否已经在用户购物车中，如果存在则数量+1
        if shop_name in user_dic.get('shop_car'):
            user_dic['shop_car'][shop_name] += number
        else:
            user_dic['shop_car'].update(
                {shop_name:price_number}
            )
    db_handler.save(user_dic)

    return True,'添加购物车成功！'

def show_shop_car_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('shop_car')