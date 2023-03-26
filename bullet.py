import pygame
from Gamesprite import *

class Bullet(GameSprite):
    def __init__(self, picture, x, y, speed, name):
        super().__init__(picture, x, y)
        self.name = name
        self.speed = speed
    def update(self):
        if self.name == 'new_bullet_r':
            self.rect.x += self.speed
            if self.rect.x >= 820:
                self.kill()
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.kill()        