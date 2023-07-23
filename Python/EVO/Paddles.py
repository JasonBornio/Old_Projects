import pygame
import numpy as np

class Paddle(object):
    def __init__(self, window, window_dim):
        super().__init__()
        self.size = 10
        self.position = (0,0)
        self.velocity = 0
        self.dim = window_dim
        self.window = window
        self.state = [True,True]
        self.speed = 25
        self.move_up = False
        self.move_down = False
        
    def update(self):
        self.check_collisions()
        self.update_position()
        self.draw()
        return
    
    def check_collisions(self):
        self.state = [False,False]
        
        if self.position[1] < 0:
            self.state[1] = True
            
        if self.position[1] + self.size*3 > self.dim[1]:
            self.state[0] = True
            
        return

    def update_position(self):
        self.velocity = 0
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_UP]:
            self.move_up = True
        else:
            self.move_up = False
            
        if pressed_keys[pygame.K_DOWN]:
            self.move_down = True
        else:
            self.move_down = False
                    
        if self.move_up and self.state[1] == False:
            self.velocity = -1
            #print("RYYY")
        elif self.move_down and self.state[0] == False:
            self.velocity = 1
            #print("eyyy")
                    
        self.position = np.add(self.position, (0, self.velocity * self.speed * 0.001))
        #print(self.position)
        return 
    
    def draw(self):
        pygame.draw.rect(self.window, (255,0,0), (self.position[0], self.position[1], self.size,self.size*3))
        return