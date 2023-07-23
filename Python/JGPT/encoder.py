# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""
from torch import nn
import parameters as para

import embedding as em
import positional_encoding as en
import encoder_layer as la

class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        self.encoder_layers = nn.ModuleList([la.EncoderLayer() for _ in range(para.num_encoders)])

    def forward(self, inpu):
        embd = em.embedd(inpu, "words")
        #print("EMBEDDING----------------------------")
        #print(embd)
        
        enc = en.encode(embd)
        #print("ENCODE-------------------------------")
        #print(enc)
        
        out = enc
        for layer in self.encoder_layers:
            out = layer(out)
            
        return out