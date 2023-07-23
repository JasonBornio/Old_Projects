# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:27:21 2023

@author: jugwu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""

import parameters as para
import numpy as np
import utilities as util
import re
from scipy.stats import skewnorm
import math

tag_list = []
vector_list = []
MAX = 1
BATCHES = 128
EPOCHS = 6
EMBPATH = "embeddings\\"
import torch
import torch.nn.functional as F
from torch import nn
from torch import optim
from torch.utils import data
from tqdm import tqdm

class EmbeddNET(nn.Module):
    def __init__(self, input_size=10, hidden_size=10):
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
    
def data_generator():
    np.random.seed(para.SEED)
    max_points = MAX
    max_neighbour_index = 10
    min_neighbour_index = 3
    data_points, data_labels = [], []
    data = util.load_words('clean4')
    
    for k in range(max_points):
        for i in range(np.shape(data)[0]):
            maxlen = len(data[i])
            for j in range(maxlen):
                #rand_in_index = np.random.randint(maxlen)
                #print("Outer index: ", rand_index, "Inner index: ", rand_in_index, "Max: ", maxlen)
                if np.random.rand() > 0.35:
                    neighbour_index = np.random.randint(min_neighbour_index * 2) - min_neighbour_index
                else:
                    neighbour_index = np.random.randint(max_neighbour_index * 2) - max_neighbour_index
                index = j + neighbour_index
                if index < 0:
                    index = 0
                if index >= maxlen:
                    index = maxlen - 1
                    
                if index == j and j != (maxlen - 1):
                    index += 1
                elif index == j:
                    index -= 1
        
                data_points.append(data[i][j].lower())
                data_labels.append(data[i][index].lower())
        #print("it:", k)
    
    names = []
    for line in data:
        for word in line:
            if word.lower() not in names:
                names.append(word.lower())
    ########################################
    X = []
    Y = []
    size = np.shape(names)[0]
    for word, label in zip(data_points, data_labels):
        temp = np.zeros(size)
        temp[names.index(word)]
        X.append(temp)
        temp = np.zeros(size)
        temp[names.index(label)]
        Y.append(temp)
    print("it:")
    
        
    X= torch.tensor(X, dtype=torch.float, requires_grad=True)
    Y= torch.tensor(Y, dtype=torch.float, requires_grad=True)
    print(X.shape)
        
    return names, X, Y


def skew(num):
    num_locs = num

    numValues = 10000
    maxValue = ((num_locs * 2) - 1)
    skewness = 0  #Negative values are left skewed, positive values are right skewed.

    random = skewnorm.rvs(a = skewness,loc=maxValue, size=numValues)  #Skewnorm function

    random = random - min(random)      #Shift the set so the minimum value is equal to zero.
    random = random / max(random)      #Standadize all the vlues between 0 and 1. 
    random = random * maxValue   
    random = random - (num_locs)      #Multiply the standardized values by the maximum value.
    
    list_ = []
    for i in range(numValues):
        index = np.random.randint(numValues)
        num = random[index]
        number = math.floor(num)
        if number == 0:
            number = np.random.randint(maxValue + 1) - num_locs 
        if number == 0:
            if np.random.rand() < 0.5:
                number = 1 
            else:
                number = -1
        list_.append(math.floor(number))
        
    
    max_index = np.shape(list_)[0]
    sum_ = np.zeros(num_locs * 2)
    
    for num_ in list_:
        sum_[num_+num_locs] += 1

    return list_, max_index


def data_generator_rand():
    np.random.seed(para.SEED)
    max_points = MAX
    data_points, data_labels = [], []
    data = util.load_words('clean4')
    print("generating data...")
    skew_distribution, max_ind = skew(10)
    
    for k in range(max_points):
        for i in tqdm(range(np.shape(data)[0])):
            maxlen = len(data[i])
            for j in range(maxlen):
                rand_in_index = np.random.randint(maxlen)
                neighbour_index = skew_distribution[np.random.randint(max_ind)]
                
                index = rand_in_index + neighbour_index
                if index < 0:
                    index = 0
                if index >= maxlen:
                    index = maxlen - 1
                    
                if index == rand_in_index and rand_in_index != (maxlen - 1):
                    index += 1
                elif index == rand_in_index:
                    index -= 1
        
                data_points.append(data[i][rand_in_index].lower())
                data_labels.append(data[i][index].lower())
        #print("it:", k)
    
    names = []
    for line in data:
        for word in line:
            if word.lower() not in names:
                names.append(word.lower())
    ########################################
    X = []
    Y = []
    size = np.shape(names)[0]
    for word, label in tqdm(zip(data_points, data_labels)):
        temp = np.zeros(size)
        temp[names.index(word)] = 1
        X.append(temp)
        temp = np.zeros(size)
        temp[names.index(label)] = 1
        Y.append(temp)
        
    X= torch.tensor(X, dtype=torch.float, requires_grad=True)
    Y= torch.tensor(Y, dtype=torch.float, requires_grad=True)
    print(X.shape)
        
    return names, X, Y

def data_generator_rand_old():
    np.random.seed(para.SEED)
    max_points = MAX
    max_neighbour_index = 10
    min_neighbour_index = 3
    data_points, data_labels = [], []
    data = util.load_words('clean4')
    
    for k in range(max_points):
        for i in range(np.shape(data)[0]):
            maxlen = len(data[i])
            for j in range(int(maxlen/10) + 1):
                rand_in_index = np.random.randint(maxlen)
                #print("Outer index: ", rand_index, "Inner index: ", rand_in_index, "Max: ", maxlen)
                if np.random.rand() > 0.35:
                    neighbour_index = np.random.randint(min_neighbour_index * 2) - min_neighbour_index
                else:
                    neighbour_index = np.random.randint(max_neighbour_index * 2) - max_neighbour_index
                index = rand_in_index + neighbour_index
                if index < 0:
                    index = 0
                if index >= maxlen:
                    index = maxlen - 1
                    
                if index == rand_in_index and rand_in_index != (maxlen - 1):
                    index += 1
                elif index == rand_in_index:
                    index -= 1
        
                data_points.append(data[i][rand_in_index].lower())
                data_labels.append(data[i][index].lower())
        #print("it:", k)
    
    names = []
    for line in data:
        for word in line:
            if word.lower() not in names:
                names.append(word.lower())
    ########################################
    X = []
    Y = []
    size = np.shape(names)[0]
    for word, label in zip(data_points, data_labels):
        temp = np.zeros(size)
        temp[names.index(word)] = 1
        X.append(temp)
        temp = np.zeros(size)
        temp[names.index(label)] = 1
        Y.append(temp)
    print("it:")
    
        
    X= torch.tensor(X, dtype=torch.float, requires_grad=True)
    Y= torch.tensor(Y, dtype=torch.float, requires_grad=True)
    print(X.shape)
        
    return names, X, Y

def train(epoch : int = 10, base_model = None):
    names, points, targets = data_generator_rand()
    
    input_size = np.shape(names)[0]
    print(input_size)
    if base_model == None:    
        model = EmbeddNET(input_size, para.d_model)
    else:
        model = base_model
    # define the loss function and the optimiser
    loss_function = nn.CrossEntropyLoss()
    optimiser = optim.Adam(model.parameters())
    
    dataset = data.TensorDataset(points,targets)
    dataloader = data.DataLoader(dataset, batch_size=BATCHES, shuffle=True) #batch size 25
    
    # the epoch loop
    for epoch in range(epoch):
        running_loss = 0.0
        for batch in tqdm(dataloader):
            optimiser.zero_grad()
            
            # forward + loss + backward + optimise (update weights)
            outputs = model(batch[0])
            loss = loss_function(outputs, batch[1])
            #print(loss)
            loss.backward()
            optimiser.step()
        
            # keep track of the loss this epoch
            running_loss += loss.item()
            
        print("Epoch %d, loss %4.12f" % (epoch, running_loss))
    print('**** Finished Training ****')
    
    vectors = torch.stack(list(model.fc1.weight))
    vectors = vectors.t()
    return names, vectors, model 

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

def distan(word1, word2, vectors, tags):
    dot = torch.dist(vectors[tags.index(word1)],vectors[tags.index(word2)])
    print(word1 + " - " + word2 + ": ", dot.item())
    

def test():
    PATH = "models\\tagsMEME2No.pt"  
    #model22
    #model225
    #tags, vectors = train(EPOCHS)
    model = EmbeddNET(1670, para.d_model)
    model.load_state_dict(torch.load(PATH))
    tags, vectors, model = train(EPOCHS, base_model=model)
    torch.save(model.state_dict(), PATH)
    
    save("memebed8No", tags, vectors)
    tags, vectors = load("memebed8No")
    
    #save("words", tags, vectors)
    #print(len(tags))

    distan('tanjiro', 'akaza', vectors, tags)
    distan('tanjiro', 'gyutaro', vectors, tags)
    distan('akaza', 'gyutaro', vectors, tags)
    distan('akaza', 'upper', vectors, tags)
    #distan('akaza', 'lower', vectors, tags)
    distan('akaza', '3', vectors, tags)
    distan('akaza', 'three', vectors, tags)
    distan('akaza', '6', vectors, tags)
    distan('gyutaro', 'upper', vectors, tags)
    #distan('gyutaro', 'lower', vectors, tags)
    distan('gyutaro', '6', vectors, tags)
    distan('gyutaro', 'six', vectors, tags)
    distan('gyutaro', '3', vectors, tags)
    #distan('tanjiro', 'goku', vectors, tags)
    distan('tanjiro', 'he', vectors, tags)
    #distan('goku', 'he', vectors, tags)
    distan('nezuko', 'he', vectors, tags)
    distan('tanjiro', 'she', vectors, tags)
    #distan('goku', 'she', vectors, tags)
    distan('nezuko', 'she', vectors, tags)
    #distan('goku', 'vegeta', vectors, tags)
    #distan('goku', 'saiyan', vectors, tags)
    #distan('demon', 'saiyan', vectors, tags)
    distan('he', 'she', vectors, tags)

    #target = (vectors[tags.index('goku')] - vectors[tags.index('vegeta')])
    #min_idx = torch.norm(vectors - target.unsqueeze(0), dim=1).argmin()
    #print(tags[min_idx])

    vals = np.arange(para.d_model)
    
    plt.bar(vals, vectors[tags.index('it')].detach().numpy())
    plt.title("IT")
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
        
def main():
    test()
    tags, vectors = load("memebed8")
    print(np.shape(tags))
    print(vectors.shape)

    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'gohan', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'he', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'she', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'goku', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'tanjiro', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'dragon', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'ball', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'to', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'it', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'water', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'is', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'vegeta', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'demon', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'gyutaro', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'akaza', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'android', tags), tags)))
    #print(print_tuples(closest_words(vectors, get_vector(vectors, 'zohakuten', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'breathing', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'sword', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'sound', tags), tags)))
    print(print_tuples(closest_words(vectors, get_vector(vectors, 'get', tags), tags)))
    

    print(print_tuples(analogy(vectors, 'boy', 'man', 'girl', tags)))
    print(print_tuples(analogy(vectors, 'she', 'her', 'he', tags)))
    return 0 
        
if __name__=="__main__":
    main()