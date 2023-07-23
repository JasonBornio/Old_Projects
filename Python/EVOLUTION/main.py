# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:40:27 2023

@author: Jugwu
"""

import fighter as f
import forms

def main():
    
    goku = f.creature()
    print(goku.battlePower())
    
    forms.ssj(goku)
    
    print(goku.battlePower())
    
    return 0
    
if __name__ == "__main__":
    main()