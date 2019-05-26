# -*- coding:utf-8 -*-
from flask_login import login_user, logout_user, login_required, current_user
from models.skill_learn_assistant.ordinary_user import OrdinaryUser
from forms.skill_learn_assistant.ordinary.auth import LoginForm, RegisterForm
from apis.skill_learn_assistant.ordinary import ordinary_bp, logger
from utils.api.blue_route import BlueRoute
from utils.api.api_data import *

auth_br = BlueRoute(ordinary_bp, '/auth')


@auth_br.route('/login', methods=['GET', 'POST'])
def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            user_email = form.user_email.data
            password = form.password.data
            ordinary_user = OrdinaryUser.objects(user_email=user_email).first()
            if ordinary_user:
                if ordinary_user.validate_password(password):
                    login_user(ordinary_user)
                    return json_data({'code': 1, 'msg': '用户登陆成功'})
                else:
                    return json_data({'code': 2, 'msg': '用户密码错误'})
            else:
                return json_data({'code': 2, 'msg': '用户账号错误'})
        return json_data({'code': 2, 'msg': '用户验证失败'})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'code': -1, 'msg': '系统异常，请联系管理员'})


@auth_br.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
        return json_data({'msg': '用户登出成功'})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'msg': '用户登出异常'})


@auth_br.route('/get_current_user', methods=['GET'])
@login_required
def get_current_user():
    try:
        return json_data({'user_name': current_user.user_name})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'user_name': None})


@auth_br.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            ordinary_user = OrdinaryUser.objects(user_name=form.user_name.data).first()
            if ordinary_user:
                return json_data({'code': 2, 'msg': '用户已存在'})
            else:
                params = {
                    'user_name': form.user_name.data,
                    'user_email': form.user_email.data,
                    'password': form.password.data,
                }
                ordinary_user = OrdinaryUser()
                ordinary_user.dict_to_object(params)
                ordinary_user.save()
                return json_data({'code': 1, 'msg': '注册成功'})
        else:
            return json_data({'code': 2, 'msg': '参数错误'})
    except Exception as e:
        print(e)
        return json_data_error({'code': -1, 'msg': '注册失败'})


