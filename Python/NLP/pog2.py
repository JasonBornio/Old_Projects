# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:39:12 2023

@author: jugwu
"""

#import torch
import numpy as np
#import time
import re
np.random.seed(0)
DATAPATH = 'data//'
from tqdm import tqdm

class J_AI(object):
    def __init__(self):
        super(J_AI, self).__init__()
        self.long_memory = []
        self.short_memory = []
        self.index_probailities = []
        self.long_mem_weights = []
        self.probs = 0
        self.long_memory.append("///STOP///")
        self.long_mem_weights.append([0])
        self.index_probailities.append(0)
        self.weight_mem = []
        
    def forward(self, string):
        string = re.sub(",","",string)
        #string = re.sub(r".","",string)
        string = re.sub(":","",string)
        string = re.sub(";","",string)
        string = re.sub("-","",string)
        string = re.sub(r"[?]","",string)
        string = re.sub(r"[!]","",string)
        string = string.lower()
        words = string.split()
        
        index_list = []
        
        #add to mem.
        for word in words:
            if word not in self.long_memory:
                self.long_memory.append(word)           
        #print(self.long_memory)
                
        for word in words:
            for i in range(np.size(self.long_memory)):
                if (self.long_memory[i] == word) and (i not in index_list):
                    index_list.append(i)
        #print(index_list)
        
        for num in index_list:
            self.assign_weights(num, index_list)
        
        #print(self.long_mem_weights)
                
        return
    
    def assign_weights(self, num, _list=None):
        size =  len(self.long_memory)

        new_weights = []
        
        if size > num:
            count = 1
            self.index_probailities.append(0.01)
            for pos in _list:
                if pos == num:
                    new_weights.append(0)
                elif pos < num:
                    new_weights.append(-count/1)
                else:
                    new_weights.append(1/count)
                count += 1
            self.long_mem_weights.append(new_weights)
            return
        else:
            count = 1
            self.index_probailities[num] += 0.01
            for pos in _list:
                if pos == num:
                    new_weights.append(0)
                elif pos < num:
                    new_weights.append(-count/1)
                else:
                    new_weights.append(1/count)
                count += 1
            self.long_mem_weights = self.long_mem_weights + new_weights
            return
    
    def pad(self, a, b):
        while np.size(a) < np.size(b):
            a.append(0)  
        return a
    
    def get_index(self, word_index, prev_index : int=0):
        
        w1 = self.long_mem_weights[word_index]
        #print(self.long_mem_weights[word_index])
        w2 = self.long_mem_weights[word_index+1]
        #print(self.long_mem_weights[word_index+1])
        
        if len(w1) < len(w2):
            w1 = self.pad(w1,w2)
        elif len(w2) < len(w1):
            w2 = self.pad(w2,w1)
            
        weights = (list)(np.multiply(w1,w2))
        weights = self.pad(weights, self.index_probailities)
        self.weight_mem = self.pad(self.weight_mem, weights)
        
        memory = []
        
        for i in range(len(self.weight_mem)):
            memory.append(self.sigmoid(self.weight_mem[i]) +0.1)
        
        weights = (list)(np.add(weights,memory))
        self.weight_mem = weights
        #print("\nWWWWWWWWWWW\n")
        #print(weights)
        return np.argmax(weights) + 1
    
    def talk(self, seed):
        self.weight_mem = []
        sentence = []
        word_index = seed
        prev_index = 0
        
        count = 0
        
        while(word_index != 0):
            
            word_index = self.get_index(prev_index)
            sentence.append(self.long_memory[word_index])
            prev_index = word_index
            
            if count > 10:
                break
            
            count += 1
            
        return " ".join(sentence)
    
    def train(self, data, iterations : int=1):
        for _ in range(iterations):
            for datapoint in tqdm(data):
                self.forward(datapoint)
                
        #print(self.index_probailities)
        return
    
    def loadData(self, file):
        data = []
        with open(DATAPATH + file + ".txt", 'r',encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines: 
            sentence = re.sub(r'\n','',line)
            if line != '\n':
                data.append(sentence)
                
        #print(data)
        return data
    
    def sigmoid(self, x):
        result = 1 / (1 + np.exp(-x))
        if result < 0.00001:
            return 0
        else:
            return result
    
brain = J_AI()
data = brain.loadData("train")
brain.train(data, 47)
print(brain.long_memory)
print(brain.talk(15))
for i in range(15):
    print(i)
    print(brain.talk(i+30))

#print(brain.talk(10))