# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:37:48 2022

@author: Jugwu
"""

import cv2
import re
from PIL import Image
import numpy as np
import os
from pathlib import Path
import NeuralNet as nn
import matplotlib.pyplot as plt
import DATA as dp
import itertools

#______________________________________________________

TEST = True

FOLDERSAVE = False
#FOLDERSAVE = True
EPOCHS = 3
ALL = False

DIRECTORY = 'Pokimane'

NAME = 'poki'

#FOLDER = 'C:\\Users\\Jugwu\\.code\\logs2\\logs1\\logs1\\logs2\\logs1\\WOW\\TRANSFER\\\ssdf\\saves3'
#FOLDER = 'C:\\Users\\Jugwu\\Downloads\\DOWNPO\\huge'
#FOLDER = 'C:\\Users\\Jugwu\\.code\\logs2\\logs1\\logs1\\logs2\\logs1\\WOW\\TRANSFER\\instantclassics\\SORT\\TAGS\\finalNomercy'
FOLDER = 'C:\\Users\\Jugwu\\.code\\logs2\\logs1\\logs1\\logs2\\logs1\\MEGA\\REDDIT\\POKI'


#______________________________________________________
PATH = "LAYOUTS\\"

EXTENSIONS = ['.png', '.jpg', '.jpeg','.jfif','.webp',
              '.gif',
              '.mp4','.m4v','.webm','.avi','.mpeg']
              
FOLDEXTENSIONS = ['.png', '.jpg', '.jpeg','.jfif','.webp',
              '.gif',
              '.mp4','.m4v','.webm','.avi','.mpeg','.ini','.csv','.txt','.log']

functions = []
#______________________________________________________
def getDimensions():
    with open('FILES\\newLayout.txt', 'r',encoding='utf-8') as f:
        lines = f.readlines()
        video = False
        num = 0
        widthVect = []
        heightVect = []
        url = []
        for line in lines:
            line = re.sub("\n","", line)
            url.append(line)
            line = re.sub("file:///", '', line)
            line = re.sub("%C3%B3","ó", line)
            line = re.sub("%20"," ", line)
            #print(line)          
            
            if ".mp4" in line:
                #print("MP444444444444")
                video = True
            elif ".webm" in line:
                #print("WEBMMMMMMMMMMM")
                video = True
            elif ".avi" in line:
                #print("AVIIIIIIIIIIII")
                video = True
            elif ".mov" in line:
                #print("MOVVVVVVVVVVVV")
                video = True
            elif ".mpeg" in line:
                #print("MPEGGGGGGGGGGG")
                video = True
            elif ".m4v" in line:
                #print("M4AAAAAAAAAAAA")
                video = True
                
            if video == True:
                vid = cv2.VideoCapture(line)
                height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
                width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
                video = False
                
            else:
                im = Image.open(line)
                width, height = im.size
                
            #print("height:")
            #print(height)
            #print("weight:")
            #print(width)
            
            widthVect.append(width)
            heightVect.append(height)
            num += 1
        #print(url)        
        f.close()
    return widthVect, heightVect, num, url

def choseTemplate(w_h_Ratios, num):
    
    labels = []
    SWide, Wide, Tall, STall, Square = 0,0,0,0,0
    for ratio in w_h_Ratios:
        if ratio >= 1.5:
            labels.append("SWide")
            SWide += 1
        elif ratio < 1.5 and ratio >= 1.10:
            labels.append("Wide")
            Wide += 1
        elif ratio <= 0.9 and ratio > 0.7:
            labels.append("Tall")
            Tall += 1
        elif ratio <= 0.7:
            labels.append("STall")
            STall += 1
        else:
            labels.append("Square")
            Square += 1
            
    print(labels)
    
    pos, size = [],[]
    
    if num == 1:
        pos, size = F()
        
    if num == 2:
        pos, size = H()
        
    if num == 3:
        if STall > 0:
            if SWide > 0 or Wide > 0:
                pos, size = H2DH()
            else:
                pos, size = H2DV()
        elif STall == 3:
            pos, size = H2DV()
        else:
            pos, size = H2DH()

    if num == 4:
        if STall == 4 or Tall == 4:
            pos, size = DV()
        elif SWide == 4 or Wide == 4:
            pos, size = DH()
        elif STall >0:
            if SWide == 2 or Wide == 2:
                pos, size = DV2DH()
            else:
                pos, size = H2S1DV()
        elif Wide == 1 or SWide == 1:
            pos, size = H2S1DH()
        elif Tall == 2: 
            pos, size = H2S1DH()
        else:
            pos, size = DV2DH()

    if num == 5:
        if STall == 3:
            if Wide == 1 or SWide == 1:
                pos, size = DV2S1DH()
            else:
                pos, size = DV2S1DV()
        elif Tall == 3:
            if Wide == 1 or SWide == 1:
                pos, size = DV2S1DH()
            else:
                pos, size = H4S()
        else:
            pos, size = H4S()
                                    
    if num == 6:
        if STall == 2:
            if Tall == 4:
                pos, size = DV4S()
            elif Wide == 1 or SWide == 1:
                pos, size = S2DH()
            else:
                pos, size = DV4S()
        elif Tall == 4:
            if Wide ==1 or SWide == 1:
                pos, size = S2DH()
            else:
                pos, size = DV4S()
        else:
            pos, size = S2DH()     
           
    if num == 7:
        if STall == 1:
            pos, size = S1DV()
        elif SWide == 1:
            pos, size = S1DH()
        elif Tall > 0:
            pos, size = S1DV()
        else:
            pos, size = S1DH()
        
    if num == 8:
        pos, size = S()
        
    if num == 9:
        print(9)
        
    print(pos)
    print(size)
    return pos, size

def choseTemplate2(w_h_Ratios, num,widths,heights):
    

    
    pos, size = [],[]
    score =0
    
    
    if num == 1:
        pos, size = F()
    if num == 2:
        pos, size = H()
    if num == 3:
        minVal = 0
        score =0
        for i in range(num):
            if i == 0:
                score += Hscore(w_h_Ratios[i])
            if i == 1:
                score += DVscore(w_h_Ratios[i])
            if i == 2:
                score += DVscore(w_h_Ratios[i])
        minVal = score/3
        print(score/3)
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(w_h_Ratios[i])
            if i == 1:
                score += DHscore(w_h_Ratios[i])
            if i == 2:
                score += Hscore(w_h_Ratios[i])
        print(score/3)
        if (score / 3) > minVal:
            pos,size = H2DH()
        else:
            pos,size = H2DV()
    if num == 4:
        minVal = 0
        score =0
        index =[]
        for i in range(num):
            if i == 0:
                score += Hscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += DVscore(w_h_Ratios[i])
        minVal = score/4
        index = 0
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(w_h_Ratios[i])
            if i == 1:
                score += Hscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
        if (score / 4) > minVal:
            index = 1
            minVal = score/4
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(w_h_Ratios[i])
            if i == 1:
                score += DHscore(w_h_Ratios[i])
            if i == 2:
                score += DVscore(w_h_Ratios[i])
            if i == 3:
                score += DVscore(w_h_Ratios[i])
        if (score / 4) > minVal:
            index = 2
            minVal = score/4
        score = 0
        for i in range(num):
            if i == 0:
                score += DVscore(w_h_Ratios[i])
            if i == 1:
                score += DVscore(w_h_Ratios[i])
            if i == 2:
                score += DVscore(w_h_Ratios[i])
            if i == 3:
                score += DVscore(w_h_Ratios[i])
        if (score / 4) > minVal:
            index = 3
            minVal = score/4
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(w_h_Ratios[i])
            if i == 1:
                score += DHscore(w_h_Ratios[i])
            if i == 2:
                score += DHscore(w_h_Ratios[i])
            if i == 3:
                score += DHscore(w_h_Ratios[i])
        if (score / 4) > minVal:
            index = 4
            minVal = score/4
            
        if index == 0:
            pos, size = H2S1DV()
        if index == 1:
            pos, size = H2S1DH()
        if index == 2:
            pos, size = DV2DH()
        if index == 3:
            pos, size = DV()
        if index == 4:
            pos, size = DH()
    if num == 5:
        minVal = 0
        score =0
        index =[]
        for i in range(num):
            if i == 0:
                score += Hscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
            if i == 4:
                score += Sscore(w_h_Ratios[i])
        minVal = score/5
        index = 0
        score = 0
        for i in range(num):
            if i == 0:
                score += Sscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += DVscore(w_h_Ratios[i])
            if i == 3:
                score += DVscore(w_h_Ratios[i])
            if i == 4:
                score += DVscore(w_h_Ratios[i])
        if (score / 5) > minVal:
            index = 1
            minVal = score/5
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(widths[i], heights[i])
            if i == 1:
                score += Sscore(widths[i], heights[i])
            if i == 2:
                score += Sscore(widths[i], heights[i])
            if i == 3:
                score += DVscore(widths[i], heights[i])
            if i == 4:
                score += DVscore(widths[i], heights[i])
        if (score / 5) > minVal:
            index = 2
            minVal = score/5
            
        if index == 0:
            pos, size = H4S()
        if index == 1:
            pos, size = DV2S1DV()
        if index == 2:
            pos, size = DV2S1DH()

    if num == 6:
        print("SIIIIIIIIIIIIIIXXXX")
        minVal = 0
        score =0
        for i in range(num):
            if i == 0:
                score += Sscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
            if i == 4:
                score += DVscore(w_h_Ratios[i])
            if i == 5:
                score += DVscore(w_h_Ratios[i])
        minVal = score/6
        print(score/6)
        score = 0
        for i in range(num):
            if i == 0:
                score += Sscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
            if i == 4:
                score += DHscore(w_h_Ratios[i])
            if i == 5:
                score += DHscore(w_h_Ratios[i])
        print(score/6)
        if (score / 6) > minVal:
            pos,size = S2DH()
        else:
            pos,size = DV4S()
    if num == 7:
        minVal = 0
        score =0
        for i in range(num):
            if i == 0:
                score += Sscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
            if i == 4:
                score += Sscore(w_h_Ratios[i])
            if i == 5:
                score += Sscore(w_h_Ratios[i])
            if i == 6:
                score += DVscore(w_h_Ratios[i])
        minVal = score/7
        score = 0
        for i in range(num):
            if i == 0:
                score += DHscore(w_h_Ratios[i])
            if i == 1:
                score += Sscore(w_h_Ratios[i])
            if i == 2:
                score += Sscore(w_h_Ratios[i])
            if i == 3:
                score += Sscore(w_h_Ratios[i])
            if i == 4:
                score += Sscore(w_h_Ratios[i])
            if i == 5:
                score += Sscore(w_h_Ratios[i])
            if i == 6:
                score += Sscore(w_h_Ratios[i])
        if (score / 7) > minVal:
            pos,size = S1DH()
        else:
            pos,size = S1DV()
    if num == 8:
        pos, size = S() 
    print(pos)
    print(size)
    return pos, size

def choseTemplate3(w_h_Ratios, num):
    
    if num == 1:
        pos, size = F()
    elif num == 2:
        pos, size = H()
    elif num == 8:
        pos, size = S()
    else:
        
                #2 H2DH
        #3 H2S1DV
        #4 H2S1DH
        #5 4DV
        #6 4DH
        #7 2DV2DH
        #8 H2S1DH
        #9 H4S
        #10 DV2S1DV
        #11 DV2S1DH
        #12 DV2S2DH
        #13 DH2S1
        #14 DV4S
        #15 S2DH
        #16 S1DV
        #17 S1DH
        
        if num == 3:
            mlp = nn.MultiLayerPerceptron(3, 2, 0,32)
            mlp.load('LAYOUT3.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = H2DH()
            else:
                pos, size = H2DV()
                
        if num == 4:
            mlp = nn.MultiLayerPerceptron(4, 5, 0,80)
            mlp.load('LAYOUT4.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = H2S1DV()
            elif maxVal == 1:
                pos, size = H2S1DH()
            elif maxVal == 2:
                pos, size = DV()
            elif maxVal == 3:
                pos, size = DH()
            else:
                pos, size = DV2DH()
                
        if num == 5:
            mlp = nn.MultiLayerPerceptron(5, 5, 0,80)
            mlp.load('LAYOUT5.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = H4S()
            elif maxVal == 1:
                pos, size = DV2S1DV()
            elif maxVal == 2:
                pos, size = DV2S1DH()
            elif maxVal == 3:
                pos, size = DV2S2DH()
            else:
                pos, size = DH2S1()
         
        if num == 6:
            mlp = nn.MultiLayerPerceptron(6, 2, 0,32)
            mlp.load('LAYOUT6.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = DV4S()
            else:
                pos, size = S2DH()
                
        if num == 7:
            mlp = nn.MultiLayerPerceptron(7, 2, 0,32)
            mlp.load('LAYOUT7.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = DV4S()
            else:
                pos, size = S2DH()
                
        
            
        
       # i = maxVal
        
       # if i == 0:
       #     pos, size =H2DV()
        #if i == 1:
        #    pos, size =H2DH()
        #if i == 2:
        #    pos, size =H2S1DV()
        #if i == 3:
         #   pos, size =H2S1DH()
        #if i == 4:
         #   pos, size =DV()
        #if i == 5:
      #      pos, size =DH()
      #  if i == 6:
      ##      pos, size =DV2DH()
     #   if i == 7:
      #      pos, size =H2S1DH()
     #   if i == 8:
      #      pos, size =H4S()
    #    if i == 9:
     #       pos, size =DV2S1DV()
     #   if i == 10:
     #       pos, size =DV2S1DH()
     #   if i == 11:
     #       pos, size =DV2S2DH()
      #  if i == 12:
     #       pos, size =DH2S1()
     #   if i == 13:
      ##      pos, size =DV4S()
      #  if i == 14:
      #      pos, size =S2DH()
      #  if i == 15:
      #      pos, size =S1DV()
      #  if i == 16:
        #    pos, size =S1DH()

    return pos, size
    
def createLayout(name):
    
    widths, heights, num, url = getDimensions()
    
    #print("widths:")
    #print(widths)
    #print("heights")
    #print(heights)
    
    w_h_Ratios = np.divide(widths, heights)
    
    #print("RATIO:")
    #print(w_h_Ratios)
    
    rats = w_h_Ratios
    
    urls = []
    
    for i in range(num):
        maxVAL = 0
        index = 0
        count = 0
        for value in rats:
            if value > maxVAL:
                maxVAL = value
                index = count
            count += 1
                
        urls.append(url[index])
        rats[index] = 0
        
    
    w_h_Ratios = np.divide(widths, heights)
        
    #print("RATIO:")
    #print(w_h_Ratios)
    #print(url)
    #print(urls)
    
        
    pos, size = choseTemplate(w_h_Ratios, num)
    #pos, size = choseTemplate(w_h_Ratios, num)
    nam = ''
    nam = name
    after = ''
    if ALL:
        direct = nam.split('\\')
        for i in range(len(direct) - 1):
            after += direct[i] + '\\'
            i+=2
        print('AFTER:' +after)
        
    if DIRECTORY != '' and os.path.exists(PATH + DIRECTORY + after) == False:
        if  ALL:
            if os.path.exists(PATH + DIRECTORY) == False:
                os.mkdir(PATH + DIRECTORY) 
            for i in range(len(direct) - 1):
                after += direct[i] + '\\'
                print(after)
                os.mkdir(PATH + DIRECTORY + after) 
                i+=2
            print('AFTER:' +after)
        else:
            os.mkdir(PATH + DIRECTORY) 
       
            
    
    with open(PATH + DIRECTORY + name + '.txt', 'w',encoding='utf-8') as f:
        for i in range(num):
            f.write(pos[i])
            f.write("\n")
            f.write(size[i])
            f.write("\n")
            f.write(urls[i])
            if i < num-1:
                f.write("\n")
                
        f.close
    
    return

def multifolder():

    files = Path(FOLDER).iterdir()
    Loop = True
    filesBefore = 0
    FINALIST = []
    while Loop == True: 
        folderList = []
        Loop = False
        for file in files:
            filename = os.fsdecode(file)
            name = True
            for ext in FOLDEXTENSIONS:
                if ext in filename.lower():
                    name = False
                    
            if name == True:      
                folderList.append(file)
                FINALIST.append(file)
                Loop = True
         
        one = True      
        files = []
        for folder in folderList:
            if one:
                files = Path(folder).iterdir()
                #print(files)
                one = False
            else:
                #print("\nFOLDER:   " + str(folder))
                files = itertools.chain(files, Path(folder).iterdir())
       
        
        #print(np.size(filesBefore))
        if np.size(folderList) == filesBefore:
            Loop = False
        else:
            filesBefore = 0
            filesBefore += np.size(folderList)
                
        #print("\n\nFOLDER:")
        #print(FINALIST)
        #print("\n\nFILES:")
        #print(files)
       # print(np.size(folderList))
        
    name = ''
    for folder in FINALIST:
        #print(string)
        name = str(folder).replace(FOLDER, "")        
        folderSave(str(folder), name)

    
    
    return

def folderSave(folder, name):
    
    count = 0
    urls = []
    namecount = 0
    
    with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
        newname = re.sub(r'\\', '_', name)
        f.write("\n" + newname +" = [")
        f.close()
        
        
        
        
    #print(folder)  
    files =[]
    files2  = sorted(Path(folder).iterdir(), key = os.path.getctime)
    size = np.size(files2)
    for i in range (size):
        files.append(files2[(size - 1) - i])
    for file in files:
        
        filename = os.fsdecode(file)
        for ext in EXTENSIONS:
            if ext in filename.lower():

                fold = re.sub (r'\\','/', filename)
                fold = re.sub (r'Ã³','ó', fold)
                filepath = 'file:///' + fold

                urls.append(filepath)
                #print(urls)
        
                if count == EPOCHS - 1:
                    count = -1
                    open('FILES\\newLayout.txt', 'w').close()
                    with open('FILES\\newLayout.txt', 'w',encoding='utf-8') as f:
                        for url in urls:
                            f.write(url)
                            f.write('\n')
                    urls = []
                    
                    nam = name +' (' + str(namecount) + ')'
                    createLayout(nam)
                    with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
                        f.write("'")
                        for letter in DIRECTORY:
                            if letter == '\\':
                                f.write('\\\\')
                            else:
                                f.write(letter)
                        for letter in nam:
                            if letter == '\\':
                                f.write('\\\\')
                            else:
                                f.write(letter)
                
                        f.write('.txt' + "',")
                        f.write('\n')
                        f.close
                    namecount += 1
                    #print('ok')
                count += 1
        
    if np.size(urls) > 0:
        open('FILES\\newLayout.txt', 'w').close()
        with open('FILES\\newLayout.txt', 'w',encoding='utf-8') as f:
            for url in urls:
                f.write(url)
                f.write('\n')
        urls = []
        nam = name +' (' + str(namecount) + ')'
        createLayout(nam)
        with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
            f.write("'")
            for letter in DIRECTORY:
                if letter == '\\':
                    f.write('\\\\')
                else:
                    f.write(letter)
            for letter in nam:
                if letter == '\\':
                    f.write('\\\\')
                else:
                    f.write(letter)
                
            f.write('.txt' + "',")
            f.write('\n')
            f.close

            
    with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
        f.write("]")
        f.close()
        
    return   
#______________________________________________________
def sigmoid(inpu):
    return 1/(1+np.exp(-inpu))

def Fscore(ratio):
    RAT = sigmoid(1920/1154)
    ratio = sigmoid(ratio)
    if RAT > ratio:
        return RAT - ratio
    else:
        return ratio - RAT
def Hscore(ratio):
    RAT = sigmoid(960/1154)
    ratio = sigmoid(ratio)
    print("RAT   " + str(RAT))
    print("ratio " + str(ratio))
    if RAT > ratio:
        return RAT - ratio
    else:
        return ratio - RAT
def DHscore(ratio):
    RAT = sigmoid(960/577)    
    ratio = sigmoid(ratio)
    print("RAT   " + str(RAT))
    print("ratio " + str(ratio))
    if RAT > ratio:
        return RAT - ratio
    else:
        return ratio - RAT
def DVscore(ratio):
    RAT = sigmoid(480/1154)
    ratio = sigmoid(ratio)
    print("RAT   " + str(RAT))
    print("ratio " + str(ratio))
    if RAT > ratio:
        return RAT - ratio
    else:
        return ratio - RAT
def Sscore(ratio):
    RAT = sigmoid(480/577)
    ratio = sigmoid(ratio)
    if RAT > ratio:
        return RAT - ratio
    else:
        return ratio - RAT
        
#______________________________________________________
def subset(predicted_values, num):
    if num == 3:
        return np.argmax(predicted_values[:2])
    if num == 4:
        return np.argmax(predicted_values[2:8]) +2
    if num == 5:
        #print(np.argmax(predicted_values[8:13]))
        return np.argmax(predicted_values[8:13]) + 8
    if num == 6:
        #print(np.argmax(predicted_values[13:15]))
        return np.argmax(predicted_values[13:15]) +13
    if num == 7:
        return np.argmax(predicted_values[15:]) +15

def F():
    return ['TLL'],['F']
def H():
    return ['TLL', 'TR'],['H','H']
def H2DV():
    return ['TLL','TR','TRR'],['H','DV','DV']
def H2S1DV():
    return ['TLL','TR','BR','TRR'],['H','S','S','DV']
def H4S():
    return ['TLL', 'TR','BR','TRR','BRR'],['H','S','S','S','S']
def H2DH():
    return ['TR','BR','TLL'],['DH','DH','H']
def H2S1DH():
    return ['BR','TLL','TR','TRR'],['DH','H','S','S']
def DV():
    return ['TLL','TL','TR','TRR'],['DV','DV','DV','DV']
def DH():
    return ['TLL','TR','BLL','BR'],['DH','DH','DH','DH']
def DV2S1DV():
    return ['TLL','BLL','TL','TR','TRR'],['S','S','DV','DV','DV']
def DV4S():
    return ['TLL','BLL','TL','BL','TR','TRR'],['S','S','S','S','DV','DV']
def DV2DH():
    return ['TLL','BLL','TR','TRR'],['DH','DH','DV','DV']
def DV2S1DH():
    return ['TLL','BLL','BL','TR','TRR'],['DH','S','S','DV','DV']
def S1DV():
    return ['TLL','BLL','TL','BL','TR','BR','TRR'],['S','S','S','S','S','S','DV']
def S():
    return ['TLL','BLL','TL','BL','TR','BR','TRR','BRR'],['S','S','S','S','S','S','S','S']
def S2DH():
    return ['TLL','BLL','TR','BR','TRR','BRR'],['DH','DH','S','S','S','S']
def S1DH():
    return ['TLL','BLL','BL','TR','BR','TRR','BRR'],['DH','S','S','S','S','S','S']
def DV2S2DH():
    return ['TLL','BLL','TR','BR','TRR'],['DH','DH','S','S','DV']
def DH2S1():
    return ['TLL','BLL','TR','BR','BRR'],['DH','DH','DH','S','S']
def shuffle(datas):
    datas2 = []
    for data in datas:
        data2 = []
        for d in data:
            rand = ((np.random.rand() * 2) -1) * (d *0.25)
            d = d + rand
            data2.append(d)
        datas2.append(data2)
    return datas2
        
#______________________________________________________
def main():

    functions.append(H2DV())
    functions.append(H2DH())
    functions.append(H2S1DV())
    functions.append(H2S1DH())
    functions.append(DV())
    functions.append(DH())
    functions.append(DV2DH())
    functions.append(H2S1DH())
    functions.append(H4S())
    functions.append(DV2S1DV())
    functions.append(DV2S1DH())
    functions.append(DV2S2DH())
    functions.append(DH2S1())
    functions.append(DV4S())
    functions.append(S2DH())
    functions.append(S1DV())
    functions.append(S1DH())

    
    if TEST == False:
        if ALL == True:
            multifolder()
            
        elif FOLDERSAVE == True:
            if os.path.isfile(PATH + DIRECTORY + NAME + ' (0).txt '):
                print("SORRY THIS TEMPLATE ALREADY EXISTS!!!")
            else:
                folderSave(FOLDER, NAME) 
        else:
            if os.path.isfile(PATH + DIRECTORY + NAME + '.txt'):
                print("SORRY THIS TEMPLATE ALREADY EXISTS!!!")
            else:
                createLayout(NAME)
                with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
                    f.write("'" + DIRECTORY + NAME + '.txt' +"',")
                    f.write('\n')
    
    if TEST == True:
        
        #inputs are 5 values 
        #sorted with highest ratios at top
        #0 ratios for rest
        #outs are 18 
        
        #1 H2DV
        #2 H2DH
        #3 H2S1DV
        #4 H2S1DH
        #5 4DV
        #6 4DH
        #7 2DV2DH
        #8 H2S1DH
        #9 H4S
        #10 DV2S1DV
        #11 DV2S1DH
        #12 DV2S2DH
        #13 DH2S1
        #14 DV4S
        #15 S2DH
        #16 S1DV
        #17 S1DH
        
        mlp = nn.MultiLayerPerceptron(3, 2, 0,60)
        
        training_data = dp.training_data3
       
        labels = dp.labels3
        

        #print(np.shape(training_data))
        #print(np.shape(labels))
        mlp.setEtaAplha(0.03, 0.05)
        mlp.setEtaAplha(0.007, 0.005)
        #mlp.setEtaAplha(0.002, 0.007)
        mlp.setThreshold(0.0277)
        mlp.load('LAYOUT3.txt')

        #mlp.train(10,training_data, labels,stopCondition = False,lossPlot=(True))
        mlp.save('LAYOUT3.txt')
        #mlp.save('saveS2.txt')
        predicted_values = mlp.predict(training_data,labels, show=(True))
        
        index = 0
        for i in range(mlp.outputLength):
            
            if i < 2:
                #print(i)
                index = 3
            elif i < 8:
                #print(i)
                index = 4
            elif i < 13:
                #print("i:" + str(i))
                index = 5
            elif i < 15:
                #print("j:" + str(i))
                index = 6
            else:
                index = 7
                
            maxVal = subset(predicted_values[i],index)
            maxVal = np.argmax(predicted_values[i])
            plt.figure() 
            plt.plot(predicted_values[i])
            plt.plot(labels[i])
            plt.title(f"predictions vs labels {i}: {maxVal}")
            plt.xlabel('predicted')
            plt.ylabel('labels')
            plt.show()
    
        #plot histogram of polarities

    

        
    
    return 0
    
if __name__ == "__main__":
    main()