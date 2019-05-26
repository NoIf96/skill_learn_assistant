# # -*- coding:utf-8 -*-
from flask import request
from flask_login import login_required
from algorithms.skill_learn_assistant.apis import algorithms_api
from utils.api.blue_route import BlueRoute
from utils.data.manager.json.convert_provider import ModelParamConvertProvider
from utils.data.manager.json.model_param_provider import (
    CurrentModelProvider,
    KmeansModelParamProvider,
    KnnModelParamProvider,
)
from apis.skill_learn_assistant.admin.system import system_br, logger

from utils.api.api_data import *

config_br = BlueRoute(system_br, "/config")


@config_br.route("/get_model_param_options", methods=["GET"])
@login_required
def get_model_param_options():
    convert_provider = ModelParamConvertProvider()
    return json_data(
        {"options": {"kmeans": convert_provider.kmeans, "knn": convert_provider.knn}}
    )


@config_br.route("/get_model_param", methods=["GET"])
@login_required
def get_model_param():
    params = request.args
    model_type = params["model_type"]
    kmeans_model_param = KmeansModelParamProvider(model_type=model_type).param
    knn_model_param = KnnModelParamProvider(model_type=model_type).param
    return json_data({"kmeans": kmeans_model_param, "knn": knn_model_param})


@config_br.route("/generate_model", methods=["POST"])
@login_required
def generate_model():
    try:
        params = request.get_json()
        model_type = params.get("model_type")
        key_ = f"config_{model_type}"
        current_model_provider = CurrentModelProvider(model_type=model_type)
        current_model_provider.current_model_name = "tmp"
        current_model_provider.write_json(current_model_provider.json_data)

        kmeans_model_provider = KmeansModelParamProvider(model_type=model_type)
        kmeans_model_provider.param = params.get("kmeans")
        kmeans_model_provider.write_json(kmeans_model_provider.json_data)

        knn_model_provider = KnnModelParamProvider(model_type=model_type)
        knn_model_provider.param = params.get("knn")
        knn_model_provider.write_json(knn_model_provider.json_data)

        algorithms_api.generate_blr_model(model_type=model_type, key=key_)
        return json_data({"code": 1, "msg": "生成模型成功"})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"code": -1, "msg": "生成模型失败"})


@config_br.route("/save_model", methods=["POST"])
@login_required
def save_model():
    try:
        params = request.get_json()
        model_type = params.get("model_type")
        model_name = params.get("model_name")
        key_ = f"config_{model_type}"
        status, msg = algorithms_api.save_blr_model(model_name=model_name, model_type=model_type, key=key_)

        kmeans_model_provider = KmeansModelParamProvider(model_type=model_type)
        kmeans_param = kmeans_model_provider.param
        kmeans_json_data = kmeans_model_provider.json_data
        kmeans_json_data[model_name] = {"param": kmeans_param}
        kmeans_model_provider.write_json(kmeans_json_data)

        knn_model_provider = KnnModelParamProvider(model_type=model_type)
        knn_param = knn_model_provider.param
        knn_json_data = knn_model_provider.json_data
        knn_json_data[model_name] = {"param": knn_param}
        knn_model_provider.write_json(knn_json_data)
        return json_data({"code": status, "msg": msg})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"code": -1, "msg": "保存模型失败"})


@config_br.route("/load_model", methods=["POST"])
@login_required
def load_model():
    try:
        params = request.get_json()
        model_type = params.get("model_type")
        model_name = params.get("model_name")
        key_ = f"main_{model_type}"
        status, msg = algorithms_api.load_blr_model(model_name=model_name, model_type=model_type, key=key_)
        current_model_provider = CurrentModelProvider(model_type=model_type)
        current_model_provider.current_model_name = model_name
        current_model_provider.write_json(current_model_provider.json_data)
        return json_data({"code": status, "msg": msg})
    except Exception as e:
        logger.exception(e)
        return json_data_error({"code": -1, "msg": "加载模型失败"})


@config_br.route("/get_model_list", methods=["GET"])
@login_required
def get_model_list():
    params = request.args
    model_type = params["model_type"]
    model_list = algorithms_api.get_model_list(model_type)
    return json_list_data({"list": model_list, "total": len(model_list)})


@config_br.route("/get_img_data", methods=["GET"])
@login_required
def get_img_data():
    params = request.args
    model_type = params["model_type"]
    key_ = f"config_{model_type}"
    elbow_rule_data = algorithms_api.get_elbow_rule_data(model_type=model_type, key=key_)
    plt2d_data = algorithms_api.get_plt2d_data(key=key_)
    plt3d_data = algorithms_api.get_plt3d_data(key=key_)

    list_ = [
        {"title": "elbow_rule", "data": elbow_rule_data, "total": len(elbow_rule_data)},
        {"title": "plt2d", "data": plt2d_data, "total": len(plt2d_data)},
        {"title": "plt3d", "data": plt3d_data, "total": len(plt3d_data)},
    ]

    return json_list_data({"list": list_, "total": len(list_)})
