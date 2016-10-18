#-*- encoding=utf-8 -*-  
'''
Created on 2016年10月12日

@author: xsh
'''
dic  = {'0.0':'a','1.2':'b','1.1':'c','8.9':'d'}
print(dic)

print(sorted(dic.items(),key=lambda asd:asd[0],reverse = True))
print(dic)