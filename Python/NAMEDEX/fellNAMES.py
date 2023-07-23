# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:42:11 2023

@author: Jugwu
"""

#_______________________________

PATH = 'NAMES\\'
FILE = 'text2'
OUTPUT = 'testTEXT4'

DATES = ['Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul', 'Aug ', 'Sep ', 'Oct ', 'Nov ', 'Dec ']
KEYS = ['Archive', 'Poll', 'Voting', 'Comments', 'raffle', 'Event', 'Translated']

newFile = []

def rename():
    newText = False
    write = False
    count = 0
    with open(PATH + FILE + '.txt', 'r',encoding='utf-8') as f:
        for line in f.readlines():
            if newText == False:
                for date in DATES:
                    if date in line:
                        newText = True
                        newFile.append('\n_______________________________________\n')
                        newFile.append('\n.')
                        newFile.append('\n_______________________________________\n')
                        count = 0      
            if newText == True:
                #if count == 0:
                 #   nothing = 0
                write = False
                if line == ('\n' or '\n ' or '\n  ' or '' or ' '):
                    count-=1
                else:# if count > 0:
                    write = True
                    for keyword in KEYS:
                        if keyword in line:
                            write = False
                    
                if write == True:
                    newFile.append(line)
                    written = True
                
                if count == 1 and written == True:
                    newFile.append('---------------------------------------\n')
                    written = False
                                
                count += 1   
    
                if count == 5:
                    newText = False
            
    f.close()
    return 

def showFile(file):
    count = 0
    for line in file:
        print(str(count) + ": " + line)
        count += 1
    return

def writeFile():
    file = formatText()
    with open(PATH + OUTPUT + '.txt', 'w',encoding='utf-8') as f:
        for line in file:
            f.write(line)
            #f.write('\n')
    f.close()
    showFile(file)
    #print(file)
    
    return

def formatText():
    count = 0
    lines = []
    formatted = []
    
    for line in newFile:
        lines = line.split()
        count = 0
        for word in lines:
            if count % 6 == 0:
                lines.insert(count, ' \n ')
            count+=1
        formatted.append(' '.join(lines))
    
    return formatted

#_______________________________

def main():
    rename()
    writeFile()
    return

if __name__ == "__main__":
    main()