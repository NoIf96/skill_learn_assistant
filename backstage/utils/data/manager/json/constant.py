# -*- coding:utf-8 -*-
from utils.data.constant import DATABASEDIR

CONFIG_BASE_PATH = DATABASEDIR + "/config/"
# CONFIG_BASE_PATH = '/home/NoIf/item_test/data/'

# info.json 文件
INFO_JSON_PATH = CONFIG_BASE_PATH + "db/{json_name}.json"
INFO_JSON = {"SKILL_INFO": "skill_info", "OCCUPATION_INFO": "occupation_info"}

# algorithm_model_param.json
ALGORITHM_MODEL_PARARM_JSON_PATH = CONFIG_BASE_PATH + "algorithm_model/{model_type}/{json_name}.json"
ALGORITHM_MODEL_PARARM_TYPE = {
    "SKILL": "skill",
    "OCCUPATION": "occupation"
}
ALGORITHM_MODEL_PARARM_JSON = {
    "CURRENT_MODEL_NAME": "current_model_name",
    "KMEANS_MODEL_PARAM": "kmeans_model_param",
    "KNN_MODEL_PARAM": "knn_model_param",
}

# convert.json
CONVERT_JSON_PATH = CONFIG_BASE_PATH + "convert/{json_name}.json"
CONVERT_JSON = {
    "SORT_CONVERT": "sort_convert",
    "MODEL_PARAM_CONVERT": "model_param_convert",
    "PERMISSION_CONVERT": "permission_convert",
}

