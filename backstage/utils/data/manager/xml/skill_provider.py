# -*- coding:utf-8 -*-
from utils.data.manager.json.info_provider import SkillInfoProvider
from utils.data.manager.xml.constant import XML_PATH, XML
from utils.data.manager.xml.manager import Manager
from utils.data.manager.xml.provider import Provider


class SkillProvider(Provider):
    def __init__(self):
        info = SkillInfoProvider()
        manager = Manager(info.tab_name, info.label, XML_PATH.format(xml_name=XML.get("SKILL")))
        Provider.__init__(self, manager, info)
