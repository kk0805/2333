vari=[];
for i=1:10
   vari=[vari;var(magic04(:,i))];%用for循环计算出每列的方差%
end
varimax=max(vari)%找出最大值%
locmax=find(vari==max(vari))%找出最大值所在位置%
varimin=min(vari)%找出最小值%
locmin=find(vari==min(vari))%找出最小值所在位置%