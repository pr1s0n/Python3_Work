# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/8/5 23:17
# @FileNAme : server.py
# @Blog     : http://www.pr1s0n.com
import socket
from threading import Thread

def communication(conn):
    while True:
        try:

            data = conn.recv(1024)
            print(data)
            if len(data) == 0:break
            conn.send(data.upper())

        except ConnectionResetError as e:
            print(e)
            break
    conn.close()


def server(ip,port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        t = Thread(target=communication, args=(conn, ))
        t.start()


if __name__ == '__main__':
    s = Thread(target=server,args=('127.0.0.1', 8080))
    s.start()
