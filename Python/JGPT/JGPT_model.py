# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""
from torch import nn
import torch
import encoder as enc
import decoder as dec
import embedding as emb
import parameters as para
import numpy as np
from tqdm import tqdm

class J_GPT(nn.Module):
    def __init__(self):
        super(J_GPT, self).__init__()
        self.encoder = enc.Encoder()
        self.decoder = dec.Decoder()

    def forward(self, inpu, outs, counter):
        
        encoded = self.encoder(inpu)
        decoded = self.decoder(outs, encoded)
        
        return decoded[counter]
    
    def evaluate(self, inpu, outs):
        
        encoded = self.encoder(inpu)
        decoded = self.decoder(outs,encoded)
        
        class_index = torch.argmax(decoded[1])
        tags, vectors = emb.load("memebed5")
        
        prediction = tags[class_index]
            
        return prediction
    
    def pad(self, inpu):
        out = inpu
        while np.shape(out)[0] < para.max_seq_length:
            out.append('randomnoise6666')
        return out
    
    def talk(self, inpu, num : int=10):
        encoded = self.encoder(inpu)
        
        start = ['randomnoise6666'] * para.max_seq_length
        start[0] = '<start>'
        decoded = self.decoder(' '.join(start),encoded)
        counter = 1
        class_index = torch.argmax(decoded[counter])
        
        tags, vectors = emb.load("memebed5")
        
        prediction = tags[class_index]
        
        sentence = prediction + ' '
        
        sequence = [prediction]
        
        for i in tqdm(range(num)):
            decoded = self.decoder(' '.join(self.pad(sequence)),encoded)
            counter += 1
            class_index = torch.argmax(decoded[counter])
            prediction = tags[class_index]
            sentence = sentence + prediction + ' '
            sequence.append(prediction)
            
            if i == para.max_seq_length - 1:
               break;
               
        print("SENTENCE::::")
        print(sentence)
        return
    
    
    