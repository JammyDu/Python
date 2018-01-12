# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
           :param logger
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d')
        # TODO:
        # 1. 这里的目录名称也相当于用绝对路径了，不合适
        # 2. 拼接路径尽量用`os.path.join`方法
        # log_path =os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\Logs'
        log_filepath = os.path.abspath(os.path.join(os.getcwd(), '..\\logs'))
        print(log_filepath)

        log_filename = rq + '.log'
        log_filename = os.path.join(log_filepath, log_filename)
        fh = logging.FileHandler(log_filename)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    @staticmethod
    def getlog(log_name):
        return Logger(log_name).logger
