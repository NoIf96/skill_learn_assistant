# -*- coding:utf-8 -*-
from utils.data.manager.json.constant import CONVERT_JSON_PATH, CONVERT_JSON
from utils.data.manager.json.manager import Manager
from utils.data.manager.json.provider import Provider


class ConvertProvider(Provider):
    def __init__(self, json_name):
        manager = Manager(CONVERT_JSON_PATH.format(json_name=json_name))
        Provider.__init__(self, manager)


class ModelParamConvertProvider(ConvertProvider):
    def __init__(self):
        ConvertProvider.__init__(self, CONVERT_JSON.get("MODEL_PARAM_CONVERT"))

    @property
    def kmeans(self):
        return self.get_key_value(self.json_data, "kmeans")

    @property
    def knn(self):
        return self.get_key_value(self.json_data, "knn")


class SortConvertProvider(ConvertProvider):
    def __init__(self):
        ConvertProvider.__init__(self, CONVERT_JSON.get("SORT_CONVERT"))

    @property
    def sort_major(self):
        return self.get_key_value(self.json_data, "sort_major")

    @property
    def sort_secondary(self):
        return self.get_key_value(self.json_data, "sort_secondary")

    @property
    def sort_language(self):
        return self.get_key_value(self.json_data, "sort_language")


class PermissionConvertProvider(ConvertProvider):
    def __init__(self):
        ConvertProvider.__init__(self, CONVERT_JSON.get("PERMISSION_CONVERT"))

    @property
    def permission(self):
        return self.get_key_value(self.json_data, "permission")

