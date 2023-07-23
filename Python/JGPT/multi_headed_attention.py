# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""

import parameters as para
import torch
from torch import nn
import torch.nn.functional as F

def intialise_mask(matrix):
    atten_mask = torch.zeros_like(matrix)
    
    counter = 0
    
    for i in range(atten_mask.shape[0]):
        for j in range(atten_mask.shape[1]):
            if j > counter:
                atten_mask[i][j] = -float('inf')
        counter +=1
    #print(atten_mask)
    return atten_mask

def scaled_dot_product_attenetion(Q, K, V, mask : bool=False):
    dot_product = torch.matmul(Q, K.t())
    scaled_dot = dot_product / torch.sqrt(torch.tensor(para.d_model, dtype=torch.float, requires_grad=True))
    
    if mask:
        atten_mask = intialise_mask(scaled_dot)
        scaled_dot = scaled_dot + atten_mask
    
    attention_weights = F.softmax(scaled_dot, dim=1)
    #print(attention_weights)
    attention = torch.matmul(attention_weights, V)
    return attention                                
        
class MultiHeadedAttention(nn.Module):
    def __init__(self):
        super(MultiHeadedAttention, self).__init__()
        self.fc_Q = nn.Linear(para.d_model, para.d_model) 
        self.fc_K = nn.Linear(para.d_model, para.d_model) 
        self.fc_V = nn.Linear(para.d_model, para.d_model) 
        self.fc_Out = nn.Linear(para.d_model, para.d_model) 
        self.layer_norm = nn.LayerNorm(para.d_model)
        
    def forward(self, Q, K, V, mask : bool=False):
        Query = self.fc_Q(Q)
        Key = self.fc_K(K)
        Value = self.fc_V(V)
        
        inpu = Q
        
        attention = scaled_dot_product_attenetion(Query, Key, Value, mask)
        
        linear = self.fc_Out(attention)
        
        output = self.layer_norm(linear + inpu)
        
        return output