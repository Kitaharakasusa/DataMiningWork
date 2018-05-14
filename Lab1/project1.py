import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def read_file_getnp():
    rf = open("magic04.txt", "r", encoding="utf-8")#打开文件
    allvector = list() #结果数组
    for line in rf:#遍历文件
        vecotor = line.split(",")[0:-1] #取值，去除最后的lable
        floatlis = []
        for str in vecotor:
            floatlis.append(float(str))
        allvector.append(floatlis)
    np1 = np.array(allvector) #读取后转换成numpy矩阵
    return np1
def Compute_mean_vector():
    np1=read_file_getnp()
    mea=np1.mean(axis=0)
    return mea


def Compute_Con_Matrix_inner():
    np1=read_file_getnp() #读取文件转换矩阵
    mean=Compute_mean_vector() #计算平均值
    Zmatrix=np1-(np.ones([np1.shape[0],1])*mean) #中心化
    conmatrix=np.asmatrix(Zmatrix.T)*np.asmatrix(Zmatrix)/np1.shape[0] #通过内积的方法计算协方差矩阵
    print(conmatrix)
def Compute_Con_Matrix_outer():
    np1 = read_file_getnp()   #读取文件转换矩阵
    mean = Compute_mean_vector()#计算平均值
    Zmatrix = np1 - (np.ones([np1.shape[0], 1]) * mean)#中心化
    a=np.zeros([Zmatrix.shape[1],Zmatrix.shape[1]])#通过求外积的方法计算协方差矩阵
    for i in range(Zmatrix.shape[0]):
        b=np.outer(Zmatrix[i],Zmatrix[i].T)
        a+=b
    print(a/Zmatrix.shape[0])


def Correlation_X1_X2():
    np1=read_file_getnp() #读取文件转换矩阵
    aftersplit=np.hsplit(np1,np1.shape[1])#按列分割
    #组合一下,得到只有属性X1 X2的矩阵
    x1x2=np.hstack((aftersplit[0],aftersplit[1])) #组合成矩阵
    mean=x1x2.mean(axis=0) #求均值
    u1=mean[0]
    u2=mean[1]
    xigema12=0.0
    xigema1=0.0
    xigema2=0.0
    for i in range(x1x2.shape[0]):
        xigema12+=((x1x2[i][0]-u1)*(x1x2[i][1]-u2))
        xigema1+=pow(x1x2[i][0]-u1,2)
        xigema2+=pow(x1x2[i][1]-u2,2)
    cosvalue=xigema12/np.sqrt(xigema1*xigema2)

    x=[]
    y=[]
    for i in range(x1x2.shape[0]):
        x.append(x1x2[i][0])
        y.append(x1x2[i][1])
    plt.scatter(x,y)
    plt.show()
    print(cosvalue)
def X1_normal_density_function():
    np1=read_file_getnp() #读取矩阵
    x1=np.hsplit(np1,np1.shape[1])[0] #分割矩阵
    mu=np.mean(x1) #属性1 求均值
    sigma=np.std(x1) #属性1 求标准差
    print(sigma)
    print(mu)
    mulaji=stats.norm.pdf(x1,mu,sigma)
    x=[]
    for i in range(x1.shape[0]):
        x.append(x1[i])
    y=[]
    for i in range(mulaji.shape[0]):
        y.append(mulaji[i])
    plt.scatter(x,y)
    plt.show()

    print(type(mulaji))
    print(mulaji)
def get_max_min_variance():
    np1=read_file_getnp()
    resli=[]
    for i,lis in enumerate(np.hsplit(np1,np1.shape[1])):
        print(str(i)+":")
        print(np.var(lis)) #求方差
        resli.append(np.var(lis))
    print("max",max(resli))
    print("min",min(resli))
    # np2=np.split(np1,)
def get_max_min_covariance():
    np1=read_file_getnp()
    mat=np.cov(np1.T) #求协方差矩阵
    nowmax=mat[0][0] #最大记录
    nowmin=mat[0][0]#最小记录
    #最大最小下标
    maxx=0
    maxy=0
    minx=0
    miny=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]>nowmax:
                nowmax=mat[i][j]
                maxx=i
                maxy=j
            if nowmin>mat[i][j]:
                nowmin=mat[i][j]
                minx=i
                miny=j
    print("max",nowmax," ",maxx,maxy)
    print("min",nowmin," ",minx,miny)
    print(mat)
    # arrlist=np.hsplit(np1,np1.shape[1])
    # nowlist=[]
    # lable=[]
    # reslist=[]
    #
    # for i in range(len(arrlist)):
    #     for j in range(i,len(arrlist)):
    #         if j-i>=1:
    #             lable.append(str(i)+"and"+str(j))
    #             nowlist.append(np.hstack((arrlist[i],arrlist[j])))
    # for i in range(len(nowlist)):
    #     print(lable[i])
    #     reslist.append(np.cov(np.array(nowlist[i]).T))
    # maxlable=0
    # minlable=0
    # maxcov=None
    # mincov=None
    # for i in range(len(reslist)):
    #     if i==0:
    #         maxcov=reslist[i]
    #         mincov=reslist[i]
    #     else:
    #         if reslist[i]>maxcov:
    #             maxcov=reslist[i]
    #             maxlable=i
    #         if reslist[i]<mincov:
    #             mincov=reslist[i]
    #             minlable=i
    # print(lable[maxlable]," ",lable[minlable])
    # print(len(nowlist))
if __name__=="__main__":
    # print(Compute_mean_vector())
    # Compute_Con_Matrix_outer()
    # Correlation_X1_X2()
    # Compute_Con_Matrix_inner()
    get_max_min_covariance()
    # get_max_min_variance()
    # np1=np.array([12,14,18,23,27,28,34,37,39,40])
    # print(np.std(np1))
    # X1_normal_density_function()
    # Correlation_X1_X2()
    # Compute_mean_vector()
    # a=np.array([[0, 1, 2],[3, 4, 5],[6,7,8]])
    # lista=np.hsplit(a,a.shape[1])
    # b=lista[0]
    # print(b)
    # c=lista[1]
    # print(c)
    # print(np.hstack((b,c)))
