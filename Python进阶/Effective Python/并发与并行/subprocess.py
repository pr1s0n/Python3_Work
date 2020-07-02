# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/7/2 22:26
# @FileNAme : subprocess.py
# @Blog     : http://www.pr1s0n.com
import subprocess
# proc = subprocess.Popen(
#     ['echo','Hello from the child!'],
#     stdout=subprocess.PIPE)
# out, err = proc.communicate()
# print(out.decode('utf-8'))
proc = subprocess.Popen(['sleep','0.3'])
while proc.poll() is None:
    print('Working...')

print('Exit status',proc.poll())