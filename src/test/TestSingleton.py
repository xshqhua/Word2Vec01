# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月11日
@author: xsh
'''
from domain.Singleton import Singleton_Instance
import numpy as np

one = Singleton_Instance().model_Instance
two = Singleton_Instance().model_Instance

positive = ['woman', 'king']
negative = ['man']

print(one.most_similar(positive, negative , topn=10, restrict_vocab=None))
print(two.most_similar(positive, topn=10, restrict_vocab=None))

print(one.similarity('woman', 'man'))
print(one.similarity('king', 'queen'))
ve1 = one['computer']

print(ve1)
print(len(ve1))
print(two.most_similar(positive,negative , topn=10, restrict_vocab=None))
print(one.similarity('power','powerful'))
print(one.similar_by_vector(ve1, topn=10, restrict_vocab=None))

str1 = 'my computer name is china'
# vec2dis = [vi for vi in  ]
vec2dis = one[str1.split()]
vec1 = vec2dis[0][1] 
print(vec2dis)

vec2 = vec2dis[:3,:]
vec3 = vec2

print(vec1)
print("=================")
print("=================")
print("=================")
print(vec2)
print(vec3)
print("=================")
print("=================")
print(one['co-worker'])
print(one['rn'])
print('==================')

print(one['medical'])
