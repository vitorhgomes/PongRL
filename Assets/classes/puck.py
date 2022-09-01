from lib2to3 import pygram
import pygame, os
import numpy as np

class Puck:
    def __init__(self):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'puck.png'))
        self.angle = np.array([1,1])
        self.speed = np.array([2,2])
        self.position = np.array([0,0])
        self.size = np.array([self.surface.get_width(), self.surface.get_height()])

    def render(self, screen, center):
        screen.blit(self.surface, center - (self.size / 2))