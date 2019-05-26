# -*- coding:utf-8 -*-
from utils.data.manager.json.constant import (
    ALGORITHM_MODEL_PARARM_JSON_PATH,
    ALGORITHM_MODEL_PARARM_TYPE,
    ALGORITHM_MODEL_PARARM_JSON,
)
from utils.data.manager.json.manager import Manager
from utils.data.manager.json.provider import Provider


class CurrentModelProvider(Provider):
    def __init__(self, model_type=ALGORITHM_MODEL_PARARM_TYPE.get("SKILL")):
        manager = Manager(
            ALGORITHM_MODEL_PARARM_JSON_PATH.format(model_type=model_type,
                                                    json_name=ALGORITHM_MODEL_PARARM_JSON.get("CURRENT_MODEL_NAME"))
        )
        Provider.__init__(self, manager)

    @property
    def current_model_name(self):
        return self.get_key_value(self.json_data, "current_model_name")

    @current_model_name.setter
    def current_model_name(self, value):
        self.set_key_value(self.json_data, "current_model_name", value)


class ModelParamProvider(Provider):
    def __init__(self, model_type, json_name):
        manager = Manager(
            ALGORITHM_MODEL_PARARM_JSON_PATH.format(model_type=model_type, json_name=json_name)
        )
        Provider.__init__(self, manager)
        self.__current_model_provider = CurrentModelProvider(model_type)
        self.__current_model_name = self.__current_model_provider.current_model_name

    @property
    def current_model_name(self):
        return self.__current_model_name

    @current_model_name.setter
    def current_model_name(self, value):
        self.__current_model_name = value

    @property
    def param(self):
        return self.get_key_value(self.get_key_value(self.json_data, self.current_model_name), "param")

    @param.setter
    def param(self, value):
        self.set_key_value(self.get_key_value(self.json_data, self.current_model_name), "param", value)


class KmeansModelParamProvider(ModelParamProvider):
    def __init__(self, model_type=ALGORITHM_MODEL_PARARM_TYPE.get("SKILL")):
        ModelParamProvider.__init__(
            self,
            model_type,
            ALGORITHM_MODEL_PARARM_JSON.get("KMEANS_MODEL_PARAM")
        )


class KnnModelParamProvider(ModelParamProvider):
    def __init__(self, model_type=ALGORITHM_MODEL_PARARM_TYPE.get("SKILL")):
        ModelParamProvider.__init__(
            self,
            model_type,
            ALGORITHM_MODEL_PARARM_JSON.get("KNN_MODEL_PARAM")
        )
