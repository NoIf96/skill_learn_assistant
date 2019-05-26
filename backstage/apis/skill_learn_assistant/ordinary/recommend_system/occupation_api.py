# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.skill import Skill
from models.skill_learn_assistant.occupation import Occupation
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.recommend_system import recommend_system_br, logger
from utils import util
from utils.api.api_data import *
from algorithms.skill_learn_assistant.apis import algorithms_api

occupation_br = BlueRoute(recommend_system_br, "/occupation")


@occupation_br.route("/get_recommended_occupation_list")
@login_required
def get_recommended_occupation_list():
    try:
        user_skill_list = current_user.user_skill_list
        recommended_occupation_list = algorithms_api.recommendation(user_skill_list, key="main_occupation", dup_re=False)
        recommended_occupation_list = [recommended_occupation.zfill(4) for recommended_occupation in recommended_occupation_list]
        recommended_occupation_list = list(set(recommended_occupation_list) - set(current_user.recommend_occupation_list))
        recommended_occupation_list_data = Occupation.objects(no__in=recommended_occupation_list)
        recommended_occupation_list_data = [{"no": occupation.no, "name": occupation.name, "introduction": occupation.introduction}
                                       for occupation in recommended_occupation_list_data]

        return json_data({"list": recommended_occupation_list_data, "total": len(recommended_occupation_list_data)})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"list": [], "total": 0})


@occupation_br.route("/add_user_recommend_occupation_list", methods=['POST'])
@login_required
def add_user_recommend_occupation_list():
    params = request.get_json()
    no = params["no"]
    try:
        user_recommend_occupation_list = current_user.recommend_occupation_list
        user_recommend_occupation_list.append(no)
        user_recommend_occupation_list = list(set(user_recommend_occupation_list))
        current_user.user_recommend_occupation_list = user_recommend_occupation_list
        current_user.save()
        return json_data({"msg": "添加成功"})
    except Exception as e:
        return json_data({"msg": " 添加失败"})
