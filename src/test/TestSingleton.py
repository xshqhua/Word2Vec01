#-*- encoding=utf-8 -*-  
'''
Created on 2016年10月18日

@author: xsh
'''
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
positive1 = ['woman','woman','woman','woman', 'king']
positive2 = two['woman','woman','woman','woman', 'king']
print(len(positive2))
# aa = two[positive2[0]]
# for i in range(1,len(positive2)):
#     aa=aa+two[positive2[i]]
    
negative = ['man']

print(one.most_similar(positive, negative , topn=10, restrict_vocab=None))
print(two.most_similar(positive, topn=10, restrict_vocab=None))
print(two.most_similar(positive1, topn=10, restrict_vocab=None))
print(two.most_similar(positive2, topn=10, restrict_vocab=None))

