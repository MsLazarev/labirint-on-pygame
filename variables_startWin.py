import pygame
from Gamesprite import *

pygame.init()
start_window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Лабиринт")
start_window.fill((81, 11, 151))

font = pygame.font.SysFont("Arial", 40)
start_label = font.render("START", True, (61, 9, 112))
rect_coord = pygame.Rect(50, 100, 220, 120)
