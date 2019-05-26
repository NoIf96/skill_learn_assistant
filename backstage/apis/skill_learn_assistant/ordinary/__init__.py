# -*- coding:utf-8 -*-
from blueprints.skill_learn_assistant_bp import ordinary_bp
from utils.data.manager.log.manage import Manage

log_manage = Manage('skill_learn_assistant_ordinary')
log_manage.set_handler('skill_learn_assistant_ordinary.log')
logger = log_manage.logger


from apis.skill_learn_assistant.ordinary import auth_api, system_library, user_library, recommend_system