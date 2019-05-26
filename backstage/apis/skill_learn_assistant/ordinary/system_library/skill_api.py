# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.skill import Skill
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.system_library import (
    system_library_br,
    logger,
)
from utils.api.api_data import *

skill_br = BlueRoute(system_library_br, "/skill")


@skill_br.route("/list", methods=["GET"])
@login_required
def get_list_system_skill():
    params = request.args
    current_page = int(params["current_page"]) - 1
    page_size = int(params["page_size"])

    try:
        model_objects = Skill.objects.skip((current_page * page_size)).limit(page_size)
        total = Skill.objects.count()
        new_model_objects = [
            {
                "no": model_object.no,
                "name": model_object.name,
                "introduction": model_object.introduction,
            }
            for model_object in model_objects
        ]
        return json_list_data({"list": new_model_objects, "total": total})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({"list": []})


@skill_br.route("/user_list", methods=["GET"])
@login_required
def get_list_user_skill():
    try:
        user_skill_list = current_user.user_skill_list
        model_objects = Skill.objects(no__in=user_skill_list)
        total = len(user_skill_list)
        new_model_objects = [
            {
                "no": model_object.no,
                "name": model_object.name,
                "introduction": model_object.introduction,
            }
            for model_object in model_objects
        ]
        return json_list_data({"list": new_model_objects, "total": total})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({"list": []})


@skill_br.route("/save_user_skill", methods=["POST"])
@login_required
def save_user_skill():
    params = request.get_json()
    user_skill_list = params["skill_list"]
    try:
        current_user.user_skill_list = user_skill_list
        current_user.save()
        return json_data({"msg": "保存成功"})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"msg": "保存失败"})
