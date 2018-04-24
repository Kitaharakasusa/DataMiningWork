# from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import math


UNCLASSIFIED = False
NOISE = 0

def loadDataSet(fileName, splitChar='\t'):
    """
    输入：文件名
    输出：数据集
    描述：从文件读入数据集
    """
    dataSet = []
    rf = open(fileName, "r", encoding="utf-8")
    allvector = list()
    for line in rf:
        vecotor = line.split(",")[0:-1]
        # print(vecotor)
        floatlis = []
        for str in vecotor:
            floatlis.append(float(str))
        allvector.append(floatlis)
    # with open(fileName) as fr:
    #     for line in fr.readlines():
    #         curline = line.strip().split(splitChar)
    #         fltline = list(map(float, curline))
    #         dataSet.append(fltline)
    #         print(fltline)
    return allvector

def dist(a, b):
    """
    输入：向量A, 向量B
    输出：两个向量的欧式距离
    """
    return math.sqrt(np.power(a - b, 2).sum())

def eps_neighbor(a, b, eps):
    """
    输入：向量A, 向量B
    输出：是否在eps范围内
    """
    return dist(a, b) < eps

def region_query(data, pointId, eps):
    """
    输入：数据集, 查询点id, 半径大小
    输出：在eps范围内的点的id
    """
    nPoints = data.shape[1]
    seeds = []
    for i in range(nPoints):
        if eps_neighbor(data[:, pointId], data[:, i], eps):
            seeds.append(i)
    return seeds

def expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
    """
    输入：数据集, 分类结果, 待分类点id, 簇id, 半径大小, 最小点个数
    输出：能否成功分类
    """
    seeds = region_query(data, pointId, eps)
    if len(seeds) < minPts: # 不满足minPts条件的为噪声点
        clusterResult[pointId] = NOISE
        return False
    else:
        clusterResult[pointId] = clusterId # 划分到该簇
        for seedId in seeds:
            clusterResult[seedId] = clusterId

        while len(seeds) > 0: # 持续扩张
            currentPoint = seeds[0]
            queryResults = region_query(data, currentPoint, eps)
            if len(queryResults) >= minPts:
                for i in range(len(queryResults)):
                    resultPoint = queryResults[i]
                    if clusterResult[resultPoint] == UNCLASSIFIED:
                        seeds.append(resultPoint)
                        clusterResult[resultPoint] = clusterId
                    elif clusterResult[resultPoint] == NOISE:
                        clusterResult[resultPoint] = clusterId
            seeds = seeds[1:]
        return True

def dbscan(data, eps, minPts):
    """
    输入：数据集, 半径大小, 最小点个数
    输出：分类簇id
    """
    clusterId = 1
    nPoints = data.shape[1]
    clusterResult = [UNCLASSIFIED] * nPoints
    for pointId in range(nPoints):
        point = data[:, pointId]
        if clusterResult[pointId] == UNCLASSIFIED:
            if expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
                clusterId = clusterId + 1
    return clusterResult, clusterId - 1
def read_file_getnp():
    rf = open("iris.txt", "r", encoding="utf-8")
    allvector = list()
    for line in rf:
        vecotor = line.split(",")[0:-1]
        # print(vecotor)
        floatlis = []
        for str in vecotor:
            floatlis.append(float(str))
        allvector.append(floatlis)
    np1 = np.mat(allvector).transpose()
    return np1
def get_DBSCAN(D,eps,min_sample):
    #D数据集
    #eps 距离的阈值
    #min_sample要成为核心对象所需要的ϵ-邻域的样本数阈值
    a,b=dbscan(D,eps,min_sample)
    print(a,b)
    # numclusters=a.labels_
    # # print(numclusters)
    # plt.scatter(D[:,0],D[:,1],c=y_pred)
    # plt.show()
if __name__=="__main__":
    np1=read_file_getnp()
    # print(np1)
    get_DBSCAN(np1,5,6)
