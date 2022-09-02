from turtle import speed
import pygame
import os
import numpy as np

class Player:
    def __init__(self, screen_size, player = 1):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'bumper.png'))
        self.rectangle = self.surface.get_rect()
        self.size = self.rectangle.size
        self.speed = np.array([0,4])

        self.screen_size = screen_size

        if player == 1:
            self.position = np.array([0, screen_size[1] / 2 - self.size[1] / 2])
            self.up = pygame.K_w
            self.down = pygame.K_s
        
        if player == 2:
            self.position = np.array([(screen_size[0]-self.size[0]), screen_size[1] / 2 - self.size[1] / 2])
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN

    
    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.up] and self.position[1] > 0:
            self.position -= self.speed
        if keys_pressed[self.down] and (self.position[1]+self.rectangle.bottom) < self.screen_size[1]:
            self.position += self.speed