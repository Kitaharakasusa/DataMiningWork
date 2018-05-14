import numpy as np
import math

c=[] #所有的类
class node:
    cl = ""  # 类别
    # left=0
    # right=0
    data=[]
    children = []  # 子节点
    purity=0
    splitpoint=0 #属性分割值
    splitindex=0 #属性下标
    left=None;
    right=None;
    def __init__(self, cl="",data=[],purity=0):
        # self.left=left
        # self.right=right
        self.cl=cl
        self.data=data
        self.purity=purity
def readfile():
    rf = open("iris.txt", "r", encoding="utf-8")
    allvector = list()
    for line in rf:
        vec=line.strip().split(",")
        lable=vec[-1]
        if lable.strip() not in c:
            c.append(lable.strip())
        allvector.append(vec)

    return allvector

def judgeyi(yi):
    for i in range(len(c)):
        if yi==c[i]:
            return i


def getpurity(ni,n):
    maxnow=0 #最大纯度
    maxindex=0 #最大下标记录
    for i in range(len(ni)):
        if ni[i]/n > maxnow:
            maxnow=ni[i]/n
            maxindex=i
    return maxnow,maxindex
# yj是每一组数据的lable



def CaculatePciDy(Nvi,Nv):
    nowsum=0
    for j in range(len(Nv)):
        nowsum+=Nv[j]
        # print(Nv[j])
    return Nvi/nowsum
def CaculatePciDn(Nvi,Nv,nii,ni):

    nowsum=0
    for j in range(len(Nv)):
        nowsum+=(ni[j]-Nv[j])
    if nowsum==0:
        return nowsum
    return (nii-Nvi)/nowsum
def PciD(Cindex,D):  #获取求得的PciD
    csum=0
    for i in range(len(D)):
        if(D[i][-1]==c[Cindex]):
            csum+=1
    return csum/len(D)
def HDYN(Dyn,PicyYn):
    res = 0
    for i in range(len(c)):
        a = PicyYn[i]
        # print(a)
        if a == 0:
            continue
        res -= a * math.log(a, 2)
    return res
def HD(D):
    res = 0
    for i in range(len(c)):
        a = PciD(i,D)
        print("自己算的Pcidy", a)
        if a==0:
            continue
        res -= a * math.log(a, 2)

    return res
def Gain(D,Dy,Dn,PciDy,PciDn):
    n=len(D)
    ny=len(Dy)
    nn=len(Dn)
    res=HD(D)-((ny/n)*HD(Dy)+(nn/n)*HD(Dn))
    return res

def EVALUATE_NUMERIC_ATTRIBUTE9(D,Xj):
    PciDy = [0] * len(c)
    PciDn = [0] * len(c)
    #这里的Xj就是属性的下标
    Nv=[0]*len(c)
    D.sort(key=lambda d:d[Xj])
    M=set() #set of midpoint
    ni=[0]*len(c)   #ni<-0 统计各个类别的纯度
    for i in range(len(c)):
        for j in range(len(D)-1):
            if D[j][-1]==c[i]:
                ni[i]+=1
            if D[j+1][Xj]!=D[j][Xj]: #求解分割值并保存
                v=(D[j+1][Xj]+D[j][Xj])/2
                M.add(v)
                for x in range(len(c)):
                    if D[j][Xj]<v and D[j][-1]==c[i]:
                        Nv[x] = ni[x]
                    # print("ni[i]",ni[i])
        if D[len(D)-1][-1]==c[i]:
            ni[i]+=1
    print("Nv", Nv, "ni", ni)
    vxing=0
    scorexing=0

    for v in M: #遍历所有的分割值，并根据特定函数求分割值的得分
        for i in range(len(c)):
            PciDy[i]=CaculatePciDy(Nv[i],Nv)
            # print("Nv",Nv,"ni",ni)
            PciDn[i]=CaculatePciDn(Nv[i],Nv,ni[i],ni)
        print("Pcidy",PciDy,"  ",PciDn)
        NowDy=[]
        NowDn=[]
        for index in range(len(D)):
            if(D[index][Xj]<=v):
                NowDy.append(D[index])
            else:
                NowDn.append(D[index])

        scoreXxyv=Gain(D,Dy=NowDy,Dn=NowDn,PciDy=PciDy,PciDn=PciDn)
        if scoreXxyv>scorexing:
            vxing=v
            scorexing=scoreXxyv

    return vxing,scorexing

def Decision_tree(D,yita,pi,nowroot):
    # nowroot=nowroo

    n=len(D) #patition size
    ni=[0]*len(c)
    for i in range(len(c)):
       for j in range(n):
           if D[j][-1]==c[i]: #yj=ci size of class ci
                ni[i]+=1
    putityD,index=getpurity(ni,n)
    if n<=yita or putityD>=pi: #满足条件
        cxing=c[index] #majority class
        nowroot.cl=cxing
        nowroot.data=D
        nowroot.purity=putityD
        print(D)
        print("111",nowroot.cl)
        print("222",nowroot.splitpoint)
        #构造成叶节点 终止
        return

    splitponit=0 #这个点是个具体的值
    splitponitindex=0 #这个参数记录具体是哪个属性
    scorexing=0
    for i in range(len(D[0])-1):
        v,score=EVALUATE_NUMERIC_ATTRIBUTE9(D,i)
        if score>scorexing:
            splitponit=v
            splitponitindex=i
            scorexing=score

    nowroot.splitpoint=splitponit
    nowroot.splitindex=splitponitindex
    print("333",nowroot.splitindex)
    Dy=[]
    Dn=[]
    #// partition D into DY and DN using split point∗, and call recursively
    for i in range(len(D)):
        if D[i][splitponitindex]<=splitponit:
            Dy.append(D[i])
        else:
            Dn.append(D[i])


    nowroot.left=node()
    nowroot.right=node()

    Decision_tree(Dy,yita,pi,nowroot.left)
    Decision_tree(Dn,yita,pi,nowroot.right)



def printtree(rootnode):
    if (len(rootnode.children))!=0:
        for child in rootnode.children:
            print(child.cl)
            print(child.splitpoint)
            printtree(child)
    else:
        return

def printt(root):
    if root is None:
        return
    if root.cl=="":
        print("this is a partition point  the index and splitpoint",root.splitindex," ",root.splitpoint)
    else:
        print("this is a leaf point  the class and purity",root.cl," ",root.purity)
    printt(root.left)
    printt(root.right)
if __name__=="__main__":

    D=readfile()
    print(D)
    for i in range(len(D)):
        for j in range(len(D[0])-1):
            D[i][j] = (float(D[i][j]))

    rootnode=node()
    Decision_tree(D,5,0.95,rootnode)
    print("_____________")
    printt(rootnode)
