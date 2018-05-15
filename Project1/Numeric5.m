[mu,sigma]=normfit(z1);%z1为高斯分布，因此求出z1的概率密度函数的参数值%
[n,x]=hist(z1,19020);
y=normpdf(x,mu,sigma);%求出概率密度函数中每个x对应的y值%
plot(x,y,'r-')%画出图像%