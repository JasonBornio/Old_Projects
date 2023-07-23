# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:37:48 2022

@author: Jugwu
"""
import natsort 
import os
from pathlib import Path

FOLDER = 'C:\\'

def LINKS():
    files =[]
    files2 = []
    files = sorted(Path(FOLDER).iterdir(), key=os.path.getctime)

    for file in files:
        
        filename = os.fsdecode(file)
        files2.append(filename)
        
    files3 = natsort.natsorted(files2,reverse=True)
    with open('FILES\\LINKS.txt', 'w',encoding='utf-8') as f:
        for file in files3:
            f.write(file)
            f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()

    return


def main():
    
    LINKS()
    
    return 0
    
if __name__ == "__main__":
    main()