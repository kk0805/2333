x=ones(19020,1);%定义一个19020行，1列的全1矩阵%
y=x*u;%求出样本均值%
z=magic04-y;%用原始矩阵减去样本均值数的矩阵得到中心化矩阵%
E=(z'*z)/19020%用中心化矩阵的转置乘以中心化矩阵再除以19020得到协方差矩阵%

