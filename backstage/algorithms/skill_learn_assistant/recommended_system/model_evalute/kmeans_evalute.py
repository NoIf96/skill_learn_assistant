# -*- coding:utf-8 -*-


from sklearn import metrics


# silhouette coefficient系数
def silhouette_coefficient(model, data):
    print("；轮廓系数：%.03f", metrics.silhouette_score(data, model.labels_, metrics='euclidean'))
