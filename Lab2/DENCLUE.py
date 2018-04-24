from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt

epsilon=math.e
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
    np1 = np.array(allvector)
    return np1

def fx(Xxing,D,h):
    sumvalue=0
    for i in range(D.shape[0]):
        xi=D[i]
        sumvalue+=Guassian_kernel(Xxing,xi,h)
    # print("fx",sumvalue/(D.shape[0]*pow(h,D.shape[1])))
    return sumvalue/(D.shape[0]*pow(h,D.shape[1]))


def Guassian_kernel(xt,xi,h):
    res=pow(epsilon,-pow(np.linalg.norm(xt-xi),2)/(2*pow(h,2)))
    # print("res",res)
    return res
def caculate_Guassian(xt,D,h):
    fenzi=0
    fenmu=0
    for i in range(D.shape[0]):
        fenzi+=(Guassian_kernel(xt,D[i],h)*D[i])
        fenmu+=Guassian_kernel(xt,D[i],h)

    return fenzi/fenmu
def FINDATTRACTOR(x,D,h,eps):
    t=0
    xt=x
    xt2=x
    while(True):
        xt=xt2
        xt2=caculate_Guassian(xt,D,h)
        if(np.linalg.norm(xt2-xt)<=eps):

            return xt2
    return xt2
def showpicture(clusterdict):
    scatterColors = ['black', 'blue', 'green', 'yellow', 'red', 'purple', 'orange', 'brown']
    for i in  range(len(clusterdict)):
        nowlisx=[]
        nowlisy=[]
        nowls=clusterdict[str(i)]
        for point in nowls:
            nowlisx.append(point[0])
            nowlisy.append(point[1])
        plt.scatter(nowlisx,nowlisy,c=scatterColors[i])
    plt.show()

def DENCLUE(D,h,kexi,eps):
    A=list()
    R=dict()
    for i in range(D.shape[0]):
        x=D[i]
        Xxing=FINDATTRACTOR(x,D,h,eps)
        # print("atrcor",Xxing)
        # print("type",type(Xxing))
        # print(list(Xxing))
        Xxingli=list(Xxing)
        if fx(Xxing,D,h)>=kexi:
            A.append(Xxingli)
            if str(Xxingli) not in R.keys():
                a=[]
                a.append(x)
                R[str(Xxingli)]=a
            else:
                a= R[str(Xxingli)]
                a.append(x)
                R[str(Xxingli)] = a

     #eps1 距离的阈值
    #min_sample要成为核心对象所需要的ϵ-邻域的样本数阈值
    eps1=0.1
    min_sample=2
    a=DBSCAN(eps=eps1,min_samples=min_sample)
    HC=a.fit_predict(np.mat(A))#dbscan聚类结果
    clusterset=set()
    clusterdict=dict()
    for i in range(len(HC)):
        if(HC[i]!=-1):
            clusterset.add(HC[i])
            if str(HC[i]) not in clusterdict.keys():
                a=[]
                a.append(A[i])
                clusterdict[str(HC[i])]=a
            else:
                a=clusterdict[str(HC[i])]
                a.append(A[i])
    print("number of clusters",len(clusterdict.keys()))
    for key in R.keys():
        print("density attracotr",key)
        print("atracted point",R[key])

    for i in clusterdict.keys():
        ls = clusterdict[i]
        for x in clusterdict[i]:
            if str(x) in R.keys():
                for z in R[str(x)]:
                    ls.append(z)
        clusterdict[i]=ls

    for i in clusterdict.keys():
        print('clusterres', i)
        print('set of point in the cluster', clusterdict[i])
    showpicture(clusterdict)
if __name__=="__main__":
    D=read_file_getnp()
    h=0.3
    kexi=8
    eps=0.0001
    DENCLUE(D,h,kexi,eps)