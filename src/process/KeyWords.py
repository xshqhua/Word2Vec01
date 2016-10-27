# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月26日

@author: xsh
'''

import re
from nltk.corpus import wordnet as wn
from domain.Singleton import Singleton_Instance
from docutils.parsers.rst.directives import flag

def findStr(words, pos):
    ws = words.split(' ')
    pattern = re.compile(r'((JJ )?(NN)+)')
    res = []
    res_pos = []
    data = pattern.finditer(pos)
    for i in data:
        index = i.span()
        str1 = pos[:index[0]]
        str2 = pos[:index[1]]
        res_pos.append(pos[index[0]:index[1]])
        index1 = str1.count(' ')
        index2 = str2.count(' ') + 1
        res.append(ws[index1:index2])
    return res, res_pos
def getSim(word, pos):
    ps = [i for i in pos.split(' ')]
#     print(ps)
#     print(word)
    res = []
    for i in range(len(ps)):
        w = word[i]
        sim = []
        sim.append(w)
        if ps[i].__eq__('JJ'):
            tep = wn.ADJ
        else:
            tep = wn.NOUN
        for j in wn.synsets(w, tep):  # @UndefinedVariable
            for k in j.lemma_names():
                if k not in sim:
                    if '_' not in k and '-' not in k and k not in w and w not in k:
                        sim.append(k)
        res.append(sim)
    res1 = []
    if len(res) == 1:
        return res[0]
    for i in res[0]:
        for j in res[1]:
            k = i + " " + j
            res1.append(k)
    return res1
def getSimWord2Vec(word):
    w2v = Singleton_Instance.model_Instance
    res = []
#     print(word)
#     print(w2v.most_similar(positive=['woman', 'king'], negative=['man']))
# 先判断是不是含有这words
    ws1 = []
    for w1 in word:
        if w2v.__contains__(w1):
            ws1.append(w1)
        elif w2v.__contains__(w1.lower()):
            ws1.append(w1.lower())
            
    if len(ws1) < 1:
        return res
    tep = w2v.most_similar(positive=ws1, negative=[])
#     print(tep[0])

    tep1 = ' '.join(ws1)
    flag =0
    if tep1.title():
        flag=1
    if flag==1:
        for i in range(4):
    #         print(tep[i][0])
            tt = tep[i][0][0].upper()
            tt=tt+tep[i][0][1:]
            res.append(tt)
    else:
        for i in range(4):
        #         print(tep[i][0])
            res.append(tep[i][0])
    return res
def getPos(words):
    nk = Singleton_Instance.nk
    tokens = nk.word_tokenize(words)
    wp = nk.pos_tag(tokens)
#     print('-----')
#     print(wp)
    words = []
    pos = []
    for w, p in wp:
        words.append(w)
        pos.append(p)
    
    ws = ' '.join(words)
    ps = ' '.join(pos)
    ps = ps.replace('NNS', 'NN')
#     print(ws)
#     print(ps)
    return ws, ps

def expendKeywords(words):
    ws, ps = getPos(words)
    w, p = findStr(ws, ps)
#     print(w)
#     print(p)
    print('=====================WordNet=========================')
    for i in range(len(w)):
        sim = getSim(w[i], p[i])
        print(sim)
        if len(sim) != 1:
            for i in range(0, len(sim)):
                print(words.replace(sim[0], sim[i]))
        else:
            print(words)
    print('=====================Word2Vec========================')
    flag = 0
    for i in w:
        tep = getSimWord2Vec(i)
        print(i)
        for j in tep:
            str = ' '.join(i)
            print(words.replace(str, j))
            flag = 1
            
        if flag == 1:
            print()
    if flag == 0:
        print(words)
        
