#-*- encoding=utf-8 -*-  
'''
Created on 2016年10月18日

@author: xsh
'''
import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import  models

train = []
stopwords = codecs.open('../../corpus/English_StopWords.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
fp = codecs.open('../../corpus/test.lsnp','r',encoding='utf8')
for line in fp:
    line = line.split()
    train.append([ w for w in line if w not in stopwords ])
print(train)
dictionary = Dictionary(train)
corpus = [ dictionary.doc2bow(text) for text in train ]
print(corpus[0])
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
# 打印前20个topic的词分布
print(lda.print_topics(20))
# 打印id为20的topic的词分布
print(lda.print_topic(20))
#模型的保存/ 加载
lda.save('zhwiki_lda.model')
lda = models.ldamodel.LdaModel.load('zhwiki_lda.model')


# tt = 'loss of energy , motivation and no interest in work anymore - be it time to through it all in'
# 
# test_doc = list(i for i in tt.split())
# 
# doc_bow = id2word.doc2bow(test_doc)      #文档转换成bow
# doc_lda = lda[doc_bow]                   #得到新文档的主题分布
# #输出新文档的主题分布
# print doc_lda
# for topic in doc_lda:
#     print "%s\t%f\n"%(lda.print_topic(topic[0]), topic[1])
