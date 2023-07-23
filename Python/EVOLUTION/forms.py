# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:00:06 2023

@author: Jugwu
"""

def ssj(creature):
    
    
    
    
    
    
    
    creature.atk = int(creature.atk * 2)
    creature.kiAtk = int(creature.kiAtk * 1.5)
    creature.health = int(creature.health * 5)
    creature.healthRegen = int(creature.healthRegen * 1.5)
    creature.defense = int(creature.defense * 2)
    creature.kiDefense = int(creature.kiDefense * 1.5)
    creature.kiCharge = int(creature.kiCharge * 1.5)
    creature.maxKi = int(creature.maxKi * 2)
    creature.kiRegen = int(creature.kiRegen * 1.5)
    creature.speed = int(creature.speed * 2)
    
    return