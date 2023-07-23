# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:32:46 2022

@author: Jugwu
"""

import re
import os
import numpy as np



#____________________________________

RENAME_FOLDER = 'DIR'

#____________________________________

def rename():
    urls = []
    with open('urls.txt', 'r',encoding='utf-8') as f:
        urls = f.readlines()
    f.close()
    
    #print(urls)
    cleanUrls = []
    
    for line in urls:
        line = re.sub('\n','', line)
        line = re.sub(r'https://','', line)
        line = re.sub(r'https://','POST::', line)
        line = re.sub('\+\+',' ', line)
        line = re.sub('\+',' ', line)
        line = re.sub(r'%3a%3e%3d','-vac-',line)
        line = re.sub(r'%3e','>',line)
        line = re.sub(r'%3d','=',line)
        line = re.sub(r'%28','(',line)
        line = re.sub(r'%29',')',line)
        cleanUrls.append(line)
    
    #print()
    #print(cleanUrls)
    
    names = []
    names = os.listdir(RENAME_FOLDER)

    for i in range(np.size(cleanUrls)):
        if 'chrome://newtab/' in cleanUrls[i]:
            names.insert(i, 'CHROME')
    
    #print(names)
    
    for url, name in zip(cleanUrls, names):
        if 'chrome://newtab/' not in url:
            os.rename(RENAME_FOLDER + '\\' + name ,RENAME_FOLDER + '\\' + url)
            print(url + "-->" + name)
        else:
            print(url + "-->" + name)
            
    
    return

#____________________________________

def main():
    
    rename()
    
    return 0
    
if __name__ == "__main__":
    main()