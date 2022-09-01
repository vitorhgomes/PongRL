import pygame

class Score():
    def __init__(self):
        self.left = 0
        self.right = 0
    
    def reset(self):
        self.left = 0
        self.right = 0
    
    def left_scores(self):
        self.left += 1
    
    def right_scores(self):
        self.right += 1