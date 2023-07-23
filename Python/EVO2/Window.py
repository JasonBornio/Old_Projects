# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:04:14 2023

@author: jugwu
"""

import pygame
import globalVars as globs
from entity import Entity
BLUE =      (  0,   0, 255)
DIM_X = 300
DIM_Y = 300
CENTER = (DIM_X/2,DIM_Y/2)

class Game(object):
    def __init__(self):
        super().__init__()
        self.background_colour = (255,255,255)
        self.dim = (DIM_X, DIM_Y)
        self.running = False
        self.physics = globs.global_physics
        self.elapsed = 0
        self.old_elapsed = 0
        self.init()
        
        
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
        ball = Entity(globs.shapes)
        globs.entities.append(ball)
        return
    
    def update(self):
        self.screen.fill(self.background_colour)
        self.handle_objects()
        return
    
    def postUpdate(self):
        self.elapsed = pygame.time.get_ticks()
        delta = self.elapsed - self.old_elapsed
        self.old_elapsed = self.elapsed
        self.physics.update(delta * 0.00001)
        return
    
#__________________________________________#

    def handle_objects(self):
        for shapes, objs in zip(globs.shapes, globs.entities):
            shapes[0] = objs.position_current
            #print(shapes[0])
            pygame.draw.circle(self.screen, shapes[1], shapes[0], shapes[2])
        return

def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)


if __name__ == '__main__':
    console = Game()
    console.run()
    