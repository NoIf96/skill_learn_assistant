# -*- coding:utf-8 -*-
from utils.data.manager.json.constant import INFO_JSON_PATH, INFO_JSON
from utils.data.manager.json.manager import Manager
from utils.data.manager.json.provider import Provider


class InfoProvider(Provider):
    def __init__(self, json_name):
        manager = Manager(INFO_JSON_PATH.format(json_name=json_name))
        Provider.__init__(self, manager)

    @property
    def info(self):
        return self.get_key_value(self.json_data, "info")

    @property
    def db_name(self):
        return self.get_key_value(self.info, "db_name")

    @property
    def tab_name(self):
        return self.get_key_value(self.info, "tab_name")

    @property
    def label(self):
        return self.get_key_value(self.info, "label")

    @property
    def no_use_label(self):
        return self.get_key_value(self.info, "no_use_label")


class SkillInfoProvider(InfoProvider):
    def __init__(self):
        InfoProvider.__init__(self, INFO_JSON.get("SKILL_INFO"))


class OccupationInfoProvider(InfoProvider):
    def __init__(self):
        InfoProvider.__init__(self, INFO_JSON.get("OCCUPATION_INFO"))

