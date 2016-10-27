# -*- encoding=utf-8 -*-  
'''
Created on 2016年10月19日

@author: xsh
'''
import re
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
        
    def write(self, lines, id):
        if len(lines) > 1:
            line = re.sub(r'[\[\]]', '', str(lines[0]))
            self.file_object.write(str(id) + '##' + line + '\n')
        else:
            self.file_object.write(str(id) + '##' + str(lines) + '\n')
                
    def writeLines(self, lines, ids):
        for i in range(len(lines)):
            self.write(lines[i], ids[i])
    def __del__(self):
        self.file_object.close()
