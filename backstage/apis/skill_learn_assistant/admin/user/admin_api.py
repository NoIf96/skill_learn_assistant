# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.admin_user import AdminUser
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.admin.user import user_br, get_permission_convert, SUPER_ADMINISTRATOR, logger
from apis.skill_learn_assistant.admin.auth_api import logout

from utils.api.api_data import *

admin_br = BlueRoute(user_br, '/admin')


@admin_br.route('/add', methods=['POST'])
@login_required
def add_admin_user():
    if current_user.permission != SUPER_ADMINISTRATOR:
        return json_data_error({'msg': '权限不足'})

    params = request.get_json()
    if not is_exist(AdminUser, params, AdminUser.is_exist_key()):
        model_object = AdminUser()
        model_object.dict_to_object(params)
        try:
            model_object.save()
            return json_data({'msg': '添加成功'})
        except Exception as e:
            logger.exception(e)
            return json_data_error({'msg': '添加失败，数据库添加出错'})
    return json_data_error({'msg': '添加失败，该管理员已存在'})


@admin_br.route('/delete', methods=['POST'])
@login_required
def delete_admin_user():
    if current_user.permission != SUPER_ADMINISTRATOR:
        return json_data_error({'msg': '权限不足'})

    params = request.get_json()
    model_object = is_exist(AdminUser, params, AdminUser.is_exist_key())
    if model_object:
        try:
            if model_object == current_user:
                logout()
            model_object.delete()
            return json_data({'msg': '删除成功'})
        except Exception as e:
            logger.exception(e)
            return json_data_error({'msg': '删除失败，数据库删除出错'})
    return json_data_error({'msg': '删除失败，该管理员不存在'})


@admin_br.route('/edit', methods=['POST'])
@login_required
def update_admin_user():
    if current_user.permission != SUPER_ADMINISTRATOR:
        return json_data_error({'msg': '权限不足'})

    params = request.get_json()
    model_object = is_exist(AdminUser, params, AdminUser.is_exist_key())
    if model_object:
        try:
            model_object.dict_to_object(params)
            model_object.save()
            return json_data({'msg': '修改成功'})
        except Exception as e:
            logger.exception(e)
            return json_data_error({'msg': '修改失败，数据库删除出错'})
    return json_data_error({'msg': '修改失败，该管理员不存在'})


@admin_br.route('/list', methods=['GET'])
@login_required
def get_list_admin_user():
    params = request.args
    current_page = int(params['current_page']) - 1
    page_size = int(params['page_size'])

    try:
        model_objects = AdminUser.objects.skip((current_page * page_size)).limit(page_size)
        total = AdminUser.objects.count()
        transform_keys = AdminUser.get_transform_keys()
        model_transform = get_permission_convert()
        new_model_objects = transform_key_value(model_objects, model_transform, transform_keys)
        return json_list_data({'list': new_model_objects, 'total': total})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({'list': []})


@admin_br.route('/get_permission_options', methods=['GET'])
@login_required
def get_permission_options():
    try:
        permission_option_data = get_permission_convert().get('permission')
        permission_options = [{'label': permission_option_data.get(key), 'value': key} for key in permission_option_data]

        return json_data({'options': permission_options})
    except Exception as e:
        logger.exception(e)
        return json_data_error({'options': []})
