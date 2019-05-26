# -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from models.skill_learn_assistant.skill import Skill
from utils.api.blue_route import BlueRoute
from apis.skill_learn_assistant.ordinary.user_library import user_library_br, logger
from utils import util
from utils.api.api_data import *


skill_tree_br = BlueRoute(user_library_br, "/skill_tree")


@skill_tree_br.route("/list", methods=["GET"])
@login_required
def get_list_skill():
    params = request.args
    sort_type = params["sort_type"]
    try:
        user_skill_list = current_user.user_skill_list
        user_skill_list_data = Skill.objects(no__in=user_skill_list)
        data = util.get_graph_data(user_skill_list_data, sort_type)
        return json_data({"graph_data": data})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"graph_data": {}})

