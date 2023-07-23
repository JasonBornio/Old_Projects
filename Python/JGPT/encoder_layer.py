# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:38:44 2023

@author: jugwu
"""

from torch import nn

import multi_headed_attention as mh
import feed_forward as ff

class EncoderLayer(nn.Module):
    def __init__(self):
        super(EncoderLayer, self).__init__()
        self.multi_headed_attention = mh.MultiHeadedAttention()
        self.positionwise_ff = ff.FeedForwardNetwork()
        
    def forward(self, inpu):
        
        atten = self.multi_headed_attention(inpu, inpu, inpu)
        #print("ATTENTION----------------------------")
        #print(atten)
        
        forward = self.positionwise_ff(atten)
        #print("FORWARD------------------------------")
        #print(forward)
        
        return forward