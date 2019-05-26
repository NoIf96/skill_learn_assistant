# -*- coding:utf-8 -*-
import pymongo
import pandas as pd
from utils.data.manager.mongo import logger
from utils.data.manager.mongo.constant import *


class Manager(object):
    def __init__(
        self,
        client_host=CLIENT_DEVELOPMENT_HOST,
        client_port=CLIENT_PORT,
        user_name=USER_NAME,
        user_pw=USER_PW,
        db_name="",
        tab_name="",
    ):
        # client_url = f'mongodb://{user_name}:{user_pw}@{client_host}:{client_port}/'
        client_url = f"mongodb://{client_host}:{client_port}/"
        self.client = self.__get_clinet(client_url)
        self.db = self.client[db_name]
        self.tab = self.db[tab_name]

    def __get_clinet(self, client_url):
        try:
            return pymongo.MongoClient(client_url)
        except Exception:
            logger.error(f"root 与mongodb连接出错， 连接url为: {client_url}")
            raise

    def query(self, find_query, project, label):
        try:
            items = self.tab.find(find_query, project)
            data = pd.DataFrame(list(items), columns=label)
            data = data.apply(pd.to_numeric, errors="ignore")
            return data
        except Exception:
            logger.error(f"root 查询错误， 语句{find_query}")
            raise

    def query_all(self, project, label):
        try:
            item = self.tab.find({}, project)
            data = pd.DataFrame(list(item), columns=label)
            data = data.apply(pd.to_numeric, errors="ignore")
            return data
        except Exception:
            logger.error(f"root 查询全部数据错误")
            raise

    def insert_one(self, data):
        try:
            self.tab.insert(data)
        except Exception:
            logger.error(f"root 插入数据错误 数据如下：{data}")
            raise

    def insert_many(self, datas):
        try:
            self.tab.insert_many(datas)
        except Exception:
            logger.error(f"root 插入数据错误 数据如下：{datas}")
            raise

    def close(self):
        self.client.close()

