# -*- coding:utf-8 -*-
from apis.skill_learn_assistant.ordinary import ordinary_bp, logger
from utils.api.blue_route import BlueRoute

system_library_br = BlueRoute(ordinary_bp, '/system_library')

from apis.skill_learn_assistant.ordinary.system_library import skill_api, occupation_api