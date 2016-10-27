# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月26日

@author: xsh
'''

import re
from nltk.corpus import wordnet as wn

words = 'the recruiter know when you be suppose to report . give he a call . p.s. . this question ought to have be in the military board .'
pos = 'DT NN VBZ WRB PRP VBP VBN TO VB . VB PRP DT NN . NN . DT NN MD TO VB VBN IN DT JJ NN .'

ws = words.split(' ')
pattern = re.compile(r'((JJ )?(NN)+)')
 
data = pattern.finditer(pos)

for i in data:
    index = i.span()
    
    str1 = pos[:index[0]]
    str2 = pos[:index[1]]
#     print(str1)
#     print(str2)
    w_pos = pos[index[0]:index[1]]
    print(w_pos)
    index1 = str1.count(' ')
    index2 = str2.count(' ') + 1
    
    print(ws[index1:index2])
    
# for i in ws:
#     for j in wn.synsets(i): # @UndefinedVariable
#         print(j.lemma_names)

print('---------')
w='military'
sim = []
sim.append(w)

for j in wn.synsets(w, wn.ADJ):
#     print(j)
#     print(j.lemma_names())
    for k in j.lemma_names():
        if k not in sim:
            if '_' not in k and '-' not in k and k not in w and w not in k:
                sim.append(k)
# question', 'inquiry', 'enquiry', 'query', 'interrogation'

# print('+++++')
# a = wn.synset('question')
print(sim)

print('=====================')
w='stole'
sim = []
sim.append(w)

for j in wn.synsets(w):
    print(j)
