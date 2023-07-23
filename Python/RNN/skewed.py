# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:11:20 2023

@author: jugwu
"""

from scipy.stats import skewnorm
import numpy as np
import math

def skew(num):
    num_locs = num

    numValues = 10000
    maxValue = ((num_locs * 2) - 1)
    skewness = 0  #Negative values are left skewed, positive values are right skewed.

    random = skewnorm.rvs(a = skewness,loc=maxValue, size=numValues)  #Skewnorm function

    random = random - min(random)      #Shift the set so the minimum value is equal to zero.
    random = random / max(random)      #Standadize all the vlues between 0 and 1. 
    random = random * maxValue   
    random = random - (num_locs)      #Multiply the standardized values by the maximum value.
    
    list_ = []
    for i in range(numValues):
        index = np.random.randint(numValues)
        num = random[index]
        number = math.floor(num)
        if number == 0:
            number = np.random.randint(maxValue + 1) - num_locs 
        if number == 0:
            if np.random.rand() < 0.5:
                number = 1 
            else:
                number = -1
        list_.append(math.floor(number))
        
    
    max_index = np.shape(list_)[0]
    sum_ = np.zeros(num_locs * 2)
    
    for num_ in list_:
        sum_[num_+num_locs] += 1

    return list_, max_index

    
    