# -*- coding:utf-8 -*-
import os
from utils.data.manager.mongo.skill_provider import SkillProvider
from utils.data.manager.mongo.occupation_provider import OccupationProvider
from utils.data.manager.json.model_param_provider import (
    KmeansModelParamProvider,
    KnnModelParamProvider,
)
from algorithms.manager import Manager
from algorithms.skill_learn_assistant.visualization.processing.visualization import (
    figure_2D,
    figure_3D,
)

model_catalog = "F:/CODE/item/backstage/data/model/{model_type}/"
# model_catalog = "/home/NoIf/item/backstage/data/model/{model_type}/"


def get_manager():
    return Manager()


def get_blr_object(key="main_skill"):
    manager = get_manager()
    return manager.get_blr_object(key)


def generate_blr_model(model_type="skill", key="main_skill", kmeans_param=None, knn_param=None):
    try:
        # 获取blr算法模型
        blr = get_blr_object(key)
        # 获取训练用数据
        provider = SkillProvider() if model_type == "skill" else OccupationProvider()
        blr.original_data = provider.get_all_data()
        blr.system_library = provider.get_clean_all_data()

        # 获取模型参数
        if kmeans_param is None:
            kmeans_param = KmeansModelParamProvider().param
        if knn_param is None:
            knn_param = KnnModelParamProvider().param
        # 生成模型
        blr.generate_model(kmeans_param, knn_param)
        return True
    except Exception as e:
        raise e


def recommendation(skill_list, key="main_skill", dup_re=True):
    provider = SkillProvider()

    # 加载用户技能库数据
    users_skill_library_initial = provider.get_id_data(skill_list)
    users_skill_library_initial_clean = provider.get_clean_all_data(users_skill_library_initial)

    # 获取blr算法模型
    blr = get_blr_object(key)
    recommended_list = blr.recommendation(users_skill_library_initial_clean)  # 推荐
    recommended_list = list(map(str, recommended_list))
    if dup_re:
        recommended_list = list(set(recommended_list) - set(skill_list))
    return recommended_list


def save_blr_model(model_name, model_type="skill", key="main_skill"):
    try:
        model_path = model_catalog.format(model_type=model_type) + f"{model_name}"
        # 获取blr算法模型
        blr = get_blr_object(key)
        if os.path.exists(model_path):
            return 2, "该模型名已存在"
        os.mkdir(model_path)
        blr.save_model(model_path)
        return 1, "保存模型成功"
    except Exception as e:
        return -1, "保存模型出错"


def load_blr_model(model_name, model_type="skill", key="main_skill"):
    try:
        model_path = model_catalog.format(model_type=model_type) + f"{model_name}"
        # 获取blr算法模型
        blr = get_blr_object(key)
        if not os.path.exists(model_path):
            return 2, "不存在该模型"
        blr.load_model(model_path)
        return 1, "加载模型成功"
    except Exception as e:
        return -1, "加载模型出错"


def get_model_list(model_type):
    return os.listdir(model_catalog.format(model_type=model_type))


def get_elbow_rule_data(model_type="skill", key="main_skill", kmeans_param=None):
    try:
        # 获取blr算法模型
        blr = get_blr_object(key)

        # 获取模型参数
        if kmeans_param is None:
            kmeans_param = KmeansModelParamProvider(model_type=model_type).param
        # 生成模型
        elbow_rule_data = blr.bis.get_elbow_rule_data(kmeans_param)
        return elbow_rule_data
    except Exception as e:
        return []


def get_plt2d_data(key="main_skill"):
    try:
        blr = get_blr_object(key)
        figure_2d = figure_2D.Figure2D("2", blr.bis.k, blr.bis.data, blr.bis.labels)
        return figure_2d.get_data()
    except Exception as e:
        return []


def get_plt3d_data(key="main_skill"):
    try:
        blr = get_blr_object(key)
        figure_3d = figure_3D.Figure3D("3", blr.bis.k, blr.bis.data, blr.bis.labels)
        return figure_3d.get_data()
    except Exception as e:
        return []


if __name__ == "__main__":
    print(generate_blr_model(key="test"))
    blr = get_blr_object(key="test")
    print(blr)
    print(blr.original_data)
    print(save_blr_model(key="test", model_name="test"))
    # get_test_object()
    # generate_test_model()
    # test_obj = get_test_object()
    # print(test_obj.no)
