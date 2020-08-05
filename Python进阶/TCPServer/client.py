# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/5 23:17
# @FileNAme : client.py
# @Blog     : http://www.pr1s0n.com
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))
while True:
    client.send(b'hello,world!')
    data = client.recv(1024)
    print(data)