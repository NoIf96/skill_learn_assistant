# -*- coding:utf-8 -*-
from utils.data.manager.json.info_provider import OccupationInfoProvider
from utils.data.manager.xml.constant import XML_PATH, XML
from utils.data.manager.xml.manager import Manager
from utils.data.manager.xml.provider import Provider


class OccupationProvider(Provider):
    def __init__(self):
        info = OccupationInfoProvider()
        manager = Manager(info.tab_name, info.label, XML_PATH.format(xml_name=XML.get("OCCUPATION")))
        Provider.__init__(self, manager, info)

