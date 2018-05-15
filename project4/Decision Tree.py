import os
import types
import math
import sys
import numpy as np

c=[]##用数组记录

class node:
    c_label=""##类别
    data=[]
    purity=0
    children=[]##定义子节点
    splitpoint_star=0##分割点
    split_index=0##分割点下标值
    left=None
    right=None
    def __init__(self,c_label="",data=[],purity=0):
        self.c_label=c_label
        self.data=data
        self.purity=purity

def readFile():##读取txt中的数据
    f = open("iris.txt", "r", encoding="utf-8")
    F = []
    for line in f:
        s = line.strip().split(",")
        label = s[-1]
        if label.strip() not in c:
            c.append(label.strip())
        F.append(s)
    return F


def Purity(ni,n):##计算纯净度
    temp=0
    temp_index=0##标记下标
    for i in range(len(ni)):
        if ni[i]/n > temp:
            temp=ni[i]/n##找出最大的一类的点
            temp_index=i
    return temp,temp_index

def P_ciDY(nvi,nv):##Y分支的可能性
    sum = 0
    for j in range(len(nv)):
        sum+=nv[j]##所有点之和
    ans=nvi/sum##Y中的点除以所有点
    return ans

def P_ciDN(nvi,nv,nii,ni):##N分支的可能性
    sum=0
    for j in range(len(nv)):
        sum+=ni[j]-nv[j]##所有点减去Y中的点
    if sum==0:
        return 0
    return (nii-nvi)/sum##N中的点除以所有点

def P_ciD(c_index,D):##ci在D中的可能性
    c_sum=0
    for i in range(len(D)):
        if D[i][-1]==c[c_index]:##通过标签判断属于哪一类
            c_sum+=1
    return c_sum/len(D)##该类的点数除以总点数

def H(D):##D中ci的熵函数
    H_sum = 0
    for j in range(len(c)):
        if P_ciD(j,D)==0:
            continue
        H_sum-=P_ciD(j,D)*math.log(P_ciD(j,D),2)
    return H_sum

def Gain(D,DY,DN):##信息增益函数
    n=len(D)
    nY=len(DY)
    nN=len(DN)
    gain=H(D)-nY/n*H(DY)-nN/n*H(DN)
    return gain

def Evalute_Numeric_Attribute(D,xi):##数字属性
    nv=[0]*len(c)
    D=sorted(D,key=lambda x:x[xi])##对每个点的数字属性进行排序
    M=set()
    ni=[0]*len(c)##类的个数，初始化
    for j in range(len(D)-1):##对D中的每个点，除最后一个
        for i in range(len(c)):  ##判断其属于哪一类
            if D[j][-1]==c[i]:
                ni[i]+=1##找到该类，然后点数加一
            if D[j+1][xi]!=D[j][xi]:##与下一个属性不同时
                v=(D[j+1][xi]+D[j][xi])/2##计算中间点
                M.add(v)##将其加入集合
            # print(M)
            for i in range(len(c)):##属于ci且xj<v的点的个数
                    nv[i]=ni[i]

    if D[len(D)-1][-1]==c[i]:
        ni[i]+=1

    v_star=0
    score_star=0
    p_ciDY=[0]*len(c)
    p_ciDN=[0]*len(c)
    for v in M:##对集合中的每个midpoint进行判断
        for i in range(len(c)):
            p_ciDY=P_ciDY(nv[i],nv)##属于ci类且为Y的可能性
            p_ciDN=P_ciDN(nv[i],nv,ni[i],ni)##属于ci类且为N的可能性
        DY=[]##记录Y中的点
        DN=[]##记录N中的点
        for j in range(len(D)):
            if D[j][xi]<=v:##小于V即为Y
                DY.append(D[j])##插入列表中
            else:
                DN.append(D[j])
    score_minv=Gain(D,DY,DN)##算出得分
    if score_minv>score_star:##让score_star为最大得分
        v_star=v
        score_star=score_minv
    return v_star,score_star


def decisionTree(D,leaf_size,pi,root):##决策树主函数
    n=len(D)
    ni=[0]*len(c)
    for i in range(len(c)):##对D中的每个点进行判断，看它属于哪一类
        for j in range(n):
            if D[j][-1]==c[i]:
                ni[i]+=1
    purity_D,purity_index=Purity(ni,n)##计算纯净度
    print("purity",purity_D)##输出纯净度
    if n<=leaf_size or purity_D>pi:##判断条件，如果小于叶节点数或纯净度大于要求就转化为叶节点
        c_star=c[purity_index]
        # print("purity",purity_D)
        root.c_label=c_star
        root.data=D
        root.purity=purity_D
        return

    splitpoint_star=0
    score_star=0
    split_index=0
    for i in range(len(D[0])-1):##对每个数字属性进行评估打分
        v,score=Evalute_Numeric_Attribute(D,i)
        if score>score_star:##让score为最大得分
            score_star=score
            splitpoint_star=v
            split_index=i
    root.splitpoint_star=splitpoint_star
    root.split_index=split_index
    print("internal node",v)##输出internal node
    Dy=[]
    Dn=[]
    for i in range(len(D)):##将Y和N中的点分别存入列表中
        if D[i][split_index]<=splitpoint_star:
            Dy.append(D[i])
        else:
            Dn.append(D[i])

    Ynode=node
    Nnode=node
    root.left=Ynode##左子节点
    root.right=Nnode##右子节点
    print("Dy",len(Dy),Dy)##输出每次的划分
    print("Dn",len(Dn),Dn)
    decisionTree(Dy,leaf_size,pi,root.left)##嵌套调用
    decisionTree(Dn,leaf_size,pi,root.right)

if __name__ == "__main__":
    D=readFile()##读取txt中的数据
    for i in range(len(D)):##将数据类型转换为float
        for j in range(len(D[0])-1):
            D[i][j]=float(D[i][j])##D中的数字属性为字符串类型，将其转换为floa类型
    root=node
    decisionTree(D,5,0.95,root)

