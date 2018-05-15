k=iris*iris';%输入空间的kernel matrix
K=k.^2
u=mean(K);%用mean()计算矩阵中每一列的均值%
x=ones(150,1);%定义一个150行，1列的全1矩阵%
y=x*u;%求出样本均值%
K_z=K-y;%用原始矩阵减去样本均值数的矩阵得到中心化矩阵%
K_n=mapminmax(K_z,0,1)%标准化%







