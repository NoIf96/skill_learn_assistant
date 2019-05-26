# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.skill import Skill
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.recommend_system import recommend_system_br, logger
from utils import util
from utils.api.api_data import *
from algorithms.skill_learn_assistant.apis import algorithms_api

skill_br = BlueRoute(recommend_system_br, "/skill")


@skill_br.route("/get_recommended_skill_tree")
@login_required
def get_recommended_skill_tree():
    try:
        user_skill_list = current_user.user_skill_list
        recommended_skill_list = algorithms_api.recommendation(user_skill_list, key="main_skill")
        recommended_skill_list_data = Skill.objects(no__in=recommended_skill_list)
        recommended_skill_list_data = [{"no": skill.no, "name": skill.name, "introduction": skill.introduction}
                                       for skill in recommended_skill_list_data]
        user_skill_list.extend(recommended_skill_list)
        user_skill_list_data = Skill.objects(no__in=user_skill_list)
        data = util.get_graph_data(user_skill_list_data)
        data["nodes"] = [set_recommended_category(node, recommended_skill_list) for node in data["nodes"]]
        data["categories"].append({"name": "预测"})
        return json_data(
            {"graph_data": data, "list": recommended_skill_list_data, "total": len(recommended_skill_list_data)})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"graph_data": {}, "list": [], "total": 0})


@skill_br.route("/add_user_skill", methods=['POST'])
@login_required
def add_user_skill():
    params = request.get_json()
    no = params["no"]
    try:
        user_skill_list = current_user.user_skill_list
        user_skill_list.append(no)
        user_skill_list = list(set(user_skill_list))
        current_user.user_skill_list = user_skill_list
        current_user.save()
        return json_data({"msg": "添加成功"})
    except Exception as e:
        return json_data({"msg": " 添加失败"})


def set_recommended_category(node, recommended_skill_list):
    if node["skill"]["no"] in recommended_skill_list:
        node["category"] = "预测"
    return node
