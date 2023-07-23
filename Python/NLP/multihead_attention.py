# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:32:04 2023

@author: jugwu
"""
import torch
import torch.nn as nn
import seaborn
seaborn.set_context(context="talk")
import attention

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model : int=512, n_heads : int=8, dv_dk : int=64):
        super(MultiHeadAttention, self).__init__()
        ## The inputs size of QKV vectors are the same
        self.W_Q = nn.Linear(d_model, dv_dk * n_heads).to(device)
        self.W_K = nn.Linear(d_model, dv_dk * n_heads).to(device)
        self.W_V = nn.Linear(d_model, dv_dk * n_heads).to(device)
        self.linear = nn.Linear(n_heads * dv_dk, d_model).to(device)
        self.layer_norm = nn.LayerNorm(d_model)
    
    def forward(self, Q, K, V, attn_mask):
        residual, batch_size = Q, Q.size(0)

        q_s = self.W_Q(Q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2) 
        k_s = self.W_K(Q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2)
        v_s = self.W_V(Q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1,2) 

        attn_mask = attn_mask.unsqueeze(1).repeat(1, self.n_heads, 1, 1)

        context, attn = attention.ScaledDotProductAttention()(q_s, k_s, v_s, attn_mask)
        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.n_heads * self.d_v) 
        output = self.linear(context)
        return self.layer_norm(output + residual), attn