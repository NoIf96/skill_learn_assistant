# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required
from models.skill_learn_assistant.occupation import Occupation
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.admin.library import (
    library_br,
    get_sort_convert,
    logger,
)

from utils.api.api_data import *
from utils.worm import baidu_encyclopedia

occupation_br = BlueRoute(library_br, "/occupation")


@occupation_br.route("/add", methods=["POST"])
@login_required
def add_occupation():
    params = request.get_json()
    if not is_exist(Occupation, params, Occupation.is_exist_key()):
        model_object = Occupation()
        model_object.dict_to_object(params)
        try:
            model_object.save()
            return json_data({"msg": "添加成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "添加失败，数据库添加出错"})
    return json_data_error({"msg": "添加失败，该职业已存在"})


@occupation_br.route("/delete", methods=["POST"])
@login_required
def delete_occupation():
    params = request.get_json()
    model_object = is_exist(Occupation, params, Occupation.is_exist_key())
    if model_object:
        try:
            model_object.delete()
            return json_data({"msg": "删除成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "删除失败，数据库删除出错"})
    return json_data_error({"msg": "删除失败，该职业不存在"})


@occupation_br.route("/edit", methods=["POST"])
@login_required
def update_occupation():
    params = request.get_json()
    model_object = is_exist(Occupation, params, Occupation.is_exist_key())
    if model_object:
        try:
            model_object.dict_to_object(params)
            model_object.save()
            return json_data({"msg": "修改成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "修改失败，数据库修改出错"})
    return json_data_error({"msg": "修改失败，该技职业不存在"})


@occupation_br.route("/list", methods=["GET"])
@login_required
def get_list_occupation():
    params = request.args
    current_page = int(params["current_page"]) - 1
    page_size = int(params["page_size"])

    try:
        model_objects = Occupation.objects.skip((current_page * page_size)).limit(
            page_size
        )
        total = Occupation.objects.count()
        transform_keys = Occupation.get_transform_keys()
        model_transform = get_sort_convert()
        new_model_objects = transform_key_value(
            model_objects, model_transform, transform_keys
        )
        return json_list_data({"list": new_model_objects, "total": total})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({"list": []})


@occupation_br.route("/get_sort_options", methods=["GET"])
@login_required
def get_occupation_options():
    try:
        occupation_option_data = get_sort_convert()
        sort_major_data = occupation_option_data.get("sort_major")
        sort_secondary_data = occupation_option_data.get("sort_secondary")
        sort_language_data = occupation_option_data.get("sort_language")
        sort_major_options = [
            {"label": sort_major_data.get(key), "value": key} for key in sort_major_data
        ]
        sort_secondary_options = [
            {"label": sort_secondary_data.get(key), "value": key}
            for key in sort_secondary_data
        ]
        sort_language_options = [
            {"label": sort_language_data.get(key), "value": key}
            for key in sort_language_data
        ]
        occupation_options = {
            "sort_major": sort_major_options,
            "sort_secondary": sort_secondary_options,
            "sort_language": sort_language_options,
        }

        return json_data({"options": occupation_options})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"options": []})


@occupation_br.route("/auto_update_occupation_introduction", methods=["GET"])
@login_required
def auto_update_occupation_introduction():
    try:
        count, fail_list = baidu_encyclopedia.update_introduction("occupation")
        if fail_list:
            return json_data({"msg": f"共获取{count}个描述， 获取失败如下:{''.join(fail_list)}"})
        return json_data({"msg": f"共获取{count}个描述"})
    except Exception as e:
        return json_data({"msg": " 获取描述失败"})


@occupation_br.route("/get_occupation_introduction", methods=["POST"])
@login_required
def get_occupation_introduction():
    params = request.get_json()
    name = params["name"]
    tmp = params["introduction"]
    try:
        url = tmp.split("-*-*-")[1] if tmp.startswith("-*-*-") else ""
        introduction = baidu_encyclopedia.get_one_introduction(name, url)
        introduction = introduction
        return json_data({"msg": "获取描述成功", "introduction": introduction})
    except Exception as e:
        return json_data({"msg": " 获取描述失败", "introduction": ""})

