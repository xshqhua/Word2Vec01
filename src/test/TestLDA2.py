# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月18日

@author: xsh
'''
import numpy as np
import lda
X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
print(X.shape)
model = lda.LDA(n_topics=20, n_iter=100, random_state=1)
model.fit(X) 
topic_word = model.topic_word_
# print(topic_word)
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))


# doc_topic = model.doc_topic_
# for i in range(10):
#     print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))
# print(doc_topic[i])