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
        words = string.split()
        #words = words.split(",")
        index_list = []
            
        for word in words:
            found = False
            for i in range(np.size(self.long_memory)):
                if word == self.long_memory[i]:
                    self.index_probailities[i] += 0.01
                    self.assign_weights(i, index_list)
                    index_list.append(i)
                    found = True
                    break;
            if found == False:
                self.long_memory.append(word)
                self.index_probailities.append(0.01)
                self.long_mem_weights.append(self.assign_weights())
                index_list.append(np.size(self.long_memory)-1)
        #print(self.long_memory)
        #print(self.index_probailities)
        return
    
    def assign_weights(self, index=None, new=None):
        size = np.size(self.long_memory)
        
        if new is not None:
            new_weights = []
            
            for i in range(size):
                if i in new:
                    new_weights.append(1/(size - i))
                else:
                    new_weights.append(-0.01)
            
            #print(new_weights)
            self.long_mem_weights[index] = self.pad(self.long_mem_weights[index], self.long_memory)
            self.long_mem_weights[index] = (list)(np.add(self.long_mem_weights[index], new_weights))
            
        else:
            weights = []
            for i in range(size):
                if i == size -1:
                    weights.append(0)
                else:
                    weights.append(1/(size - i))
            
            return weights
    
    def pad(self, a, b):
        while np.size(a) < np.size(b):
            a.append(0)  
        return a
    
    def get_index(self, word_index, prev_index : int=0):
        
        a = self.long_mem_weights[prev_index]
        b = self.long_mem_weights[word_index]
        
        if np.size(a) > np.size(b):
            b = self.pad(b, a)
        elif np.size(b) > np.size(a):
            a = self.pad(a, b)
            
        weights = (list)(np.add(b, a))
        #print(weights)
        weights = self.pad(weights, self.index_probailities)
        self.weight_mem = self.pad(self.weight_mem, weights)
        
        memory = []
        for i in range(np.size(self.weight_mem)):
            memory.append(self.weight_mem[i] * 0.1)
            
        weights = (list)(np.add(weights, memory))
        self.weight_mem = weights

        probs = np.multiply(self.index_probailities, weights)
        
        return np.argmax(weights)
    
    def talk(self, seed):
        sentence = []
        self.weight_mem = []
        
        word_index = seed
        
        next_index = self.get_index(word_index)
        
        sentence.append(self.long_memory[next_index])
        counter = 0
        while(next_index != 0):
            prev_index = next_index
            next_index = self.get_index(word_index, prev_index)
            sentence.append(self.long_memory[next_index])
            #print(self.long_memory[next_index])
            
            if counter > 8:
                break
            
            counter += 1
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
    
brain = J_AI()
data = brain.loadData("train")
brain.train(data, 1)

for i in range(100):
    print(i)
    print(brain.talk(i))

print(brain.talk(49))