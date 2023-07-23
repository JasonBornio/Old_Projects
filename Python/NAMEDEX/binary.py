# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:27:50 2023

@author: Jugwu
"""

value = 8
format(value & 0xff, '8b')
array = bin(value & 0xff)


num = int(array, 2)


format(num & 0xff, '8b')
binary = bin(num  & 0xff)


singed = int(binary, 2)

print(array)
print(num)
print(binary)
print(singed)