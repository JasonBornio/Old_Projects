# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:32:04 2023

@author: jugwu
"""
import torch.nn as nn
import seaborn
import multihead_attention as attn
seaborn.set_context(context="talk")

class AttentionDecoder(nn.Module):
    "Generic N layer decoder with masking."
    def __init__(self, n_layers : int=1):
        super(AttentionDecoder, self).__init__()
        self.layers = nn.ModuleList([DecoderLayer() for _ in range(n_layers)])
        
    def forward(self, ouputs, memory, src_mask, tgt_mask):
        dec_self_attns, dec_enc_attns = [], []
        
        for layer in self.layers:
            ouputs, dec_self_attn, dec_enc_attn = layer(ouputs, memory, src_mask, tgt_mask)
            dec_self_attns.append(dec_self_attn)
            dec_enc_attns.append(dec_enc_attn) 
            
        return ouputs, dec_self_attn, dec_enc_attn
    
class DecoderLayer(nn.Module):
    "Decoder is made of self-attn_layer1, src-attn_layer2, and fully_connected (defined below)"
    def __init__(self, fully_connected_layer):
        super(DecoderLayer, self).__init__()
        self.attn_layer1 = attn.MultiHeadAttention().to(attn.device)
        self.attn_layer2 = attn.MultiHeadAttention().to(attn.device)
        self.feed_forward = fully_connected_layer
 
    def forward(self, inputs, memory, src_mask, tgt_mask):
        dec_outputs, dec_self_attn = self.attn_layer1(inputs, inputs, inputs, tgt_mask)
        dec_outputs, dec_enc_attn = self.attn_layer2(dec_outputs, memory, memory, src_mask)
        dec_outputs = self.feed_forward(dec_outputs)
        return dec_outputs, dec_self_attn, dec_enc_attn