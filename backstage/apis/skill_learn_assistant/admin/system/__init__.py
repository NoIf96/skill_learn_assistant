# -*- coding:utf-8 -*-
from apis.skill_learn_assistant.admin import admin_bp, logger
from utils.api.blue_route import BlueRoute


system_br = BlueRoute(admin_bp, '/system')

from apis.skill_learn_assistant.admin.system import config_api
