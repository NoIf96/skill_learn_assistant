# -*- coding:utf-8 -*-
from apis.skill_learn_assistant.ordinary import ordinary_bp, logger
from utils.api.blue_route import BlueRoute

user_library_br = BlueRoute(ordinary_bp, '/user_library')

from apis.skill_learn_assistant.ordinary.user_library import skill_tree_api, occupation_api