# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:38:44 2023

@author: jugwu
"""

from torch import nn

import multi_headed_attention as mh
import feed_forward as ff

class DecoderLayer(nn.Module):
    def __init__(self):
        super(DecoderLayer, self).__init__()
        self.multi_headed_attention = mh.MultiHeadedAttention()
        self.multi_headed_attention2 = mh.MultiHeadedAttention()
        self.positionwise_ff = ff.FeedForwardNetwork()
        
    def forward(self, inpu, encoder_input):
        
        atten = self.multi_headed_attention(inpu, inpu, inpu, mask=True)
        #print("ATTENTION----------------------------")
        #print(atten)
        
        atten2 = self.multi_headed_attention2(atten, encoder_input, encoder_input)
        #print("ATTENTION2---------------------------")
        #print(atten2)
        
        forward = self.positionwise_ff(atten2)
        #print("FORWARD------------------------------")
        #print(forward)
        
        return forward