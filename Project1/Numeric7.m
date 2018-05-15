covmatrix=cov(magic04);
varimax=max(max(covmatrix))%找出最大值%
[xmax,ymax]=find(covmatrix==max(max(covmatrix)))%找出最大值所在位置%
varimin=min(min(covmatrix))%找出最小值%
[xmin,ymin]=find(covmatrix==min(min(covmatrix)))%找出最小值所在位置%
