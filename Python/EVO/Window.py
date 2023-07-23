# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:04:14 2023

@author: jugwu
"""

import pygame
import globalVars as globs
from ball import Ball
from Paddles import Paddle

BLUE =      (  0,   0, 255)
DIM_X = 500
DIM_Y = 300
CENTER = (DIM_X/2,DIM_Y/2)

class Game(object):
    def __init__(self):
        super().__init__()
        self.background_colour = (255,255,255)
        self.dim = (DIM_X, DIM_Y)
        self.running = False
        self.elapsed = 0
        self.old_elapsed = 0
        self.init()
        self.num_steps = 8
        
        
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.dim)
        pygame.display.set_caption('Tutorial 1')
        self.screen.fill(self.background_colour)
        pygame.display.flip()
        self.running = True
        return
    
    def run(self):
        self.start()
        while self.running:
            self.update()
            self.postUpdate()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
        pygame.quit()
        return
    
    def start(self):
        self.ball = Ball(self.screen, self.dim)
        self.player_paddle = Paddle(self.screen, self.dim)
        return
    
    def update(self):
        self.screen.fill(self.background_colour)
        return
    
    def postUpdate(self):
        self.elapsed = pygame.time.get_ticks()
        delta = self.elapsed - self.old_elapsed
        self.old_elapsed = self.elapsed
        
        for i in range(self.num_steps):
            self.player_paddle.update()
            self.ball.update()
        
        return
    
#__________________________________________#

def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)


if __name__ == '__main__':
    console = Game()
    console.run()
    