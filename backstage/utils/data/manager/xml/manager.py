# -*- coding:utf-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
from utils.data.manager.xml import logger
from utils.data.manager.mongo.manager import Manager as MongoManager


class Manager(object):
    def __init__(self, xml_name, xml_label, path=None):
        self.__xml_name = xml_name
        self.__xml_label = xml_label
        self.__path = path

    def read_xml(self, path=None):
        try:
            if path is None:
                path = self.__path

            if path is None:
                logger.error("root 无法读取空路径")
                return False
            dom_tree = xml.dom.minidom.parse(self.__path)  # 加载xml文件
            collection = dom_tree.documentElement  # 解析xml树
            xml_data = collection.getElementsByTagName(self.__xml_name)  # 获取结点xml列表

            datas = []  # 创建列表用于存储数据

            # 解析加载技能数据
            for xml_item in xml_data:
                data = []
                for label in self.__xml_label:
                    if xml_item.getElementsByTagName(label).length != 1:
                        item = [
                            item.childNodes[0].data
                            for item in xml_item.getElementsByTagName(label)
                        ]
                    else:
                        item = (
                            xml_item.getElementsByTagName(label)[0].childNodes[0].data
                        )
                    data.append(item)
                datas.append(data)
            return pd.DataFrame(datas, columns=self.__xml_label)
        except Exception:
            logger.error(f"root 读取xml文件失败， 读取路径为{self.__path}")
            raise

    def write_xml(self, data, path=None):
        try:
            if path is None:
                path = self.__path

            if path is None:
                logger.error("root 无法写入空路径")
                return False

            dom = xml.dom.minidom.Document()
            root_node = dom.createElement(f"{self.__xml_name}s")
            for item in data.values:
                item_node = dom.createElement(self.__xml_name)
                for i, label in enumerate(self.__xml_label):
                    node = dom.createElement(label)
                    text_node = dom.createTextNode(str(item[i]))
                    node.appendChild(text_node)
                    item_node.appendChild(node)
                root_node.appendChild(item_node)

            dom.appendChild(root_node)

            with open(path, "w", encoding="utf-8") as f:
                dom.writexml(f, indent="", addindent="\t", newl="\n", encoding="utf-8")

        except Exception:
            logger.error(f"root 写入xml文件失败， 写入路径为{self.__path}")
            raise

    def to_mongo(self, db_name, data):
        mongo_manager = MongoManager(db_name=db_name, tab_name=self.__xml_name)
        for data_i in data.values:
            data = {}
            for i, label in enumerate(self.__xml_label):
                data[label] = data_i[i]
            mongo_manager.insert_one(data)
