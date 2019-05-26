# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pprint


class Figure2D(object):
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
        ax = plt.axes()

        # 加载数据进图表
        for k in range(0, self.k):
            ax.scatter(
                self.__load_data[k][:, 0], self.__load_data[k][:, 1], c=self.color[k]
            )

        # 显示图表
        ax.set_ylabel("sort_language")
        ax.set_xlabel("sort_major")
        plt.xlim(-1, 10, 1)
        plt.ylim(-1, 10, 1)
        ax.set_title(self.title)
        plt.grid()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def get_data(self):
        data = [[self.__load_data[k][:, 0], self.__load_data[k][:, 1]] for k in range(0, self.k)]
        return [[[x, y] for x in item[0] for y in item[1]] for item in data]
