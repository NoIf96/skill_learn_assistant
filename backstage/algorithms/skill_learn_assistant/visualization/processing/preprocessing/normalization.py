# -*- coding:utf-8 -*-
'''
    规范化模块
'''
from sklearn import preprocessing


# 线性归一化
def max_min_normalization(data):
    '''
    :param data: 所需处理的np.arrary
    :return:返回归一化后的np.arrary
    '''
    return preprocessing.StandardScaler().fit_transform(data)


# 标准化
def z_score(data):
    '''
    :param data: 所需处理的np.arrary
    :return: 返回标准化后的np.arrary
    '''
    return preprocessing.scale(data)


