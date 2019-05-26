# -*- coding:utf-8 -*-
from utils.data.manager.json.convert_provider import SortConvertProvider
from apis.skill_learn_assistant.admin import admin_bp, logger
from utils.api.blue_route import BlueRoute
from utils.worm.baidu_encyclopedia import get_one_introduction

library_br = BlueRoute(admin_bp, '/library')


def get_sort_convert():
    provider = SortConvertProvider()
    return provider.json_data



from apis.skill_learn_assistant.admin.library import skill_api, occupation_api
