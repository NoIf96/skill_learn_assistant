# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required
from models.skill_learn_assistant.skill import Skill
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.admin.library import (
    library_br,
    get_sort_convert,
    logger,
)
from utils.api.api_data import *
from utils.worm import baidu_encyclopedia

skill_br = BlueRoute(library_br, "/skill")


@skill_br.route("/add", methods=["POST"])
@login_required
def add_skill():
    params = request.get_json()
    if not is_exist(Skill, params, Skill.is_exist_key()):
        model_object = Skill()
        model_object.dict_to_object(params)
        print(model_object)
        try:
            model_object.save()
            return json_data({"msg": "添加成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "添加失败，数据库添加出错"})
    return json_data_error({"msg": "添加失败，该技能已存在"})


@skill_br.route("/delete", methods=["POST"])
@login_required
def delete_skill():
    params = request.get_json()
    model_object = is_exist(Skill, params, Skill.is_exist_key())
    if model_object:
        try:
            model_object.delete()
            return json_data({"msg": "删除成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "删除失败，数据库删除出错"})
    return json_data_error({"msg": "删除失败，该技能不存在"})


@skill_br.route("/edit", methods=["POST"])
@login_required
def update_skill():
    params = request.get_json()
    model_object = is_exist(Skill, params, Skill.is_exist_key())
    if model_object:
        try:
            model_object.dict_to_object(params)
            model_object.save()
            return json_data({"msg": "修改成功"})
        except Exception as e:
            logger.exception(e)
            return json_data_error({"msg": "修改失败，数据库修改出错"})
    return json_data_error({"msg": "修改失败，该技能不存在"})


@skill_br.route("/list", methods=["GET"])
@login_required
def get_list_skill():
    params = request.args
    current_page = int(params["current_page"]) - 1
    page_size = int(params["page_size"])

    try:
        model_objects = Skill.objects.skip((current_page * page_size)).limit(page_size)
        total = Skill.objects.count()
        transform_keys = Skill.get_transform_keys()
        model_transform = get_sort_convert()
        new_model_objects = transform_key_value(
            model_objects, model_transform, transform_keys
        )
        return json_list_data({"list": new_model_objects, "total": total})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({"list": []})


@skill_br.route("/get_sort_options", methods=["GET"])
@login_required
def get_skill_options():
    try:
        skill_option_data = get_sort_convert()
        sort_major_data = skill_option_data.get("sort_major")
        sort_secondary_data = skill_option_data.get("sort_secondary")
        sort_language_data = skill_option_data.get("sort_language")
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
        skill_options = {
            "sort_major": sort_major_options,
            "sort_secondary": sort_secondary_options,
            "sort_language": sort_language_options,
        }

        return json_data({"options": skill_options})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"options": []})


@skill_br.route("/auto_update_skill_introduction", methods=["GET"])
@login_required
def auto_update_skill_introduction():
    try:
        count, fail_list = baidu_encyclopedia.update_introduction("skill")
        if fail_list:
            return json_data({"msg": f"共获取{count}个描述， 获取失败如下:{''.join(fail_list)}"})
        return json_data({"msg": f"共获取{count}个描述"})
    except Exception as e:
        logger.exception(e)
        return json_data({"msg": " 获取描述失败"})


@skill_br.route("/get_skill_introduction", methods=["POST"])
@login_required
def get_skill_introduction():
    try:
        params = request.get_json()
        name = params["name"]
        tmp = params["introduction"]
        url = tmp.split("-*-*-")[1] if tmp.startswith("-*-*-") else ""
        introduction = baidu_encyclopedia.get_one_introduction(name, url)
        introduction = introduction
        return json_data({"msg": "获取描述成功", "introduction": introduction})
    except Exception as e:
        logger.exception(e)
        return json_data({"msg": " 获取描述失败", "introduction": ""})
