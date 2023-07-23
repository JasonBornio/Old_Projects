# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:02:54 2023

@author: jugwu
"""
from torch import nn
import torch 
import numpy as np

m = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=5, stride=1)
input = torch.tensor([np.random.rand(20)], dtype=torch.float)
print(input.shape)
output = m(input)
print(output.shape)