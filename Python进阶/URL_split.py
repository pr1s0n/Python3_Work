# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/7/2 22:06
# @FileNAme : URL_split.py
# @Blog     : http://www.pr1s0n.com
from urllib.parse import parse_qs

my_values = parse_qs('red=2&green=lv&blue',keep_blank_values=True)
red = my_values.get
print(repr(my_values))
