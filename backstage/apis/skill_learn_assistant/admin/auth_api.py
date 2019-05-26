# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from models.skill_learn_assistant.admin_user import AdminUser
from forms.skill_learn_assistant.admin.auth import LoginForm
from apis.skill_learn_assistant.admin import admin_bp, logger
from utils.api.blue_route import BlueRoute
from utils.api.api_data import *

auth_br = BlueRoute(admin_bp, '/auth')


@auth_br.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'OPTIONS':
            return json_data({'code': 0})

        # if current_user.is_authenticated:
        #     return json_data({'code': 1, 'msg': '以登陆'})

        form = LoginForm()

        if form.validate_on_submit():
            user_name = form.user_name.data
            password = form.password.data
            admin_user = AdminUser.objects(user_name=user_name).first()
            if admin_user:
                if admin_user.validate_password(password):
                    login_user(admin_user)
                    return json_data({'code': 1, 'msg': '登陆成功'})
                else:
                    return json_data({'code': 2, 'msg': '密码错误'})
            else:
                return json_data({'code': 2, 'msg': '账号错误'})
        return json_data({'code': 2, 'msg': '账号错误'})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'code': -1, 'msg': '系统异常'})


@auth_br.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
        return json_data({'msg': '登出成功'})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'msg': '登出异常'})


@auth_br.route('/get_current_user', methods=['GET'])
@login_required
def get_current_user():
    try:
        return json_data({'user_name': current_user.user_name})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'user_name': None})
