[mu,sigma]=normfit(z1);%z1Ϊ��˹�ֲ���������z1�ĸ����ܶȺ����Ĳ���ֵ%
[n,x]=hist(z1,19020);
y=normpdf(x,mu,sigma);%��������ܶȺ�����ÿ��x��Ӧ��yֵ%
plot(x,y,'r-')%����ͼ��%