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
import NeuralNet as nn


#______________________________________________________


DIRECTORY = 'DIR\\'

NAME = 'name'
#______________________________________________________
PATH = "LAYOUTS\\"

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
            elif ".txt" in line:
                width = 480
                height = 480
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
            mlp = nn.MultiLayerPerceptron(3, 3, 0,70)
            mlp.load('LAYOUT3.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = H2DV()
            elif maxVal == 1:
                pos, size = H2DH()
            else:
                pos,size = THIRDS()
                
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
            mlp = nn.MultiLayerPerceptron(7, 2, 0,80)
            mlp.load('LAYOUT7.txt')
            training_data = []
            training_data.append(w_h_Ratios)
            labels =[[1]]
            predicted_values = mlp.predict(training_data,labels, show=(False))
             
            maxVal = np.argmax(predicted_values[0])
            #print(maxVal)
            
            if maxVal == 0:
                pos, size = S1DV()
            else:
                pos, size = S1DH()
                
        

    return pos, size
    
    
def createLayout(name):
    with open('FILES\\names.txt', 'a',encoding='utf-8') as f:
        newname = re.sub(r'\\', '_', DIRECTORY + name)
        f.write("\n" + newname +" = [")
        f.close()
    
    saveNow = False
    flag = ''
    urls1 = []
    count2 = 0
    with open('FILES//multiLayouts.txt', 'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub("\n","", line)
            
            if 'chrome://newtab/' in line:
                saveNow = True
            elif 'https://www.youtube.com/' in line:
                saveNow = True
                flag = 'FLG'
            
            if saveNow == True:
                saveNow = False
                with open('FILES\\newLayout.txt', 'w',encoding='utf-8') as f2:
                    for url in urls1:
                        print(url)
                        print(count2)
                        f2.write(url)
                        f2.write('\n')  
                    f2.close()
                urls1 = []     
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
    
        
                pos, size = choseTemplate3(w_h_Ratios, num)
                #pos, size = choseTemplate(w_h_Ratios, num)

                if DIRECTORY != '' and os.path.exists(PATH + DIRECTORY) == False:
                    os.mkdir(PATH + DIRECTORY) 
       
                with open(PATH + DIRECTORY + flag + name +' (' + str(count2) + ').txt', 'w',encoding='utf-8') as f:
                    for i in range(num):
                        f.write(pos[i])
                        f.write("\n")
                        f.write(size[i])
                        f.write("\n")
                        f.write(urls[i])
                        if i < num-1:
                            f.write("\n")
                
                    f.close()
                nam = flag + name +' (' + str(count2) + ')'
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
                flag = ''
                count2 += 1
            else:
                urls1.append(line)
                
        f.close()
        
    
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
def THIRDS():
    return ['TH1','TH2','TH3'],['THIRD','THIRD','THIRD']

#______________________________________________________
def main():
    
    if os.path.isfile(PATH + DIRECTORY + NAME + ' (0).txt'):
        print("SORRY THIS TEMPLATE ALREADY EXISTS!!!")
    else:
        createLayout(NAME)
    
    
    return 0
    
if __name__ == "__main__":
    main()