# -*- coding:utf-8 -*-
from blueprints.skill_learn_assistant_bp import admin_bp
from utils.data.manager.log.manage import Manage

log_manage = Manage('skill_learn_assistant_admin')
log_manage.set_handler('skill_learn_assistant_admin.log')
logger = log_manage.logger


from apis.skill_learn_assistant.admin import library, system, user, auth_api
