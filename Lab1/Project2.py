import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
from sklearn import preprocessing

def read_file_getnp():
    rf = open("iris.txt", "r", encoding="utf-8")
    allvector = list()
    for line in rf:
        vecotor = line.split(",")[0:-1]
        floatlis = []
        for str in vecotor:
            floatlis.append(float(str))
        allvector.append(floatlis)
    np1 = np.array(allvector)
    return np1

def get_Matrix_K():
    np1=read_file_getnp() #数据获取
    print(np1.shape)
    np2=np.zeros((np1.shape[0],np1.shape[0])) #保存结果
    for i in range(np2.shape[0]):
        for j in range(np2.shape[1]):
            np2[i][j]=math.pow(np.inner(np1[i],np1[j]),2) #取内积
    #means=np2.mean(axis=0)

    # print(means)
    # std=np.std(np2,axis=0)
    # print("Std",std)
    # print(means)
    # print(means.shape)
    # print(np2)
    # np2=(np2-np.ones([np2.shape[0],1])*means)
    # print(np2)
    # np2=preprocessing.normalize(np2)

    #centered
    # print("lennp2",len(np2))
    T1=np.eye(len(np2))-np.ones((len(np2),len(np2)))*1/len(np2)
    # print("T1",T1)
    c_k=T1 @ np2 @ T1
    # print("c-k",c_k)
    #normalized
    w=np.diag(np.power(np.diagonal(c_k),-0.5))
    res=w @ c_k @w
    print("K",res)

def Transfrom_Xto_feature():
    np1=read_file_getnp()
    veclis=np.vsplit(np1,np1.shape[0]) ##分割矩阵，方便运算，按行分割
    for i in range(len(veclis)):
        veclis[i]=veclis[i][0]  #去括号
    feature=[]
    for i in range(len(veclis)):  #公式实现
        nowfea=[]
        for j in range(len(veclis[i])):
            nowfea.append(pow(veclis[i][j],2)) #取平方
        for k in range(len(veclis[i])):
            for x in range(k+1,len(veclis[i])): #去根号2倍组合
                if x-k>=1:
                    nowfea.append(math.sqrt(2)*veclis[i][k]*veclis[i][x])
        # print(nowfea)
        feature.append(nowfea)


    means = np.mean(feature, axis=0)
    #centered
    feature=feature-np.mean(feature,axis=0)
    #normalized
    feature=preprocessing.normalize(feature)
    print("feature",feature)

    return feature

def Verify():
    lis=Transfrom_Xto_feature()
    # print(len(lis))
    res=np.zeros((len(lis),len(lis)))
    for i in range(len(lis)):
        for j in range(len(lis)):
            res[i][j]=np.inner(lis[i],lis[j])
    # means=np.mean(res,axis=0)
    print("res",res)
    print(res)
if __name__=="__main__":
    get_Matrix_K()
    print("______________---------------_______________")
    Verify()
    # print("______________---------------_______________")
