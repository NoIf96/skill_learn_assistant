# -*- coding:utf-8 -*-
'''
    噪声清洗模块
'''
import numpy as np
import pandas as pd
from pandas import DataFrame


# 数据清洗， 移除二维列表中指定数据
def clean_data(no_use_label, data):
    '''
    :param no_use_label:  所需移除的列列表
    :param data:   用于操作的数据列表 （二维）
    :return processed_data:   完成处理的数据列表
    '''
    return data.drop(no_use_label, axis=1)
