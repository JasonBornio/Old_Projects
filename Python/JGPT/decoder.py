# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""
from torch import nn
import parameters as para

import embedding as em
import positional_encoding as en
import decoder_layer as la
import torch.nn.functional as F

class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()
        self.decoder_layers = nn.ModuleList([la.DecoderLayer() for _ in range(para.num_encoders)])
        self.linear_classifer = nn.Linear(para.d_model, para.vocab_size,  bias=False)
        
    def forward(self, inpu, encoder_input):
        embd = em.embedd(inpu, "words")
        #print("EMBEDDING----------------------------")
        #print(embd)
        
        enc = en.encode(embd)
        #print("ENCODE-------------------------------")
        #print(enc)
        
        out = enc
        for layer in self.decoder_layers:
            out = layer(out, encoder_input)
            
        out = self.linear_classifer(out)
        #out = F.softmax(out)
            
        return out