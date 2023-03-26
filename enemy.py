import pygame
from Gamesprite import *
from bullet import *

class Enemy(GameSprite):
    def __init__(self, picture, x, y, x1, x2, speed, direction, health):
        super().__init__(picture, x, y)
        self.speed = speed
        self.x1 = x1
        self.x2 = x2
        self.direction = direction
        self.health = health
    def update(self):
        if self.rect.x <= self.x1:
            self.direction = "right"
        elif self.rect.x >= self.x2:
            self.direction = "left"

        if self.direction == "right":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.health <= 0:
            self.kill()
    def make_bullet(self, bullet_r, bullet_l, bullets_enemy):
        if self.direction == "right":
            new_bullet_r = Bullet(bullet_r, self.rect.right, self.rect.centery, 13, 'new_bullet_r')
            bullets_enemy.add(new_bullet_r)
        else:
            new_bullet_l = Bullet(bullet_l, self.rect.left, self.rect.centery, 13, "new_bullet_l")
            bullets_enemy.add(new_bullet_l)