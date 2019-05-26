# -*- coding:utf-8 -*-
from utils.data.manager.json.info_provider import SkillInfoProvider
from utils.data.manager.mongo.manager import Manager
from utils.data.manager.mongo.provider import Provider


class SkillProvider(Provider):
    def __init__(self):
        skill_info = SkillInfoProvider()
        manager = Manager(db_name=skill_info.db_name, tab_name=skill_info.tab_name)
        Provider.__init__(self, manager)
        self.label = skill_info.label
        self.no_use_label = skill_info.no_use_label

    def to_excel(self, filename=None, data=None):
        if filename is None:
            filename = 'skill_data'
        self._to_excel(filename, data)

    def get_project(self, no=1, name=1, sort_major=1, sort_secondary=1, sort_language=1, sort_level=1):
        return {'_id': 0, 'no': no, 'name': name, 'sort_major': sort_major,
                'sort_secondary': sort_secondary, 'sort_language': sort_language, 'sort_level': sort_level}
