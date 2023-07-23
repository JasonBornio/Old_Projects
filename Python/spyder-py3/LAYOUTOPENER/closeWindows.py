# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:53:44 2022

@author: Jugwu
"""
from pyvda import VirtualDesktop,  get_virtual_desktops
import pyautogui as pa
import os

def close():
    
    current_desktop = VirtualDesktop.current().number
    number_of_active_desktops = len(get_virtual_desktops())
    length = number_of_active_desktops - current_desktop   
    os.system("taskkill /im firefox.exe /f")
    for i in range(length):
        pa.hotkey('win','ctrl','right') 
        pa.hotkey('win','ctrl','F4')
        
    return

def main():
    close()
    
if __name__ == "__main__":
    main()