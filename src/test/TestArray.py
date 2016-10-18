# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月12日

@author: xsh
'''
import numpy as np
from numpy import *
vect1 = [[i for i in range(10)] for i in range(3)] 
print(vect1)
vect2 = vect1[0][:]
print(vect2)
output = [];
for i1 in range(len(vect1[0])):
    output.append(sum(vect1[j][i1] for j in range(len(vect1))))
print(output)

print('==================')
a = np.array(vect1)
print(a.shape[0])
print(a)
print('++++++++++++++++++')
m1 = mat(a)
print(m1)
print(m1.max())
print(max(m1[:, 2]))
print(m1[:, 2].max())
print(m1[2, :].max())
print(m1[2, :].sum())
print(m1[:, 2].sum())
print('==================')
print(np.max(m1, 0))
print(np.max(m1, 1))
print('++++++++++++++++++')
print(vect1)
print(m1)
print('==================')
# 列值相加
print(m1.sum(0)/4)
# 行值相加
print(m1.sum(1)/5)
