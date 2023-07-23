# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:44:16 2023

@author: jugwu
"""
import os
from PIL import Image
import natsort 
from pytesseract import pytesseract
from googletrans import Translator
import time

LOADFOLDER = "source\\"
SAVEFOLDER = "translations\\"

extensions = [".png",".jpg",".jpeg"]

path_to_tesseract = r"C:\Users\jugwu\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

translator = Translator()
translator.raise_Exception = True
#============================

def printProgressBar (iteration, total,loss, prefix = '', suffix = '', decimals = 3, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    los = ("{0:." + str(10) + "f}").format(float(loss))
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}%', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()    
     

def downloadText():
    subfolders = [ f.name for f in os.scandir(LOADFOLDER) if f.is_dir() ]
    folder = ""
    for name in subfolders:
        if "translation" not in name:
            folder = name
            
    print(folder)
    images = []
    for image in os.listdir(LOADFOLDER + folder):
        for ext in extensions:
            if (image.endswith(ext)):
                images.append(image)
    
    images = natsort.natsorted(images,reverse=False)
    print(images)
    
    pytesseract.tesseract_cmd = path_to_tesseract
    text = []
    count = 0
    total = len(images)
    for image in images:
        img = Image.open(LOADFOLDER + folder + "\\" + image)
        text.append(pytesseract.image_to_string(img,  lang='jpn_vert'))
        printProgressBar(count, total, 0, prefix = 'Progress:', suffix = 'Complete', length = 18)
        count += 1
    
    print()
    #for string in text:
        #print("--------")
        #print(string)
    
    translation = []
    count = 0
    total = len(text)
    with open(SAVEFOLDER + folder + ".txt", 'a', encoding="utf-8") as f:
        for sentence in text:
            if len(sentence) > 5:
                print(str(sentence))
                trans_text = translator.translate(str(sentence), src='ja', dest='en').text
                translation.append(trans_text)
                printProgressBar(count, total, 0, prefix = 'Progress:', suffix = 'Complete', length = 18)
                f.write("--------------------------\nPage " + str(count+1) + ":")
                f.write(trans_text + "\n")
            count += 1
            
    f.close()
        
    print()
    print("page1")
    print(translation[0])
    print("page3")
    print(translation[2])
    
        
            
    return

#庸 ( 医 木 輝 巳 に E 世 W ロ e : ロ エ ュ ぺ 森
#心 ひ モ ご 蚕 刊 G ド せ ト ュ ロ る や n ぃ そ っ i つ ら [


def main():
    downloadText()
    return 0


main()