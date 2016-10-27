# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月11日

@author: xsh
'''
from gensim.models import Word2Vec;
from scipy.stats.mstats_basic import mode
import nltk
class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  
    
class Singleton_Instance(Singleton):
    model_Instance = Word2Vec.load_word2vec_format('E:\\wordvectors\\EN.glove.6B.300d.bin', binary=True);
    nk = nltk
# class Label_Question_id(Singleton):
    
# model = Singleton_Instance.model_Instance
# v = model['test']
# print(v)
# print(type(v))
# print(v[0])
# vv = []
# for i in v:
#     vv.append(i)
# print(vv)