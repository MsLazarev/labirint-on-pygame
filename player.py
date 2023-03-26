import pygame
from Gamesprite import *
from bullet import *

cnt = 0
class Player(GameSprite):
    def __init__(self, picture, x, y, x_speed, y_speed):
        super().__init__(picture, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self, barriers, step1_right, step2_right, step3_right, step4_right, step5_right, step1_left, step2_left, step3_left, step4_left, step5_left, last_key):
        global cnt
        self.rect.y += self.y_speed
        touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for t in touched:
                self.rect.bottom = min(self.rect.bottom, t.rect.top)
                self.y_speed = 0
                if self.x_speed > 0:
                    return 1
                elif self.x_speed < 0:
                    return 1
        elif self.y_speed < 0:
            for t in touched:
                self.rect.top = max(self.rect.top, t.rect.bottom)
                self.y_speed = 0
                if self.x_speed > 0:
                    return 1
                elif self.x_speed < 0:
                    return 1
        self.rect.x += self.x_speed
        touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            cnt += 1
            if cnt == 1:
                self.image = step1_right
            elif cnt == 2:
                self.image = step2_right
            elif cnt == 3:
                self.image = step3_right
            elif cnt == 4:
                self.image = step4_right
            elif cnt == 5:
                self.image = step5_right
            elif cnt >= 6:
                self.image = step1_right
                cnt = 0
            for t in touched:
                self.rect.right = min(self.rect.right, t.rect.left)
                self.x_speed = 0
                if self.y_speed > 0:
                    return 1
                elif self.y_speed < 0:
                    return 1
                
        elif self.x_speed < 0:
            cnt += 1
            if cnt == 1:
                self.image = step1_left
            elif cnt == 2:
                self.image = step2_left
            elif cnt == 3:
                self.image = step3_left
            elif cnt == 4:
                self.image = step4_left
            elif cnt == 5:
                self.image = step5_left
            elif cnt >= 6:
                self.image = step1_left
                cnt = 0
            for t in touched:
                self.rect.left = max(self.rect.left, t.rect.right)
                self.x_speed = 0
                if self.y_speed > 0:
                    return cnt
                elif self.y_speed < 0:
                    return cnt
    def fire(self, bullet_way, bullet_l, bullet_r, bullets):
        if bullet_way[-1] == "right":
            new_bullet_r = Bullet(bullet_r, self.rect.right, self.rect.centery, 13, 'new_bullet_r')
            bullets.add(new_bullet_r)
        else:
            new_bullet_l = Bullet(bullet_l, self.rect.left, self.rect.centery, 13, "new_bullet_l")
            bullets.add(new_bullet_l)