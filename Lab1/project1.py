import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
def read_file_getnp():
    rf = open("magic04.txt", "r", encoding="utf-8")
    allvector = list()
    for line in rf:
        vecotor = line.split(",")[0:-1]
        floatlis = []
        for str in vecotor:
            floatlis.append(float(str))
        allvector.append(floatlis)
    np1 = np.array(allvector)
    return np1
def Compute_mean_vector():
    np1=read_file_getnp()
    mea=np1.mean(axis=0)
    return mea


def Compute_Con_Matrix_inner():
    np1=read_file_getnp()
    mean=Compute_mean_vector()
    Zmatrix=np1-(np.ones([np1.shape[0],1])*mean)
    conmatrix=np.asmatrix(Zmatrix.T)*np.asmatrix(Zmatrix)/np1.shape[0]
    # print(conmatrix)

    realconmatrix=np.cov(np1)

    print(conmatrix==realconmatrix)
def Compute_Con_Matrix_outer():
    np1 = read_file_getnp()
    mean = Compute_mean_vector()
    Zmatrix = np1 - (np.ones([np1.shape[0], 1]) * mean)
    Zmatri=Zmatrix.T
    a=np.ndarray
    for i in range(Zmatri.shape[0]):

        b=np.outer(Zmatri[i],Zmatri[i].reshape([1,Zmatri[0].shape[0]]))
        print(Zmatri[0].shape)
        print(Zmatri[1].shape)
        print(type(b))
        print(b.shape)
        # print(a+b)
    print(a)

def Correlation_X1_X2():
    np1=read_file_getnp()
    aftersplit=np.hsplit(np1,np1.shape[1])
    #组合一下,得到只有属性X1 X2的矩阵
    x1x2=np.hstack((aftersplit[0],aftersplit[1]))
    mean=x1x2.mean(axis=0)
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
    np1=read_file_getnp()
    x1=np.hsplit(np1,np1.shape[1])[0]
    mu=np.mean(x1)
    sigma=np.std(x1)
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
    for i,lis in enumerate(np.hsplit(np1,np1.shape[1])):
        print(str(i)+":")
        print(np.var(lis))
    # np2=np.split(np1,)
def get_max_min_covariance():
    np1=read_file_getnp()
    arrlist=np.hsplit(np1,np1.shape[1])
    nowlist=[]
    lable=[]
    for i in range(len(arrlist)):
        for j in range(i,len(arrlist)):
            if j-i>=1:
                lable.append(str(i)+"and"+str(j))
                nowlist.append(np.hstack((arrlist[i],arrlist[j])))
    for i in range(len(nowlist)):
        print(lable[i])
        print(np.cov(nowlist[i]))
    print(len(nowlist))
if __name__=="__main__":
    get_max_min_covariance()
    # get_max_min_variance()
    # np1=np.array([12,14,18,23,27,28,34,37,39,40])
    # print(np.std(np1))
    # X1_normal_density_function()
    Correlation_X1_X2()
    # Compute_mean_vector()
    # Compute_Con_Matrix_outer()
    # a=np.array([[0, 1, 2],[3, 4, 5],[6,7,8]])
    # lista=np.hsplit(a,a.shape[1])
    # b=lista[0]
    # print(b)
    # c=lista[1]
    # print(c)
    # print(np.hstack((b,c)))
