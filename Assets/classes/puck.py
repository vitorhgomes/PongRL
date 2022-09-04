from lib2to3 import pygram
import pygame, os
import numpy as np
from random import choice, randint

from Assets.classes.score import Score

class Puck:
    def __init__(self, position, limits):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'puck.png'))
        self.rectangle = self.surface.get_rect()
        self.angle = np.array([1,1])
        self.speed = np.array([randint(2,5),randint(2,5)])
        self.direction = np.array([choice((-1, 1)), choice((-1, 1))])
        self.speed *= self.direction
        self.left_limit, self.top_limit = 0, 0
        self.right_limit, self.bottom_limit = limits

        self.initial_position = position
        
        self.size = np.array([self.surface.get_width(), self.surface.get_height()])
        [self.rectangle.x, self.rectangle.y] = position - (self.size / 2)

        self.score = Score()

    def reset(self, left=True):
        self.rectangle.x = self.initial_position[0]
        self.rectangle.y = self.initial_position[1]
        self.speed = np.array([randint(2,5),randint(2,5)])
        self.direction = np.array([-1, choice((-1, 1))]) if left else np.array([1, choice((-1, 1))])
        self.speed *= self.direction


    
    def move(self):
        left_position = self.rectangle.left
        right_position = self.rectangle.right
        top_position = self.rectangle.top
        bottom_position = self.rectangle.bottom

        if left_position <= self.left_limit:
            self.score.right_scores()
            self.reset()
            print(self.score.left, self.score.right)

        if right_position >= self.right_limit:
            self.score.left_scores()
            self.reset(False)
            print(self.score.left, self.score.right)

        if top_position <= self.top_limit or bottom_position >= self.bottom_limit:
            self.speed *= np.array((1, -1))
        
        self.rectangle.x += self.speed[0]
        self.rectangle.y += self.speed[1]