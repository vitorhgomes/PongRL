from lib2to3 import pygram
import pygame, os
import numpy as np
from random import randrange

class Puck:
    def __init__(self, position, limits):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'puck.png'))
        self.rectangle = self.surface.get_rect()
        self.angle = np.array([1,1])
        self.speed = np.array([2,2])
        self.left_limit, self.top_limit = 0, 0
        self.right_limit, self.bottom_limit = limits
        
        self.size = np.array([self.surface.get_width(), self.surface.get_height()])
        [self.rectangle.x, self.rectangle.y] = position - (self.size / 2)
        # self.rectangle.y = position[1] - (self.size[1] / 2)

    
    def move(self):
        left_position = self.rectangle.left
        right_position = self.rectangle.right
        top_position = self.rectangle.top
        bottom_position = self.rectangle.bottom

        if left_position <= self.left_limit or right_position >= self.right_limit:
            self.speed *= np.array((-1, 1))

        if top_position <= self.top_limit or bottom_position >= self.bottom_limit:
            self.speed *= np.array((1, -1))
        
        self.rectangle.x += self.speed[0]
        self.rectangle.y += self.speed[1]