# -*- coding:utf-8 -*-
from utils.data.constant import TMPBASEDIR
import algorithms.skill_learn_assistant.visualization.processing.preprocessing.noise_cleaning as dpnc
import algorithms.skill_learn_assistant.visualization.processing.preprocessing.normalization as dpn


class Provider(object):
    def __init__(self, manager):
        self.__manager = manager
        self.__label = []
        self.__no_use_label = []

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @property
    def no_use_label(self):
        return self.__no_use_label

    @no_use_label.setter
    def no_use_label(self, no_use_label):
        self.__no_use_label = no_use_label

    def get_id_data(self, no):
        if isinstance(no, list):
            find_query = {"no": {"$in": [str(i) for i in no]}}
        else:
            find_query = {"no": str(no)}
        project = self.get_project()
        return self.__manager.query(find_query, project, self.label)

    def get_all_data(self):
        project = self.get_project()
        return self.__manager.query_all(project, self.label)

    def get_project(self):
        return {"_id": 0, "no": 1}

    def get_clean_all_data(self, data=None):
        if data is None:
            data = self.get_all_data()
        return dpnc.clean_data(self.no_use_label, data)

    def get_deal_all_data(self, data=None):
        return dpn.max_min_normalization(self.get_clean_all_data(data))

    def _to_excel(self, filename='', data=None):
        if data is None:
            data = self.get_all_data()
        excel_writer = f"{TMPBASEDIR}/{filename}.xls"
        data.to_excel(excel_writer)
