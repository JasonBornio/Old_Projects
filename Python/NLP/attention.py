# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:08:38 2023

@author: jugwu
"""
import torch
import torch.nn as nn
import math

class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super(ScaledDotProductAttention, self).__init__()

    def forward(self, Q, K, V, attn_mask):
        """Q --> [batch_size x n_heads x len_q x d_k]
          K --> [batch_size x n_heads x len_k x d_k]
          V --> [batch_size x n_heads x len_k x d_v]
          scores --> [batch_size x n_heads x len_q x len_k]"""

        d_k = Q.size(1)
        scores = torch.matmul(Q, K.transpose(-2, -1))/math.sqrt(d_k)

        scores.masked_fill_(attn_mask, -1e9) # This line applies a mask attn_mask to the attention scores scores by replacing the masked positions with a large negative number -1e9. 
        attn = nn.Softmax(dim=-1)(scores)
        context = torch.matmul(attn, V) # calculates the weighted sum of the values V, using the attention probabilities attn as the weights.
        return context, attn