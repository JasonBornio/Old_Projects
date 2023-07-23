# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""

import parameters as para
import numpy as np
import utilities as util
import re

tag_list = []
vector_list = []
INPUT_DIM = 0
EMBEDDING_DIM = 20
N_FILTERS = 20
FILTER_SIZES = [1,4,5]
OUTPUT_DIM = 1
DROPOUT = 0.5
EMBPATH = "embeddings\\"
import torch
import torch.nn.functional as F
from torch import nn
from torch import optim

class EmbeddNET(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(EmbeddNET, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.fc2 = nn.Linear(hidden_size, input_size)  
    
    def forward(self, x):
        out = self.fc1(x)
        out = F.relu(out)
        out = self.fc2(out)
        if not self.training:
            out = F.softmax(out, dim=1)
        return out
    
class EmbeddCNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, n_filters, filter_sizes, output_dim, dropout):
        super().__init__()
        
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.convs = nn.ModuleList([nn.Conv2d(in_channels = 1, out_channels = n_filters, kernel_size = (fs, embedding_dim)) for fs in filter_sizes])
        self.fc = nn.Linear(len(filter_sizes) * n_filters, output_dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, embedded):
        #text = text.permute(1, 0)
        #embedded = self.embedding(text)
        #embedded = embedded.unsqueeze(1)
        print(self.convs)
        #print(embedded)
        conved = [F.relu(conv(embedded)).squeeze(3) for conv in self.convs]
        pooled = [F.max_pool1d(conv, conv.shape[2]).squeeze(2) for conv in conved]
        
        cat = self.dropout(torch.cat(pooled, dim=1))
            
        return self.fc(cat)
    
def data_generator():
    np.random.seed(para.SEED)
    max_points = 100000
    max_neighbour_index = 10
    min_neighbour_index = 3
    data_points, data_labels = [], []
    data = util.load_words('text')
    
    for i in range(max_points):
        rand_index = np.random.randint(np.shape(data)[0])
        maxlen = len(data[rand_index])
        rand_in_index = np.random.randint(maxlen)
        #print("Outer index: ", rand_index, "Inner index: ", rand_in_index, "Max: ", maxlen)
        if np.random.rand() > 0.2:
            neighbour_index = np.random.randint(min_neighbour_index * 2) - min_neighbour_index
        else:
            neighbour_index = np.random.randint(max_neighbour_index * 2) - max_neighbour_index
        index = rand_in_index + neighbour_index
        if index < 0:
            index = 0
        if index >= maxlen:
            index = maxlen - 1
        
        data_points.append(data[rand_index][rand_in_index].lower())
        data_labels.append(data[rand_index][index].lower())
    
    names = []
    for line in data:
        for word in line:
            if word.lower() not in names:
                names.append(word.lower())
    #print(names)
    
    vectors = torch.rand((len(names), para.d_model), dtype = torch.float, requires_grad=True)
    #print(vector)
    return names, vectors, data_points, data_labels

def data_generatorCNN():
    np.random.seed(para.SEED)
    max_points = 5
    data_points, data_labels = [], []
    data = util.load_words('text')
    
    for i in range(max_points):
        print(1)
        for line in data:
            temp = []
            for word in line:
                temp.append(np.random.rand(para.d_model))
            while np.shape(temp)[0] < para.max_seq_length:
                temp.append(np.zeros(para.d_model))
        data_points.append(temp)
    
    
    names = []
    for line in data:
        for word in line:
            if word.lower() not in names:
                names.append(word.lower())
    #print(names)
    
    vectors = torch.rand((len(names), para.d_model), dtype = torch.float, requires_grad=True)
    #print(vector)
    return names, vectors, data_points
    
def train(epoch : int = 10):
    model = EmbeddNET(para.d_model, 75)
    names, vectors, points, targets = data_generator()
    # define the loss function and the optimiser
    loss_function = nn.CrossEntropyLoss()
    optimiser = optim.Adam(model.parameters())
    
    arr = np.array(np.stack((np.array(points), np.array(targets)),axis=-1))
    #trainloader = DataLoader(arr, batch_size=128, shuffle=True)
    
    # the epoch loop
    for epoch in range(epoch):
        running_loss = 0.0
        for data in arr:
            # get the inputs
            word, neigbour = data
            #print(word)
            #print(neigbour)
            
            inputs = vectors[names.index(word)]
            labels = vectors[names.index(neigbour)]
            # zero the parameter gradients
            optimiser.zero_grad()
            
            # forward + loss + backward + optimise (update weights)
            outputs = model(inputs)
            vectors[names.index(word)].item = outputs
            loss = loss_function(outputs, labels)
            loss.backward()
            optimiser.step()

            # keep track of the loss this epoch
            running_loss += loss.item()
        print("Epoch %d, loss %4.2f" % (epoch, running_loss))
    print('**** Finished Training ****')
    return names, vectors 

def trainCNN(epoch : int = 10):
    names, vectors, points = data_generatorCNN()
    INPUT_DIM = np.shape(names)[0]
    
    model = EmbeddCNN(INPUT_DIM, EMBEDDING_DIM, N_FILTERS, FILTER_SIZES, OUTPUT_DIM, DROPOUT)

    # define the loss function and the optimiser
    loss_function = nn.CrossEntropyLoss()
    optimiser = optim.Adam(model.parameters())
    
    #arr = np.array(np.stack((np.array(points), np.array(targets)),axis=-1))

    data = points
    #labs = targets
    #trainloader = DataLoader(arr, batch_size=128, shuffle=True)
    inputs = [vectors[names.index(w)] for w in data]
    #labels = [vectors[names.index(n)] for n in labs]
    inputs = torch.stack(inputs)
    #labels = torch.stack(labels)
    
    # the epoch loop
    for epoch in range(epoch):
        running_loss = 0.0
        # get the inputs
    
        # zero the parameter gradients
        optimiser.zero_grad()
        
        # forward + loss + backward + optimise (update weights)
        outputs = model(inputs)
        
        for w, outs in zip(data, outputs):
            vectors[names.index(w)].item = outs
                
        #loss = loss_function(outputs, labels)
        #loss.backward()
        optimiser.step()

        # keep track of the loss this epoch
        #running_loss += loss.item()
        print("Epoch %d, loss %4.2f" % (epoch, running_loss))
    print('**** Finished Training ****')
    return names, vectors 

def save(file, tags, vectors):
    with open(EMBPATH + file + "_tags.txt", 'w',encoding="utf-8") as f:
        for tag in tags:
            f.write(tag)
            f.write('\n')
    f.close()
    
    with open(EMBPATH + file + "_vects.txt", 'w',encoding="utf-8") as f:
        f.write(str(para.d_model))
        f.write('\n')
        for vector in vectors:
            for num in vector:
                f.write(str(num.item()))
                f.write('\n')
    f.close()
    return

def load(file):
    with open(EMBPATH + file + "_tags.txt", 'r',encoding="utf-8") as f:
        lines = f.readlines()
    f.close()
    
    tag_list = []
    for line in lines:
        line = re.sub("\n","", line)
        tag_list.append(line)
    
    with open(EMBPATH + file + "_vects.txt", 'r',encoding="utf-8") as f:
        lines = f.readlines()
    f.close()
    
    vects = []
    init = True
    i = 0
    temp = []
    
    for line in lines:
        line = re.sub("\n","", line)
        if init:
            init = False
            size = int(line)
        else:
            if i >= size:
                vects.append(temp)
                temp = []
                i = 0
            temp.append(float(line))
            i+=1
    vects.append(temp)

    vector_list = torch.tensor(vects, dtype=torch.float, requires_grad=True)
    return tag_list, vector_list

import matplotlib.pyplot as plt

def test():
    tags, vectors = train(10)
    save("words2", tags, vectors)
    tags, vectors = load("words2")
    
    #save("words", tags, vectors)
    #print(len(tags))

    dot = torch.dist(vectors[tags.index('yes')],vectors[tags.index('no')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('yes')],vectors[tags.index('hello')])
    print(dot.item())

    dot = torch.dist(vectors[tags.index('muffin')],vectors[tags.index('man')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('muffin')],vectors[tags.index('boy')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('dragon')],vectors[tags.index('donkey')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('shrek')],vectors[tags.index('luffy')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('luffy')],vectors[tags.index('he')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('shrek')],vectors[tags.index('he')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('luffy')],vectors[tags.index('she')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('shrek')],vectors[tags.index('she')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('one')],vectors[tags.index('piece')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('he')],vectors[tags.index('is')])
    print(dot.item())
    dot = torch.dist(vectors[tags.index('he')],vectors[tags.index('she')])
    print(dot.item())

    target = (vectors[tags.index('shrek')] - vectors[tags.index('farquaad')])
    min_idx = torch.norm(vectors - target.unsqueeze(0), dim=1).argmin()
    print(tags[min_idx])

    vals = np.arange(20)
    plt.bar(vals, vectors[tags.index('shrek')].detach().numpy())
    plt.title("SHREK")
    plt.figure()
    plt.bar(vals, vectors[tags.index('luffy')].detach().numpy())
    plt.title("LUFFY")
    plt.figure()
    
def embedd(sequence, file):
    embeddings = []
    tags, vectors = load(file)
    counter = 0
    for word in sequence.split(' '):
        if word not in tags:
            vect = torch.zeros(para.d_model)
        else:
            vect = vectors[tags.index(word)]
        embeddings.append(vect)
        counter +=1
    
    while counter < para.max_seq_length:
        embeddings.append(torch.zeros(para.d_model))
        counter+=1
        
    embeddings = torch.stack(embeddings)

    return embeddings

def get_vector(embeddings, word, tags):
    return embeddings[tags.index(word)]

def closest_words(embeddings, vector, tags, n=10):
    distances = [(w, torch.dist(vector, get_vector(embeddings, w, tags)).item()) for w in tags]
    return sorted(distances, key = lambda w: w[1])[:n]

def analogy(embeddings, word1, word2, word3, tags, n=5):
    
    candidate_words = closest_words(embeddings, get_vector(embeddings, word2, tags) - get_vector(embeddings, word1, tags) + get_vector(embeddings, word3, tags),tags, n+3)
    
    candidate_words = [x for x in candidate_words if x[0] not in [word1, word2, word3]][:n]
    
    print(f'{word1} is to {word2} as {word3} is to...')
    
    return candidate_words

def print_tuples(tuples):
    for w, d in tuples:
        print(f'({d:02.04f}) {w}') 
        
test()
tags, vectors = load("words2")
print(np.shape(tags))
print(vectors.shape)

print(print_tuples(closest_words(vectors, get_vector(vectors, 'hello', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'he', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'she', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'luffy', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'shrek', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'one', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'piece', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'to', tags), tags)))
print(print_tuples(closest_words(vectors, get_vector(vectors, 'it', tags), tags)))

print(print_tuples(analogy(vectors, 'man', 'shrek', 'woman', tags)))


#emb = embedd('hi how are you')
#print(emb)
#emb = embedd('never say you can not do something oolgoo')
#print(emb)