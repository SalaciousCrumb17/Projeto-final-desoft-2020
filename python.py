# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:04:03 2020

@author: lucas
"""

import pygame as pygame
import random
import time
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 640
HEIGHT = 400
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255,255,255)

class player(pygame.sprite.Sprite):
    def __init__(self,distancia):
        pygame.sprite.Sprite.__init__(self)
            

pygame.init()      
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(path.join(img_dir, 'back.jpg')).convert()
background_rect = background.get_rect()

        
        
        
        
        
        
        
        
        
        
    