# -*- coding:utf-8 -*-
import json
from utils.data.manager.json import logger


class Manager(object):
    def __init__(self, path):
        self.__path = path

    def read_json(self):
        try:
            with open(self.__path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception:
            logger.error(f"root 读取json数据失败， 读取路径为{self.__path}")
            raise

    def write_json(self, data):
        try:
            with open(self.__path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception:
            logger.error(f"root 写入json数据失败， 写入路径为{self.__path}")
            raise

