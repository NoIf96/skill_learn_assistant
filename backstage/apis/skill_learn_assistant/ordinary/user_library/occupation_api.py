# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.occupation import Occupation
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.user_library import user_library_br, logger
from utils.api.api_data import *
from algorithms.skill_learn_assistant.apis import algorithms_api

occupation_br = BlueRoute(user_library_br, "/occupation")


@occupation_br.route("/list")
@login_required
def get_user_occupation_list():
    try:
        user_recommend_occupation_list = current_user.recommend_occupation_list
        user_recommend_occupation_list_data = Occupation.objects(no__in=user_recommend_occupation_list)
        user_recommend_occupation_list_data = [{"no": occupation.no, "name": occupation.name, "introduction": occupation.introduction}
                                       for occupation in user_recommend_occupation_list_data]

        return json_list_data({"list": user_recommend_occupation_list_data, "total": len(user_recommend_occupation_list_data)})
    except Exception as e:
        logger.exception(e)
        return json_list_data_error({"list": [], "total": 0})
