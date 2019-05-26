# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class Figure3D(object):
    def __init__(self, title, k, data, labels):
        self.title = title  # 标题
        self.data = data.values  # 数据
        self.k = k  # 类别数
        self.labels = labels  # 标签列表
        self.color = ["r", "g", "b", "y", "m", "c", "k"]  # 颜色列表
        self.__load_data = [[] for i in range(self.k)]  # 绘图用数据二维列表
        self.__loading_data()

    def __loading_data(self):
        for k in range(0, self.k):
            for i in range(len(self.labels)):
                if self.labels[i] == k:
                    self.__load_data[k].append(self.data[i])
        # 转换数据用于显示数据时切片
        for k in range(0, self.k):
            self.__load_data[k] = np.array(self.__load_data[k], dtype="float")
        self.__load_data = np.array(self.__load_data)

    def show(self, save_path=False):
        fig = plt.figure()
        ax = plt.axes(projection="3d")

        # 加载数据进图表
        for k in range(0, self.k):
            ax.scatter3D(
                self.__load_data[k][:, 0],
                self.__load_data[k][:, 1],
                self.__load_data[k][:, 2],
                c=self.color[k],
            )

        # 显示图表
        ax.set_zlabel("sort_language")
        ax.set_ylabel("sort_secondary")
        ax.set_xlabel("sort_major")
        ax.set_title(self.title)
        plt.grid()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def get_data(self):
        data = [[self.__load_data[k][:, 0], self.__load_data[k][:, 1], self.__load_data[k][:, 2]] for k in range(0, self.k)]
        return [[[x, y, z] for x in item[0] for y in item[1] for z in item[2]] for item in data]
