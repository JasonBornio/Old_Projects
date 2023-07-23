# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:13:04 2023

@author: jugwu
"""

import utilities as util
import embedding as emb
import torch
import numpy as np
import parameters as para
from tqdm import tqdm

RAND = 'randomnoise6666'
RANDIND = 0


def load_data(tag_file, file, num : int = 10):
    data = util.load_sentences(file)
    tags, vectors = emb.load(tag_file)
    
    inputs = []
    outputs = []
    targets = []
    
    outputs.append([RAND])
    
    for i in range(num):
        inputs.append([n.lower() for n in data[i].split()])
        outputs.append([n.lower() for n in data[i].split()])
        targets.append([vectors[tags.index(n.lower())].detach().numpy() for n in data[i].split()])
    
    for i in range(num + 1):
        while np.size(outputs[i]) < para.max_seq_length:
            outputs[i].append(RAND)
            if i > 0:
                inputs[i-1].append(RAND)
                targets[i-1].append(np.zeros(para.d_model))    
            
    inputs.append([RAND] * para.max_seq_length)
    targets.append([np.zeros(para.d_model) for _ in range(para.max_seq_length)])
    #print(targets)
    #targets = torch.stack(targets)
    return  inputs,  outputs,  torch.tensor(targets, dtype = torch.float, requires_grad=True )

def load_data2(tag_file, file, num : int = 10):
    data = util.load_sentences(file)
    tags, vectors = emb.load(tag_file)
    
    inputs = []
    outputs = []
    targets = []
    
    outputs.append([RAND])
    
    for i in range(num):
        inputs.append([n.lower() for n in data[i].split()])
        outputs.append([n.lower() for n in data[i].split()])
        targets.append([tags.index(n.lower()) for n in data[i].split()])
    
    for i in range(num + 1):
        while np.size(outputs[i]) < para.max_seq_length:
            outputs[i].append(RAND)
            if i > 0:
                inputs[i-1].append(RAND)
                targets[i-1].append(0)    
            
    inputs.append([RAND] * para.max_seq_length)
    targets.append([0 for _ in range(para.max_seq_length)])
    #print(targets)
    #targets = torch.stack(targets)
    return  inputs,  outputs,  torch.tensor(targets, dtype = torch.float, requires_grad=True )

def load_data3(tag_file, file, num : int = 10):
    data = util.load_sentences(file)
    tags, vectors = emb.load(tag_file)
    
    inputs = []
    outputs = []
    targets = []
    
    outputs.append([RAND])
    
    for i in range(num):
        inputs.append([n.lower() for n in data[i].split()])
        outputs.append([n.lower() for n in data[i].split()])
        targets.append([np.zeros(para.vocab_size) for _ in data[i].split()])
        k = 0
        for name in data[i].split():
            targets[i][k][tags.index(name.lower())] = 1
            k+=1
    
    #print(targets)
    #print(np.shape(targets))
    
    for i in range(num + 1):
        while np.size(outputs[i]) < para.max_seq_length:
            outputs[i].append(RAND)
            if i > 0:
                inputs[i-1].append(RAND)
                targets[i-1].append(np.zeros(para.vocab_size))    
    
    #print(np.shape(targets))
    
    inputs.append([RAND] * para.max_seq_length)
    targets.append([np.zeros(para.vocab_size) for _ in range(para.max_seq_length)])
    #print(targets)
    #targets = torch.stack(targets)
    return  inputs,  outputs,  torch.tensor(targets, dtype = torch.float, requires_grad=True )

#inputs, outputs, targets = load_data3("words", "text", 10)
#print(targets)
#print(targets.shape)

#inputs, outputs, targets = load_data3("words", "text", 10)
#print(targets)
#print(targets.shape)

def sample_bathces(data, tags, vectors, num :int = 10):
    total_inputs = []
    total_outputs = []
    total_targets = []
    for _ in range(num):
        
        inputs = []
        outputs = []
        targets = []
        
        rand_index = np.random.randint(np.shape(data)[0])
        inputs = [n.lower() for n in data[rand_index].split(' ')]
        size = np.shape(inputs)[0]
        
        for i in range(size):
            outputs.append(inputs[:i+1])
            
            temp = np.zeros(para.vocab_size)
            if i == size - 1:
                temp = np.ones(para.vocab_size)
            else:
                temp = np.zeros(para.vocab_size)
                temp[tags.index(inputs[i+1].lower())] = 1
            
            targets.append(temp)
    
        while np.shape(inputs)[0] < para.max_seq_length:
            inputs.append(RAND)

        for k in range(size):
            while np.shape(outputs[k])[0] < para.max_seq_length:
                outputs[k].append(RAND)
        
        total_inputs.append(inputs)
        total_outputs.append(outputs)
        total_targets.append(targets)
        
        
    return  total_inputs,  total_outputs,  torch.tensor(total_targets, dtype = torch.float, requires_grad=True )




def sample(data, tags, vectors, length = None):
    inputs = []
    outputs = []
    targets = []
    
    if length > np.shape(data)[0]:
        length = np.shape(data)[0]
        
    if length == None:
        rand_index = np.random.randint(np.shape(data)[0])
    else:
        rand_index = np.random.randint(length)
        
    inputs = [n.lower() for n in data[rand_index].split(' ')]
    size = np.shape(inputs)[0]

    for i in range(size):
        outputs.append(inputs[:i+1])
        
        temp = np.zeros(para.vocab_size)
        if i == size - 1:
            temp = np.ones(para.vocab_size)
        else:
            temp = np.zeros(para.vocab_size)
            temp[tags.index(inputs[i+1].lower())] = 1
            
        targets.append(temp)
    
    while np.shape(inputs)[0] < para.max_seq_length:
        inputs.append(RAND)

    for k in range(size):
        while np.shape(outputs[k])[0] < para.max_seq_length:
            outputs[k].append(RAND)
        
    return  inputs,  outputs,  torch.tensor(targets, dtype = torch.float, requires_grad=True )



#data = util.load_sentences("clean3")
#tags, vectors = emb.load("memebed5")
#inputs, outputs, targets = sample(data, tags, vectors)
    
#print("TARGS:::")
#print(targets)
#print(targets.shape)
#print("INPUS:::")
#print(inputs)
#print(np.shape(inputs))
#print("OUTPS:::")
#print(outputs)
#qprint(np.shape(outputs))