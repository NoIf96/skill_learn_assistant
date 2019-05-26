# -*- coding:utf-8 -*-


class Provider(object):
    def __init__(self, manager, info):
        self.__manager = manager
        self.__xml_data = None
        self.__info = info

    @property
    def xml_data(self):
        if self.__xml_data is None:
            self.__xml_data = self.read_xml()
        return self.__xml_data

    def read_xml(self, path=None):
        return self.__manager.read_xml(path)

    def write_xml(self, data, path=None):
        self.__manager.write_xml(data, path)

    def to_mongo(self, db_name=None, data=None):
        if db_name is None:
            db_name = self.__info.db_name
        if data is None:
            data = self.read_xml()
        self.__manager.to_mongo(db_name, data)
