# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:53:18 2023

@author: jugwu
"""
import numpy as np

class Entity(object):
    def __init__(self, shapes):
        super().__init__()
        self.radius = 5
        self.colour = (255,0,0)
        self.position_old = (0,0)
        self.position_current = (0,0)
        self.velocity = (0,0)
        self.acceleration = (0,0)
        self.ID = None
        self.init(shapes)
        
        
    def init(self, shapes):
        color = self.colour
        rad = self.radius
        pos = (self.position_current[0] - rad/2, self.position_current[1] - rad/2)
        shapes.append([pos, color, rad])
        self.ID = len(shapes) - 1
        return
    
    
    def updatePosition(self, dt):
        x = self.position_current[0] - self.position_old[0]
        y = self.position_current[1] - self.position_old[1]
        self.velocity = (x,y)
        self.position_old = self.position_current
        x = self.position_current[0] + self.velocity[0] + self.acceleration[0] * dt * dt
        y = self.position_current[1] + self.velocity[1] + self.acceleration[1] * dt * dt
        self.position_current = (x,y)
        self.acceleration = (0,0)
        return
    
    def accelerate(self, acc):
        self.acceleration = np.add(self.acceleration, acc)
        #print(self.acceleration)
        return
