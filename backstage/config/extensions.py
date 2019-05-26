# -*- coding:utf-8 -*-
from flask import request
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

db = MongoEngine()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from models.skill_learn_assistant.admin_user import AdminUser
    from models.skill_learn_assistant.ordinary_user import OrdinaryUser

    if "admin" in request.url:
        user = AdminUser.objects(id=user_id)[0]
    else:
        user = OrdinaryUser.objects(id=user_id)[0]
    return user
