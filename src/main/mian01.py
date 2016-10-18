# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月12日

@author: xsh
'''
from domain.Singleton import Singleton_Instance
from process.Process import Read
from process.Process import Write
from process.Process import Process
# import re

file = '../../corpus/test.lsnp'
model = Singleton_Instance.model_Instance
read = Read(file)
process = Process()
all_lines = read.read()
all_qu,ids = process.getAllTitles(all_lines)
all_q2v,q2v_ids = process.allTitle2VecModel(all_qu,ids)
# print(all_q2v)
for i in range(len(all_q2v)):
    print(all_q2v[i])
# print()
# 
# print(re.sub(r'[\[\]]', '', str(all_q2v[97][0])))
# all_q2v[98]
# print(re.sub(r'[\[\]]', '', str(all_q2v[98][0])))
write = Write('../../corpus/vector1') 
write.writeLines(all_q2v,q2v_ids)

print('ok')



