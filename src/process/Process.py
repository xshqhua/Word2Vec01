# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月12日

@author: xsh
'''
import re
import math
from scipy.signal.windows import cosine
from domain.Singleton import Singleton_Instance
model = Singleton_Instance.model_Instance
class Read(object):
    '''
    classdocs
    '''     
    def __init__(self, file):         
        '''
        Constructor
        '''
        self.file = file
        
    def read(self):
        file_object = open(self.file, 'r', encoding='utf-8')
        all_lines = file_object.read()
        file_object.close()
        return all_lines.split('\n')
class Write(object):
    def __init__(self, file):
        self.file = file
        self.file_object = open(self.file, 'w+', encoding='utf-8')
        
    def write(self, lines,id):
        if len(lines)>1:
            line = re.sub(r'[\[\]]', '', str(lines[0]))
            self.file_object.write(str(id)+'##'+line + '\n')
        else:
            self.file_object.write(str(id)+'##'+str(lines) + '\n')
                
    def writeLines(self, lines,ids):
        for i in range(len(lines)):
            self.write(lines[i],ids[i])
    def __del__(self):
        self.file_object.close()

class Process(object):
    def getAllTitles(self, all_lines):
#         all_lines = Read('../../corpus/test.lsnp').read()
        question = []
        ids = []
        size=0
        for i in range(1, len(all_lines), 9):
            tep = re.sub(r'( [.])+|-[lr]rb- ', '', all_lines[i])
            question.append(tep)
            ids.append(size)
            size+=1
        return question,ids
    def title2VecModel(self, question):
        res = []
        for stri in question.split():
            if model.__contains__(stri):
                res.append(self.toArray(model[stri]))
            else:
                lower = stri.lower()
                if model.__contains__(lower):
                    res.append(self.toArray(model[lower]))
        
#         print(res)
        return res
    def toArray(self,value):
        vv = []
        for i in value:
            vv.append(i)
        return vv
    def allTitle2VecModel(self, questions,ids):
        res = []
        resIds = []
        i = 0
        for i in range(len(questions)):
            q = questions[i]
            res.append(self.title2VecModel(q))
            resIds.append(ids[i])
        return res,resIds
class Calculate(object):
    def calculate(self, ques2Ve, normalize=0):
        row = len(ques2Ve)
        col = len(ques2Ve[0])
        res1 = []
        for i in range(col):
            sum = 0
            for j in range(row):
                sum += ques2Ve[j][i]
            sum = sum / row
            res1.append(sum)
        if normalize == 0:
            return res1
        else:
            res = []
            sum = 0;
            for num in res1:
                sum += num * num
            sum = math.sqrt(sum)
            for num in res1:
                res.append(num / sum)
            return res
        
class Similty(object):
    def cosine(self, value1, value2):
        v = 0
        v1 = 0
        v2 = 0
        for i in range(len(value1)):
            v += value1[i] * value2[i]
            v1 += value1[i] * value1[i]
            v2 += value2[i] * value2[i]
        return v / (math.sqrt(v1) * math.sqrt(v2))
    def cosineList(self, value1, value2):
        res = []
        for i in range(len(value2)):
            res.append(cosine(value1, value2[i]))
        return res
    def sorted(self, keyValue):
        dic = {}
        for i in range(len(keyValue)):
            dic[keyValue[i]:str(i)]
        return sorted(dic.items(), key=lambda asd:asd[0], reverse=True)
        
        
        
         
# vv = []
# vv.append('1\n')
# vv.append('1\n')
# print(vv)
# Write('./data').write(vv)

# model = Si

        
    
# ques = Process(all_lines).getTitle()
# print(ques)

# for i in range(1,len(all_lines),9):
#     print(all_lines[i])





