irisQ=zeros(150,10);%����150*10�������%
for i=1:150%��forѭ������ÿ������x������ӳ��Ľ��%
    irisQ(i,:)=[iris(i,1)^2,iris(i,2)^2,iris(i,3)^2,iris(i,4)^2,sqrt(2)*iris(i,1)*iris(i,2),sqrt(2)*iris(i,1)*iris(i,3),sqrt(2)*iris(i,1)*iris(i,4),sqrt(2)*iris(i,2)*iris(i,3),sqrt(2)*iris(i,2)*iris(i,4),sqrt(2)*iris(i,3)*iris(i,4)];
end
u1=mean(irisQ);%��mean()���������ÿһ�еľ�ֵ%
x1=ones(150,1);%����һ��150�У�1�е�ȫ1����%
y1=x1*u1;%���������ֵ%
irisQ_z=irisQ-y1;%��ԭʼ�����ȥ������ֵ���ľ���õ����Ļ�����%
irisQ_n=mapminmax(irisQ_z,0,1)%��׼��%


