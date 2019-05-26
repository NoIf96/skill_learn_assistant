# -*- coding:utf-8 -*-
import algorithms.skill_learn_assistant.recommended_system.kernel.based_item_similarity as RKB

title = "blr"


def create_object():
    return BasedLibraryRecommendation()


class BasedLibraryRecommendation(object):
    def __init__(self):
        self.__original_data = None  # 原始数据
        self.__system_library = None  # 系统技能库
        self.__users_library = None  # 用户技能库
        self.__bis = None  # 基于物品相似度推荐系统核心
        self.__recommended = None

    @property
    def original_data(self):
        return self.__original_data

    @original_data.setter
    def original_data(self, original_data):
        self.__original_data = original_data

    @property
    def system_library(self):
        return self.__system_library

    @system_library.setter
    def system_library(self, system_library):
        self.__system_library = system_library

    @property
    def users_library(self):
        return self.__users_library

    @users_library.setter
    def users_library(self, users_library):
        self.__users_library = users_library

    @property
    def bis(self):
        return self.__bis

    @property
    def recommended(self):
        return self.__recommended

    def generate_model(self, kmeans_param, knn_param):
        if self.__bis is None:
            self.__bis = RKB.BasedItemSimilarity()
            self.__bis.data = self.__system_library
        self.__bis.generate_model(kmeans_param, knn_param)  # 进行物品相似度推荐系统核心算法建模

    # 保存模型
    def save_model(self, model_path):
        self.__bis.save_model(model_path)

    # 加载模型
    def load_model(self, model_path):
        self.__bis.load_model(model_path)

    def recommendation(self, users_library=None):
        if users_library is None:
            users_library = self.__users_library
        labels = self.__bis.labels  # 获取KMeans聚类标签
        # 获取用户技能Kmeans算法预测标签
        kmeans_labels = self.__bis.predict_kmeans_label(users_library)
        # 获取KNN算法求得的相似列表
        knn_datas = self.__bis.predict_knn_data(users_library)
        # 提取推荐列表
        recommended_no = [no for i, kmeans_label in enumerate(kmeans_labels) for no in knn_datas[i] if kmeans_label == labels[no]]

        # 去除重复数据
        recommended_no = list(set(recommended_no))
        recommended = [self.original_data.iloc[no].no for no in recommended_no]
        self.__recommended = recommended
        return recommended


if __name__ == "__main__":
    from utils.data.manager.json.model_param_provider import ModelParamProvider
    from utils.data.manager.json.constant import ALGORITHM_MODEL_PARARM_JSON
    from utils.data.manager.mongo.skill_provider import SkillProvider

    kmeans_model_param_provider = ModelParamProvider(
        ALGORITHM_MODEL_PARARM_JSON.get("KMEANS_MODEL_PARAM")
    )
    knn_model_param_provider = ModelParamProvider(
        ALGORITHM_MODEL_PARARM_JSON.get("KNN_MODEL_PARAM")
    )
    kmeans_param = kmeans_model_param_provider.param
    knn_param = knn_model_param_provider.param

    # 加载系统技能库数据
    # system_skills_library_initial = xd.readXMLData(xml_config.skill_info["file_path"],
    #                                                xml_config.skill_info["node"],
    #                                                xml_config.skill_info["label"])
    s = SkillProvider()
    system_skills_library_data = s.get_all_data()
    system_skills_library_clean = s.get_clean_all_data()
    # print(system_skills_library_clean)

    # # 加载用户技能库数据
    users_skill_library_initial = s.get_id_data(["1023"])
    # print(users_skill_library_initial)
    users_skill_library_initial_clean = s.get_clean_all_data(
        users_skill_library_initial
    )
    # print(users_skill_library_initial_clean)

    bsr = BasedLibraryRecommendation()
    bsr.original_data = system_skills_library_data
    bsr.system_library = system_skills_library_clean
    bsr.users_library = users_skill_library_initial_clean

    bsr.generate_model(kmeans_param, knn_param)  # 构建模型
    # bsr.bis.elbow_rule()  # 肘部法则
    bsr.recommendation()  # 推荐
    recommended_skill = bsr.recommended
    # print(recommended_skill)

    print(s.get_id_data(recommended_skill))
    print(bsr.save_model("F:/CODE/item/backstage/data/model/a-1/"))
    # print(bsr.bis.kmeans_model_score)
    # print(bsr.bis.knn_model_score)
