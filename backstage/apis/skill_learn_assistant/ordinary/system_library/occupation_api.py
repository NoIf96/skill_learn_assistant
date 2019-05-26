# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.occupation import Occupation
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.system_library import (
    system_library_br,
    logger,
)
from utils.api.api_data import *

occupation_br = BlueRoute(system_library_br, "/occupation")


@occupation_br.route("/list", methods=["GET"])
@login_required
def get_list_system_occupation():
    params = request.args
    current_page = int(params["current_page"]) - 1
    page_size = int(params["page_size"])

    try:
        model_objects = Occupation.objects.skip((current_page * page_size)).limit(page_size)
        total = Occupation.objects.count()
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
