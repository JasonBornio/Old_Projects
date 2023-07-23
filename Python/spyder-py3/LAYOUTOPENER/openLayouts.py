# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import pyautogui as pa
from selenium.webdriver.firefox.options import Options
import numpy as np
import templates as t
options = Options()
options.add_argument("--kiosk") 
#options.add_argument("--headless")

pa.hotkey('win','ctrl','d') #will switch one desktop to the left
pa.hotkey('win','ctrl','right') #will switch one desktop to the right

driver = webdriver.Firefox(options=options)
driver.install_addon('C:\\Users\\Jugwu\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\46sqlau7.default-release\\extensions\\{dc9c8ad5-5054-4cde-b774-b4409f986887}.xpi',temporary=True)
driver.install_addon('C:\\Users\\Jugwu\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\46sqlau7.default-release\\extensions\\{6674730a-e591-43c6-8680-d332ea121cc2}.xpi',temporary=True)

#______________________________________________________



LAYOUT = t.lol



#______________________________________________________

def openMultipleLayouts(files):
    
    count = 0
    print(np.size(LAYOUT))
    for file in LAYOUT:
        if file == 'SKIP':
            pa.hotkey('win','ctrl','d') #will switch one desktop to the left
            pa.hotkey('win','ctrl','right') #will switch one desktop to the right
            driver.switch_to.new_window('window')
        else:
            openLayout(file)
            if (count < np.size(LAYOUT) - 1):
                pa.hotkey('win','ctrl','d') #will switch one desktop to the left
                pa.hotkey('win','ctrl','right') #will switch one desktop to the right
                driver.switch_to.new_window('window')
        count+=1
        
    return

def openLayout(file):
    
    url,pos,size ='','',''
    
    first = False
    custom = False
    with open('LAYOUTS\\' + file, 'r',encoding='utf-8') as f:
        i = 0
        lines = f.readlines()
        for line in lines:
            if('custom' in line.strip() or custom == True):
                custom = True
                if(i == 1):
                    posx = int(line.strip())                         
                if(i == 2):
                    posy = int(line.strip()) 
                if(i == 3):
                    sizex = int(line.strip())                        
                if(i == 4):
                    sizey = int(line.strip()) 
                if(i == 5):
                    url = line.strip()
                    if(first == True):
                        driver.switch_to.new_window('window')
                    first = True
                    custom = False
                    CustomOpenTab(url, posx,posy, sizex,sizey)
                    i = -1
            elif custom == False:
                if(i == 0):
                    pos = line.strip()                         
                if(i == 1):
                    size = line.strip()  
                if(i == 2):
                    url = line.strip()
                    if(first == True):
                        driver.switch_to.new_window('window')
                    first = True
                    openTab(url, pos, size)
                    i = -1
            i+=1
        f.close()
            
    return

def CustomOpenTab(url, posx, posy, sizex, sizey):
    x,y,width,height =posx,posy,sizex,sizey
    
    driver.get(url) 
    driver.set_window_size(width+12,height+7)
    driver.set_window_position(x-6, y-1)
    
    return 

def openTab(url, pos, size):
    x,y,width,height =0,0,0,0
    
    if(pos == 'TLL'):
        x, y = 0, 0
    if(pos == 'BLL'):
        x, y = 0, 577
    if(pos == 'TL'):
        x, y = 480, 0
    if(pos == 'BL'):
        x, y = 480, 577
    if(pos == 'TR'):
        x, y = 960, 0
    if(pos == 'BR'):
        x, y = 960, 577
    if(pos == 'TRR'):
        x, y = 1440, 0
    if(pos == 'BRR'):
        x, y = 1440, 577
    if(pos == 'TH1'):
        x, y = 0, 0
    if(pos == 'TH2'):
        x, y = 640, 0
    if(pos == 'TH3'):
        x, y = 1280, 0
        
    
    if(size == 'F'):
        width, height = 1920, 1154
    if(size == 'H'):
        width, height = 960, 1154
    if(size == 'DH'):
        width, height = 960, 577
    if(size == 'DV'):
        width, height = 480, 1154
    if(size == 'S'):
        width, height = 480, 577
    if(size == 'THIRD'):
        width, height = 640, 1154
    
        
    driver.get(url) 
    driver.set_window_size(width+12,height+7)
    driver.set_window_position(x-6, y-1)
    
    return 

#______________________________________________________

def main():
    
    openMultipleLayouts(LAYOUT)
    
    return 0
    
    
if __name__ == "__main__":
    main()