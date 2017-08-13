# encoding: UTF-8
import os
import logging
import time
import csv

# 全局变量
LOGGING_MSG_FORMAT = '[%(asctime)s] [%(filename)s LINE:%(lineno)d %(levelname)s]:%(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# 开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, log_file_name, log_level, loger_key):
        if not os.path.exists('./logs'):
            os.makedirs('./logs')

        # 创建一个logger
        self.logger = logging.getLogger(loger_key)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        file_handler = logging.FileHandler('logs' + log_file_name)
        file_handler.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(LOGGING_MSG_FORMAT)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    # 获取loger对象
    def getlog(self):
        return self.logger

# 清洗脚本启动，创建日志文件
now_time = time.time()
log_file_name = 'DataWasher' + str(now_time) + '.log'
logger = Logger(log_file_name=log_file_name, log_level=1, loger_key="ROOT").getlog()


# 清洗脚本初始化
def init_data_washer():
    logger.info("DataWasher begin init")
    # 读取表格配置

    logger.info("DataWasher init finish")

# 主循环
def main():
    init_data_washer()
    while True:
        # 获取当前时间

        # 遍历所有任务，检查是否有该时间点需要执行的任务

        # 执行任务
        pass


# Timer（定时器）是Thread的派生类，
# 用于在指定时间后调用一个方法。

main()

