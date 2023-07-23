# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:54:52 2023

@author: jugwu
"""
import torch
import torch.nn.functional as F
from torch import nn
from torch import optim
from tqdm import tqdm
import embedding as emb
import numpy as np
from torch.utils.data import DataLoader
import utilities as util
import random
import os

input_size = 100
hidden_size = [20,10]
vocab_size = 4733
max_sequence_length = 10
test_length = 40

class NLP(nn.Module):
    def __init__(self):
        super(NLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size[0]) 
        self.attention = nn.Linear(input_size * max_sequence_length, hidden_size[0]) 
        self.attention2 = nn.Linear(hidden_size[0], hidden_size[1]) 
        self.fc2 = nn.Linear(hidden_size[0], hidden_size[1])  
        self.fc3 = nn.Linear(hidden_size[1], vocab_size)  
    
    def forward(self, current, previous):
        out = self.fc1(current)
        out = F.relu(out)
        hidden = F.relu(self.attention(previous))
        out = out + hidden
        out = self.fc2(out)
        out = F.relu(out)
        hidden2 = F.relu(self.attention2(hidden))
        out = out + hidden2
        out = self.fc3(out)
        #out = F.softmax(out)
        return out

class NLP2(nn.Module):
    def __init__(self):
        super(NLP2, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size[0]) 
        self.attention = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=50, stride=1)
        self.attention2 = nn.Linear(hidden_size[0], hidden_size[1]) 
        self.fc2 = nn.Linear(hidden_size[0], hidden_size[1])  
        self.fc3 = nn.Linear(hidden_size[1], vocab_size)  
    
    def forward(self, current, previous):
        out = self.fc1(current)
        out = F.relu(out)
        hidden = F.relu(self.attention(previous))
        out = out + hidden
        out = self.fc2(out)
        out = F.relu(out)
        hidden2 = F.relu(self.attention2(hidden))
        out = out + hidden2
        out = self.fc3(out)
        #out = F.softmax(out)
        return out
    
def load_data(file):
    tags, vectors = emb.load(file)
    print(np.shape(tags))
    
    labels = [np.zeros(np.shape(tags)) for _ in range(vocab_size)]
    for i in range(np.shape(labels)[0]):
        labels[i][i] = 1
        
    temp = []
    temp.append(vectors.detach().numpy())
    temp.append(np.array(labels))
    trainloader = DataLoader(temp, batch_size=50, shuffle=True)
    
    return trainloader

def data_generator_rand(length : int = 20):
    np.random.seed(10)
    data_points, data_labels = [], []
    tags, vectors = emb.load("memebed5")
    sentences = util.load_sentences("clean4")[150:length+150]
    #print(np.shiape(sentences))
    #print(data)
    random.shuffle(sentences)
    #print(sentences[:10])
    sentences =sentences
    
    for sentence in sentences:
        array = sentence.split(' ')
        data, labels = [], []
        for i in range(np.shape(array)[0]):
            data.append(vectors[tags.index(array[i].lower())])
            temp = []
            temp = np.zeros(vocab_size)
            if i == (np.shape(array)[0] - 1):
                temp[tags.index(array[0].lower())] = 1
            else:
                temp[tags.index(array[i+1].lower())] = 1
            labels.append(torch.tensor(temp,requires_grad=True, dtype=torch.float))
                
        data_points.append(data)
        data_labels.append(labels)
    
    #X= torch.tensor(data_points, dtype=torch.float, requires_grad=True)
    #Y= torch.tensor(data_points, dtype=torch.float, requires_grad=True)
    #print(X.shape)
        
    return tags, vectors, data_points, data_labels

def pad(output, current = None, index: int = 0, repeat:bool = False):
    count = 0
    if current != None:
        count = index * input_size
        if count >= max_sequence_length * input_size:
            #print("<<TOOBIG>>")
            if repeat == False:
                return current
            start = current.detach().numpy()
            start = list(start)
            start = start[input_size:]
        else:
            start = current.detach().numpy()
            start = list(start)
            start = start[:count]

        #print()
    else:
        start = []
    
    for out in output:
        start.append(out)
        count+=1
        
    while count < max_sequence_length * input_size:
        start.append(0)
        count+=1
    
    result = torch.tensor(start, dtype=torch.float, requires_grad=True)
    return result

def train(max_epoch : int = 10, base_model = None, repeat : bool = False, data_length : int = 10):

    if base_model !=None:
        model=base_model
    else:
        model = NLP()
        
    # define the loss function and the optimiser
    loss_function = nn.CrossEntropyLoss()
    optimiser = optim.Adam(model.parameters())
    
    #tags, vectors, inputs, labels = data_generator_rand(200)
    #sentences = util.load_sentences("text", 200)
    
    # the epoch loop
    for epoch in range(max_epoch):
        running_loss = 0.0
        tags, vectors, inputs, labels = data_generator_rand(data_length)
        for X, Y in tqdm(zip(inputs, labels), 'Epoch: ' + str(epoch)):
            init = pad(torch.zeros(1))
            i=0
            #print("X:",X)
            #print("Y:",Y)
            for word, target in zip(X, Y):
                i+=1
                inp = word
                label = target
                
                # zero the parameter gradients
                optimiser.zero_grad()
             
                # forward + loss + backward + optimise (update weights)
                outputs = model(inp, init)
                loss = loss_function(outputs, label)
                loss.backward()
                optimiser.step()
                #print("yo")
                init = pad(vectors[torch.argmax(outputs)], init, i, repeat)
                if (i >= max_sequence_length - 1) and repeat == False:
                    break;
            # keep track of the loss this epoch
            running_loss += loss.item()
        print("Loss %4.5f" % (running_loss))
    print('**** Finished Training ****')
    log(model, FILE, max_epoch, running_loss, data_length)
    return model

def log(model, file, itr, loss, d_length):
    print("writing......")
    
    if os.path.exists(file + "_log.txt"):
        with open("logs\\" + file + "_log.txt", 'r',encoding="utf-8") as f:
            lines = f.readlines()
        f.close()
        
        lines[12] = str(loss) + "\n"
        lines[14] = str(int(lines[14]) + itr) + "\n"

        with open("logs\\" + file + "_log.txt", 'w',encoding="utf-8") as f:
            for line in tqdm(lines):
                f.write(line)
        f.close()
        
    else:      
        lines = []
        lines.append(FILE)
        lines.append("Model Dimensions:")
        lines.append(str(input_size))
        lines.append(str(hidden_size[0]))
        lines.append(str(hidden_size[1]))
        lines.append("Sequence Length::")
        lines.append(str(max_sequence_length))
        lines.append("Vocab Size:::::::")
        lines.append(str(vocab_size))
        lines.append("Sample Size::::::")
        lines.append(str(d_length))
        lines.append("Loss:::::::::::::")
        lines.append(str(loss))
        lines.append("Iterations:::::::")
        lines.append(str(itr))
        
        with open("logs\\" + file + "_log.txt", 'w',encoding="utf-8") as f:
            for line in tqdm(lines):
                f.write(line)
                f.write("\n")
        f.close()
        
    return

def talk(model, num:int= 10, start = '<start>', initial = None):

    tags, vectors =  tags, vectors = emb.load("memebed5")
    inputs = vectors[tags.index(start.lower())]
    
    if initial != None:
        vect = []
        k = 0
        for word in initial.split(' '):
            k+=1
            vecto = vectors[tags.index(word)]
            for numb in vecto:
                vect.append(numb)
        init = pad(torch.zeros(1), torch.stack(vect), k, True)
        sentence = initial + ' ' + start + ' '
    else:
        init = pad(torch.zeros(1))
        sentence = start + ' '
        
    i=0
    for i in tqdm(range(num),'Writing'):
        i+=1
        outputs = model(inputs, init)
        index = torch.argmax(outputs)
        inputs = vectors[index]
        init = pad(vectors[index], init, i, True)
        
        sentence += tags[index] + ' '
    print()
    return sentence
##########
FILE = "MODELSLAYER12"
PATH = "models\\" + FILE + ".pt"
#modelTESTREPEAT 50 25 HIDDEN 10 LENGTH 50 DATA ITR: 100
#modelOGRE 35 15 HIDDEN 10 LENGTH 50 DATA
#model22
#model225
model = NLP()

#model.load_state_dict(torch.load(PATH))
model = train(2, base_model=model, repeat=False, data_length=50)
torch.save(model.state_dict(), PATH)
print(talk(model,start='akaza', num=test_length))
print()
print(talk(model,start='tanjiro', num=test_length))
print()
#print(talk(model,start='that', num=test_length,initial='tanjiro notes'))
#print()
#print(talk(model,start='unleashes', num=test_length,initial='akaza'))
#print()
#print(talk(model,start='demon', num=test_length,initial='the'))
#print()
#print(talk(model,start='powerful', num=test_length,initial='the'))
#print()
#print(talk(model,start='the', num=test_length))
#print()
#print(talk(model,start='compass', num=test_length,initial='akaza unleashes his technique development destructive death'))
#print()
#print(talk(model,start='princess', num=test_length))
#print()
#print(talk(model,start='farquaad', num=test_length))
#print()
#print(talk(model,start='prince', num=test_length))
#print(talk(model,start='orge', num=test_length))
#print()


print(talk(model,start='face', num=test_length, initial='gyutaro pauses in astonishment before furiously scratching his'))
print()
#print(talk(model,start='z', num=test_length, initial='dragon ball'))
#print()
#print(talk(model,start='super', num=test_length, initial='dragon ball'))
#print()
#print(talk(model,start='than', num=test_length, initial='goku is stronger'))
#print()




#######PRINT########