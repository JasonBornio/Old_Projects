# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:37:32 2023

@author: jugwu
"""

import matplotlib.pyplot as plt
import numpy as np
import math

num_locs = 10

numValues = 10000
maxValue = (num_locs - 1) + 2

mean = 0 
sd = 2.5
random = np.random.normal(mean, sd, size = numValues)
print(random)
random = random * maxValue
rand = random - maxValue / 2

plt.hist(random,100,density=True, color = 'red', alpha=0.2)
plt.show()

list_ = []
for i in range(numValues):
    index = np.random.randint(numValues)
    num = random[index]
    #print(int(num))
    if num < 0:
        pass
    else:
        list_.append(math.floor(num))
#print(list_)
sum_ = np.zeros(num_locs)
for num_ in list_:
    sum_[num_] += 1
print(sum_)
    
    