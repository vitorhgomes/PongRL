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
        self.position = position - (self.size / 2)

    def render(self, screen):
        screen.blit(self.surface, self.position)
    
    def move(self):
        left_position = self.position[0]
        right_position = self.position[0] + self.rectangle.right
        top_position = self.position[1]
        bottom_position = self.position[1] + self.rectangle.bottom

        if left_position <= self.left_limit or right_position >= self.right_limit:
            self.speed *= np.array((-1, 1))

        if top_position <= self.top_limit or bottom_position >= self.bottom_limit:
            self.speed *= np.array((1, -1))
        
        self.position += self.speed