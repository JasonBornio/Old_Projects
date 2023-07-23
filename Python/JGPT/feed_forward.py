# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:40:54 2023

@author: jugwu
"""

import parameters as para
from torch import nn
import torch.nn.functional as F

class FeedForwardNetwork(nn.Module):
    def __init__(self):
        super(FeedForwardNetwork, self).__init__()
        self.fc1 = nn.Linear(para.d_model, para.d_model * 4) 
        self.fc2 = nn.Linear(para.d_model * 4, para.d_model) 
        self.layer_norm = nn.LayerNorm(para.d_model)
        
    def forward(self, inpu):
        output = self.fc1(inpu)
        output = F.relu(output)
        output = self.fc2(output)
        output = self.layer_norm(output + inpu)
        return output