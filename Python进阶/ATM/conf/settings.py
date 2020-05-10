# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/7 10:37
# @FileNAme : settings.py
# @Blog     : http://www.pr1s0n.com
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

USER_DATA_PATH = os.path.join(
    BASE_PATH,'db','user_data'
)

print(USER_DATA_PATH)