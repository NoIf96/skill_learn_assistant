# -*- coding:utf-8 -*-
from apis.skill_learn_assistant.ordinary import ordinary_bp, logger
from utils.api.blue_route import BlueRoute

recommend_system_br = BlueRoute(ordinary_bp, '/recommend_system')

from apis.skill_learn_assistant.ordinary.recommend_system import skill_api, occupation_api