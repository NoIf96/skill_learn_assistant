# -*- coding:utf-8 -*-
from utils.data.manager.json import logger


class Provider(object):
    def __init__(self, manager):
        self.__manager = manager
        self.__json_data = None

    @property
    def json_data(self):
        if self.__json_data is None:
            self.__json_data = self.read_json()
        return self.__json_data

    def read_json(self):
        return self.__manager.read_json()

    def write_json(self, data):
        self.__manager.write_json(data)

    def get_key_value(self, json_data, key):
        try:
            if json_data:
                return json_data[key]
            return False
        except Exception as e:
            logger.error(f"root {json_data} 不包含键：{key}, {e}")
            raise

    def set_key_value(self, json_data, key, value):
        try:
            json_data[key] = value
        except Exception as e:
            logger.error(f"root {json_data} 赋值失败：{key}, {value}, {e}")
            raise
