# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:44:20 2023

@author: jugwu
"""
import re
import string
DATAPATH = "cleanData\\"
def load_sentences(file, num:int=100000):
    with open(DATAPATH + file + ".txt", 'r',encoding="utf-8") as f:
        lines = f.readlines()
    
    data =[]
    count = 0
    for line in lines:
        if count > num:
            break
        long = line
        #clean text
        long = re.sub('\n','',long)
        long = long.translate(str.maketrans('', '', string.punctuation))
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        if long != '\n' and long != '':
            data.append(long)
        
        count += 1
    
    #print(data)
    return data

def load_words(file):
    with open(DATAPATH + file + ".txt", 'r',encoding="utf-8") as f:
        lines = f.readlines()
    
    data =[]
    for line in lines:
        long = line
        #clean text
        long = re.sub('\n','',long)
        long = long.translate(str.maketrans('', '', string.punctuation))
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        if long != '\n' and long != '':
            data.append(long.split(' '))
    
    #print(data)
    return data

#print(load_sentences('text')[2])
#print(load_words('text')[2])