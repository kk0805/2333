irisQ=zeros(150,10);%定义150*10的零矩阵%
for i=1:150%用for循环计算每个向量x非线性映射的结果%
    irisQ(i,:)=[iris(i,1)^2,iris(i,2)^2,iris(i,3)^2,iris(i,4)^2,sqrt(2)*iris(i,1)*iris(i,2),sqrt(2)*iris(i,1)*iris(i,3),sqrt(2)*iris(i,1)*iris(i,4),sqrt(2)*iris(i,2)*iris(i,3),sqrt(2)*iris(i,2)*iris(i,4),sqrt(2)*iris(i,3)*iris(i,4)];
end
u1=mean(irisQ);%用mean()计算矩阵中每一列的均值%
x1=ones(150,1);%定义一个150行，1列的全1矩阵%
y1=x1*u1;%求出样本均值%
irisQ_z=irisQ-y1;%用原始矩阵减去样本均值数的矩阵得到中心化矩阵%
irisQ_n=mapminmax(irisQ_z,0,1)%标准化%


