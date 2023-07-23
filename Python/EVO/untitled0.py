# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:04:14 2023

@author: jugwu
"""

import pygame

class Game(object):
    def __init__(self):
        super().__init__()
        self.background_colour = (255,255,255)
        self.dim = (300, 200)
        self.running = False
        self.init()
        
    def init(self):
        self.screen = pygame.display.set_mode(self.dim)
        pygame.display.set_caption('Tutorial 1')
        self.screen.fill(self.background_colour)
        pygame.display.flip()
        self.running = True
        return
    
    def run(self):
        while self.running:
            self.update()
            self.postUpdate()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
        pygame.quit()
        return
    
    def update(self):
        self.screen.fill(self.background_colour)
        return
    
    def postUpdate(self):
        return

if __name__ == '__main__':
    console = Game()
    console.run()
    