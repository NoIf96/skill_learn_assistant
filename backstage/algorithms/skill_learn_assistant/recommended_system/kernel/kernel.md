#kernel说明

用于存放项目所使用到数据处理相关代码

###based_item_similarity

基于物品相似度的推荐核心

####based_item_similarity说明

    class BasedItemSimilarity(object)
          __init__(self, data)  初始化
          generateModel(self)   构建模型
          setK(self, k)  k值修改器
          getK(self)  k值访问器
          getLabels(self)   分类标签列表访问器
          getClusterCenters(self)   集群中心访问器
          getPredictLable(self, x)  预测分类标签访问器
          getRecommended(self, x)   推荐列表访问器
          elbowRule(self)   肘部法则 用于测试出k值选择