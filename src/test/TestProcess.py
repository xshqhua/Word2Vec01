# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月12日

@author: xsh
'''
from domain.Singleton import *
from process.Process import *
import numpy as np
from numpy import *
model = Singleton_Instance.model_Instance
q2v1 = Process().title2VecModel('my name is')
q2v2 = Process().title2VecModel('what is you name')

# print(q1)
# print(type(q1))
q2m1 = Calculate().calculate(q2v1,normalize=0)
q2m2 = Calculate().calculate(q2v2,normalize=0)
sim=Similty().cosine(q2m1, q2m2)
print(q2m1)
print(q2m2)
print(sim)