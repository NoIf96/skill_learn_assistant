# -*- coding:utf-8 -*-
from utils.data.manager.json.convert_provider import PermissionConvertProvider
from apis.skill_learn_assistant.admin import admin_bp, logger
from utils.api.blue_route import BlueRoute

SUPER_ADMINISTRATOR = '1'
ORDINARY_ADMINISTRATOR = '2'

user_br = BlueRoute(admin_bp, '/user')


def get_permission_convert():
    provider = PermissionConvertProvider()
    return provider.json_data


from apis.skill_learn_assistant.admin.user import admin_api, ordinary_api
