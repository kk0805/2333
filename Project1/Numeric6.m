vari=[];
for i=1:10
   vari=[vari;var(magic04(:,i))];%��forѭ�������ÿ�еķ���%
end
varimax=max(vari)%�ҳ����ֵ%
locmax=find(vari==max(vari))%�ҳ����ֵ����λ��%
varimin=min(vari)%�ҳ���Сֵ%
locmin=find(vari==min(vari))%�ҳ���Сֵ����λ��%