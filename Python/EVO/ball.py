import pygame
import numpy as np

class Ball(object):
    def __init__(self, window, window_dim):
        super().__init__()
        self.size = 10
        self.position = (10,50)
        self.velocity = [1,1]
        self.state = ['right','down']
        self.dim = window_dim
        self.window = window
        self.speed = 10
        
    def update(self):
        self.check_collisions()
        self.update_position()
        self.draw()
        return
    
    def check_collisions(self):
        if self.position[0] < 0:
            self.state[0] = 'right'
            
        if self.position[0] + self.size > self.dim[0]:
            self.state[0] = 'left'
            
        if self.position[1] < 0:
            self.state[1] = 'down'
            
        if self.position[1] + self.size > self.dim[1]:
            self.state[1] = 'up'
        return

    def update_position(self):
        if self.state[0] == 'right':
            self.velocity[0] = 1
        else:
            self.velocity[0] = -1
            
        if self.state[1] == 'down':
            self.velocity[1] = 1
        else:
            self.velocity[1] = -1
            
        self.position = np.add(self.position, (self.velocity[0] * self.speed * 0.001, self.velocity[1] * self.speed * 0.001))
        #print(self.position)
        return 
    
    def draw(self):
        pygame.draw.rect(self.window, (255,0,0), (self.position[0], self.position[1], self.size,self.size))
        return