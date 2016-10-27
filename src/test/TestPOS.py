#-*- encoding=utf-8 -*-  
'''
Created on 2016年10月27日

@author: xsh
'''
import nltk
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
wp = nltk.pos_tag(tokens)
words = []
pos = []
for w,p in wp:
    words.append(w)
    pos.append(p)

ws=' '.join(words)
ps=' '.join(pos)
ps=ps.replace('NNS', 'NN')
print(ws)
print(ps)