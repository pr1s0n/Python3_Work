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

# print(USER_DATA_PATH)

# 定义三种日志输出格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s' # 其中name为getlogger指定的名字
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式
logfile_dir = os.path.join(BASE_PATH,'log')
# 日志文件名
logfile_name = 'atm.log'
# b不存在则创建日志目录
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

logfile_path = os.path.join(logfile_dir,logfile_name)

LOGGING_DIC = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format
        },
        'simple':{
            'format':simple_format
        },
    },
    'filters':{},
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'simple'
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler', # 保存到文件
            'formatter':'standard',
            'filename':logfile_path, # 日志文件
            'maxBytes':1024 * 1024 * 5, # 日志文件大小
            'backupCount':5,
            'encoding':'utf-8'
        },

    },
    'loggers':{
        # logging.getLogger(__name__)拿到的logger配置
        '':{
            'handlers':['default','console'], # 这里把上面定义的两个handler都加上，即log数据写入文件同时又打印到屏幕上
            'level':'DEBUG',
            'propagate':True,# 向上(更高级别的日志)传递
        },
    },


}