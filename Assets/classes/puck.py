from lib2to3 import pygram
import pygame, os
import numpy as np

class Puck:
    def __init__(self, position):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'puck.png'))
        self.angle = np.array([1,1])
        self.speed = np.array([2,2])
        
        self.size = np.array([self.surface.get_width(), self.surface.get_height()])
        self.position = position - (self.size / 2)

    def render(self, screen):
        screen.blit(self.surface, self.position)
    
    def move(self):
        self.position += self.speed