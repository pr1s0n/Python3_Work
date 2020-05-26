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
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式
logfile_dir = os.path.join(BASE_PATH,'log')

logfile_name = 'atm.log'

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
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'standard',
            'filename':logfile_path,
            'maxBytes':1024 * 1024 * 5,
            'backupCount':5,
            'encoding':'utf-8'
        },

    },
    'loggers':{
        '':{
            'handlers':['default','console'],
            'level':'DEBUG',
            'propagate':True,
        },
    },


}