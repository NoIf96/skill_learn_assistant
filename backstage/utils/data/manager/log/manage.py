# -*- coding:utf-8 -*-
import os
import logging
from utils.data.manager.log.constant import LOG_BASE_PATH


class Manage(object):
    def __init__(self, logger_name):
        self.__logger = logging.getLogger(logger_name)

    def set_handler(self, file_name, lever=logging.DEBUG, formatter=None):
        handler = logging.FileHandler(filename=os.path.join(LOG_BASE_PATH, file_name), encoding='utf-8')
        if formatter is None:
            formatter = logging.Formatter(
                '\n\n%(asctime)apis - %(name)apis:%(levelname)apis - %(pathname)apis: 第%(lineno)s行 - 方法名:%(funcName)apis'
                '  错误信息: %(message)apis')
        handler.setFormatter(formatter)
        handler.setLevel(lever)
        self.__logger.addHandler(handler)
        handler2 = logging.StreamHandler()
        handler2.setFormatter(formatter)
        handler2.setLevel(lever)
        self.__logger.addHandler(handler2)

    @staticmethod
    def get_handler(file_name, lever=logging.DEBUG):
        handler = logging.FileHandler(filename=os.path.join(LOG_BASE_PATH, file_name), encoding='utf-8')
        formatter = logging.Formatter(
            '\n\n%(asctime)apis - %(name)apis:%(levelname)apis - %(pathname)apis: 第%(lineno)s行 - 方法名:%(funcName)apis'
            '  错误信息: %(message)apis')
        handler.setFormatter(formatter)
        handler.setLevel(lever)
        return handler

    @property
    def logger(self):
        return self.__logger
