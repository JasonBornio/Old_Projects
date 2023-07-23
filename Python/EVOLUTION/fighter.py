# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:40:27 2023

@author: Jugwu
"""
import forms

class creature():
    def __init__(self):
        self.health = 10
        self.atk = 10
        self.kiAtk = 5
        self.defense = 10
        self.kiDefense = 5
        self.kiCharge = 1
        self.maxKi = 10
        self.healthRegen = 1
        self.kiRegen = 1
        self.speed = 10
        return
    
    def attack(self, target):
        return
    
    def kiAttack(self, target):
        return
    
    def heal(self, ):
        return
    
    def battlePower(self):
        pl = 0
        pl = (self.health * self.healthRegen) 
        pl+= (self.atk + self.kiAtk + self.defense + self.kiDefense)
        pl+= (self.speed) 
        pl+= (self.kiCharge * self.maxKi)
        return pl
    
    def transform():
        return