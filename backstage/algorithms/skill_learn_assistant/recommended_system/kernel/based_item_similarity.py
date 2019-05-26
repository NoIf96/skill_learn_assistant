# -*- coding:utf-8 -*-
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt


class BasedItemSimilarity(object):
    def __init__(self):
        self.__data = None  # 数据集
        self.__kmeans_model = None
        self.__knn_model = None

    def generate_model(self, kmeans_param, knn_param):
        self.__kmeans_model = KMeans(
            n_clusters=kmeans_param["n_clusters"],
            max_iter=kmeans_param["max_iter"],
            init=kmeans_param["init"],
            n_init=kmeans_param["n_init"],
            algorithm=kmeans_param["algorithm"],
        ).fit(self.__data)
        self.__knn_model = NearestNeighbors(
            n_neighbors=knn_param["n_neighbors"],
            radius=knn_param["radius"],
            algorithm=knn_param["algorithm"],
        ).fit(self.__data)

    def save_model(self, model_path):
        joblib.dump(self.__kmeans_model, f"{model_path}/kemans_model.m", compress=3)
        joblib.dump(self.__knn_model, f"{model_path}/knn_model.m", compress=3)

    def load_model(self, model_path):
        self.__kmeans_model = joblib.load(f"{model_path}/kemans_model.m")
        self.__knn_model = joblib.load(f"{model_path}/knn_model.m")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def labels(self):
        return self.__kmeans_model.labels_

    @property
    def k(self):
        return self.__kmeans_model.n_clusters

    @property
    def cluster_centers(self):
        return self.__kmeans_model.cluster_centers_

    # 预测分类标签访问器
    def predict_kmeans_label(self, x):
        return self.__kmeans_model.predict(x)

    def predict_knn_data(self, x):
        return self.__knn_model.radius_neighbors(x, return_distance=False)

    def elbow_rule(self, save_path=False):
        meandistorions = []
        n = range(1, 10)
        fig = plt.figure()
        for k in n:
            kmeans = KMeans(n_clusters=k, max_iter=2000, n_init=30)
            kmeans.fit(self.__data)
            meandistorions.append(
                sum(
                    np.min(
                        cdist(self.__data, kmeans.cluster_centers_, "euclidean"), axis=1
                    )
                )
                / self.__data.shape[0]
            )
        plt.plot(n, meandistorions, "bx-")
        plt.xlabel("k")
        plt.ylabel("平均畸变程度")
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def get_elbow_rule_data(self, kmeans_param):
        elbow_rule_data = []
        for i in range(1, 10):
            kmeans = KMeans(
                n_clusters=i,
                max_iter=kmeans_param["max_iter"],
                init=kmeans_param["init"],
                n_init=kmeans_param["n_init"],
                algorithm=kmeans_param["algorithm"],
            ).fit(self.__data)
            elbow_rule_data.append(
                sum(
                    np.min(
                        cdist(self.__data, kmeans.cluster_centers_, "euclidean"), axis=1
                    )
                )
                / self.__data.shape[0]
            )
        return elbow_rule_data
