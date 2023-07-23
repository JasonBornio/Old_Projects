# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""

import parameters as para
import numpy as np
import torch

import embedding as emb
    
def encode(sequence_vector):
    
    pos = 0
    position_vectors = []
    for vector in sequence_vector:
        vect = []
        for i in range(para.d_model):
            if i % 2 == 0:
                vect.append(np.sin(pos/10000 ** ((2 * i)/para.d_model)))
            else:
                vect.append(np.cos(pos/10000 ** ((2 * (i-1))/para.d_model)))
        pos += 1
        position_vectors.append(vect)
        
    #print(position_vectors)
    return sequence_vector + torch.tensor(position_vectors, dtype=torch.float, requires_grad=True)

