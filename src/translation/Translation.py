# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月19日

@author: xsh
'''
# 这是根据统计翻译模型来来计算的翻译概率
from process.ReadWrite import Read
from domain.Question import Question
import re
class Questions(object):
    def __init__(self, file):
        self.lines = Read(file).read()
    def getAllTitle(self):
        self.question = []
        ids = []
        size = 0
        for i in range(1, len(self.lines), 9):
            tep1 = re.sub(r'( [.])+|-[lr]rb- ', '', self.lines[i])
            tep2 = re.sub(r'( [.])+|-[lr]rb- ', '', self.lines[i + 4])
            self.question.append(Question(tep1, tep2))
        return self.question

class Probability(object):
    def __init__(self):
        self.lama = 1
        
    def wordInQuestion(self, word, question, flag=0):
        count = 0
        words = question.title.split(' ')
        for w in words:
            if word == w:
                count = count + 1
                
        if flag == 1:
            words = question.answer.split(' ')
            for w in words:
                if word == w:
                    count = count + 1
                    
        return count
    def wordInAllQuestion(self, word, question, flag=0):
        count = 0
        for q in question:
            count = count+self.wordInQuestion(word, q, flag)
        return count
    

    
questions = Questions('../../corpus/test.lsnp').getAllTitle()
# print(questions)
for i in questions:
    print(i.title)
    print(i.answer)
    print()
print(len(questions))
print(Probability().wordInAllQuestion('school', questions,0))
print('w'=='wo')