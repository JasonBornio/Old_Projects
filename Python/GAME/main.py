import time
import tkinter
import sys
from tkinter.filedialog import askopenfilename   

#-----------------------------
fname = "unassigned"
class ENGINE(object):
    def __init__(self):
        self.height = 250
        self.width = (self.height * 2)
        self.root = tkinter.Tk()
        self.pos = 0
        #############
        self.KEYSTATUS = ''
        self.wKEYPress = False
        self.wKEYRelease = False
        self.aKEYPress = False
        self.aKEYRelease = False
        self.sKEYPress = False
        self.sKEYRelease = False
        self.dKEYPress = False
        self.dKEYRelease = False
        ############
        
    
    def MainLoop(self):
        while(True):
            self.preUpdate()
            self.time()
            self.Update()
            self.postUpdate()
        return
    
    def StartUp(self):
        self.createWindow()
        self.MainLoop()
        return
    
    def createWindow(self):
        self.master = tkinter.Canvas(self.root, bg="white", height=self.height, width=self.width)
        self.master.pack()
        tkinter.Button(self.root, text='File Open', command = self.openFile).pack(fill=tkinter.X)
        return
    
    def time(self):
        time.sleep(0.001)
        self.pos +=1
        print(self.wKEYPress)
        return
    
    def Update(self):
        self.master.update_idletasks()
        self.master.update()
        #################
        self.master.create_rectangle(0,0, self.width, self.height, fill='red')  
        #################
        #self.master.update_idletasks()
        #self.master.update()
        return
    
    def preUpdate(self):
        self.processTriggers()
        return
    
    def onKeyPress(self, event):
        self.KEYSTATUS = event.char
        self.KEYSTATUS += 'PRESSED'
        
    def postUpdate(self):
        self.drawPixel()   
        #print("hi")
        
        return
    
    def drawPixel(self):
        self.master.create_line(10, 10, 20 + self.pos, 10 + self.pos)
        return
    
    def openFile(self):
        global fname
        fname = askopenfilename()
        self.root.destroy()
    
    def processTriggers(self):
        self.master.bind("<1>", lambda event: self.master.focus_set())
        self.master.bind('<Key>', self.onKeyPress)
        
        if self.KEYSTATUS == 'wPRESSED':
            self.wKEYPress = True
        else:
            self.wKEYPress = False
        if self.KEYSTATUS == 'aPRESSED':
            self.aKEYPress = True
        else:
            self.aKEYPress = False
        if self.KEYSTATUS == 'sPRESSED':
            self.sKEYPress = True
        else:
            self.sKEYPress = False
        if self.KEYSTATUS == 'dPRESSED':
            self.dKEYPress = True
        else:
            self.dKEYPress = False
        self.KEYSTATUS = ''
        return
#-----------------------------

def main():
    game = ENGINE()
    
    game.StartUp()
    
    
    print (fname)
    
    

    return 0
    
if __name__ == "__main__":
    main()