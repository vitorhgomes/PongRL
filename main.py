import pygame
from pygame.locals import *
import os

import numpy as np

from Assets.classes.puck import Puck
from Assets.classes.score import Score

 
class Game:
    def __init__(self):
        self._running = True
        self.screen = None
        self.clock = None

        self.size = self.width, self.height = 640, 480
        self.center = np.array([self.width / 2, self.height / 2])
        self.fps = 60

        self.puck = Puck(self.center, self.size)
        self.score = Score()

 
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('PongRL')
        self._running = True
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join('Assets', 'sprites', 'background.png'))


 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.puck.move()
        pass

    def on_render(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.puck.surface, self.puck.position)
        pygame.display.update()
        pass
    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
 
        while(self._running):
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute()