# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:23:34 2023

@author: jugwu
"""

import torch
import torch.nn.functional as F
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
import re
import string

seed = 7
torch.manual_seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
import numpy as np
np.random.seed(seed)
DATAPATH = 'data//'
from tqdm import tqdm

class BaselineModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(BaselineModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size[0]) 
        self.fc2 = nn.Linear(hidden_size[0], hidden_size[1])  
        self.fc3 = nn.Linear(hidden_size[1], num_classes) 
    
    def forward(self, x):
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)
        out = F.softmax(out, dim=1)
        return out

class J_AI(object):
    def __init__(self, input_size, hidden_size):
        super(J_AI, self).__init__()
        self.memory = [] 
        self.memory_count = []
        self.data = []
        self.labels = []
        self.corpus = []
        self.model = []
        self.output_size = 0
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.testloader =[]
        self.trainloader=[]

    def train(self, epoch : int = 10):
        # define the loss function and the optimiser
        loss_function = nn.CrossEntropyLoss()
        optimiser = optim.Adam(self.model.parameters())

        # the epoch loop
        for epoch in range(epoch):
            running_loss = 0.0
            for data in tqdm(self.trainloader):
                # get the inputs
                inputs, labels = data

                # zero the parameter gradients
                optimiser.zero_grad()
                
                # forward + loss + backward + optimise (update weights)
                outputs = self.model(inputs)
                loss = loss_function(outputs, labels)
                loss.backward()
                optimiser.step()

                # keep track of the loss this epoch
                running_loss += loss.item()
            print("Epoch %d, loss %4.2f" % (epoch, running_loss))
        print('**** Finished Training ****')
        return 
    
    def loadData(self, file):
        data = []
        with open(DATAPATH + file + ".txt", 'r',encoding="utf-8") as f:
            lines = f.readlines()
            
        i = 0
        inputs = []
        labels = []
        add_label = False
        start = False
        add = False
        long = ' '.join(lines)
        #clean text
        long = re.sub('\n','',long)
        long = long.translate(str.maketrans('', '', string.punctuation))
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        long = re.sub('  ',' ',long)
        #print(long)
        print("loading_data...")
        for word in tqdm(long.split(' ')): 
            if word != '\n':
                if add_label:
                    labels.append(word.lower())
                    
                data.append(word.lower())
                i+=1
                add = True
                
            if start == True and add == True:
                inputs.append(data[i:])
                add = False
                
            elif i == 30 and start == False:
                inputs.append(data[:31])
                add_label = True
                start = True
                i = 0
                
        #print(len(inputs[0]))
        #print(len(inputs[1]))
        #print(labels)
        if len(inputs) > len(labels):
            labels.append("done")
        
        self.labels = labels
        self.data = inputs
        #print(self.data)
        #print("LABELS========================")
        #print(labels)
        return inputs, labels
    
    def creatMemory(self, data):
        print("creating_memory...")
        for sentence in tqdm(data):
            for word in sentence:
                found = False
                index = 0
                for i in range(len(self.memory)):
                    if word == self.memory[i]:
                        found = True
                        index = i
                if found:
                    self.memory_count[index][1] += 1
                else:
                    self.memory.append(word)
                    temp = []
                    temp.append(len(self.memory)-1)
                    temp.append(1)
                    self.memory_count.append(temp)
        self.output_size = len(self.memory)
        return
    
    def sortData(self, split, batch : int = 10):
        full_inputs = []
        print("sorting_data...")
        for sentence, label in tqdm(zip(self.data, self.labels)):

            init = torch.zeros(len(self.memory))
            inputs = torch.tensor(init, dtype=torch.float)
            labels = torch.tensor(init, dtype=torch.float)
            
            for word in sentence:
                #print("hey3")
                for token, count in zip( self.memory, self.memory_count):
                    if word.lower() == token:
                        inputs[count[0]] += 1
                    if label.lower() == token:
                        labels[count[0]] = 1
                        
            temp = []        
            temp.append(inputs)
            temp.append(labels)
            full_inputs.append(temp)
                    
        self.corpus = full_inputs
        #print(self.corpus[0])
        #print(len(self.memory))
        #print(len(self.corpus))
        self.trainloader = DataLoader(self.corpus, batch_size=batch, shuffle=True)
        #self.testloader = DataLoader(self.corpus[split:], batch_size=batch, shuffle=True)
        #print(self.labels)
        
    def getData(self, inpu):
        
        init = torch.zeros(len(self.memory))
        inputs = torch.tensor(init, dtype=torch.float)
        
        for word in inpu:
            #print("hey3")
            for token, count in zip(self.memory, self.memory_count):
                if word.lower() == token:
                    inputs[count[0]] += 1
        return inputs
        
    def create(self):
        self.model = BaselineModel(self.output_size, self.hidden_size, self.output_size)
        return
    
    def speak(self, start, num):
        #print("START")
        #print(start)
        #print("CONT")
        string = start
        
        for i in range(num):
            data = self.getData(start[i:])
            out = self.model(data)
            ind = torch.argmax(out).item()
            next_word = self.memory[ind]
            string.append(next_word)
        
        return ' '.join(string)
    
    def empty(self, first):
        sentence = []
        length = self.input_size - len(first)
        for i in range(length):
            sentence.append('==')
        for word in first:
            sentence.append(word)
        return sentence
        
#______________________________________________________________________________                 
              
PATH = "models\\model.pt"  

model = J_AI(15 , [300,300])
model.loadData("memetrainshort")
model.creatMemory(model.data)
model.sortData(2000, 100)
model.create()

model.model.load_state_dict(torch.load(PATH))

model.train(1000)

torch.save(model.model.state_dict(), PATH)

sentence = model.speak(model.empty(['ogres', 'are', 'like', 'onions']),50)
print(sentence)
sentence = model.speak(model.empty(['oh', 'hello', 'there']),50)
print(sentence)
sentence = model.speak(model.empty(['Most', 'of', 'the', 'villains', 'are', 'locked', 'away', 'in', 'the', 'underwater']),50)
print(sentence)
sentence = model.speak(model.empty(['somebody', 'once', 'told', 'me', 'the', 'world', 'is', 'gonna', 'roll', 'me']),50)
print(sentence)
sentence = model.speak(model.empty(['somebody', 'once', 'told', 'me', 'the', 'world', 'is', 'gonna', 'roll', 'me']),50)
print(sentence)

