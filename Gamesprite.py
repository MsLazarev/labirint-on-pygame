import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))