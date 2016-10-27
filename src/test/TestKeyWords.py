#-*- encoding=utf-8 -*-  
'''
Created on 2016年10月27日

@author: xsh
'''
from process.KeyWords import getSim,getSimWord2Vec,findStr
words = 'What contemptible scoundrel stole the cork from my lunch ?'
pos = 'VB PRP JJ NN DT NN adv ADJ NN .'
w, p = findStr(words, pos)
# print(w)
# print(p)
print('+++++++++++++++++++++++')
for i in range(len(w)):
    sim = getSim(w[i], p[i])
    print(sim)
    if len(sim) != 1:
        for i in range(0, len(sim)):
            print(words.replace(sim[0], sim[i]))
    else:
        print(words)
print('==========================================+++++++++')
    
for i in w:
    tep = getSimWord2Vec(i)
    print(i)
    for j in tep:
        str=' '.join(i)
        print(words.replace(str,j))