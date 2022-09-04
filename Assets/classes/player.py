from turtle import speed
import pygame
import os
import numpy as np

class Player:
    def __init__(self, screen_size, player = 1):
        self.surface = pygame.image.load(os.path.join('Assets', 'sprites', 'bumper.png'))
        self.rectangle = self.surface.get_rect()
        self.size = self.rectangle.size
        self.speed = 4

        self.screen_size = screen_size

        if player == 1:
            self.rectangle.x = 0
            self.rectangle.y = screen_size[1] / 2 - self.size[1] / 2
            self.up = pygame.K_w
            self.down = pygame.K_s
        
        if player == 2:
            self.rectangle.x = screen_size[0]-self.size[0]
            self.rectangle.y = screen_size[1] / 2 - self.size[1] / 2
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN

    
    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.up] and self.rectangle.top > 0:
            self.rectangle.y -= self.speed

        if keys_pressed[self.down] and (self.rectangle.bottom) < self.screen_size[1]:
            self.rectangle.y += self.speed
