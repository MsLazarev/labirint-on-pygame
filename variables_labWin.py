import pygame
from Gamesprite import *
from player import *
from enemy import *
from bullet import *


pygame.init()
window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Лабиринт")
window.fill((138, 43, 226))
#image.load start
win = pygame.transform.scale(pygame.image.load("assets/win_cup.png"), (700, 900))
lose = pygame.transform.scale(pygame.image.load("assets/sad_monkey.jpg"), (900, 900))
our_sprite = pygame.transform.scale(pygame.image.load("assets/monkey.png"), (55, 75))
enemy_sprite_right = pygame.transform.scale(pygame.image.load("assets/sliz_right.png"), (50, 70))
enemy_sprite_left = pygame.transform.scale(pygame.image.load("assets/sliz_left.png"), (50, 70))
profenemy_sprite_right = pygame.transform.scale(pygame.image.load("assets/boss_enemy_right.png"), (50, 70))
profenemy_sprite_left = pygame.transform.scale(pygame.image.load("assets/boss_enemy_left.png"), (50, 70))
banana = pygame.transform.scale(pygame.image.load("assets/banana.png"), (75, 75))
wall_y = pygame.transform.scale(pygame.image.load("assets/wall_labirint_yy.jpg"), (40, 150))
wall_x = pygame.transform.scale(pygame.image.load("assets/wall_labirint_xx.jpg"), (150, 40))
special_wall_y = pygame.transform.scale(pygame.image.load("assets/wall_labirint_yy.jpg"), (40, 75))
granica_y = pygame.transform.scale(pygame.image.load("assets/wall_labirint_y.jpg"), (70, 900))
granica_x = pygame.transform.scale(pygame.image.load("assets/wall_labirint_x.jpg"), (900, 70))
bullet_r = pygame.transform.scale(pygame.image.load("assets/bullet_right.png"), (40, 10))
bullet_l = pygame.transform.scale(pygame.image.load("assets/bullet_left.png"), (40, 10))
funny_monkey = pygame.transform.scale(pygame.image.load("assets/fun_monkey.jpg"), (250, 250))
step1_right = pygame.transform.scale(pygame.image.load("assets/step_1_r.png"), (90, 90))
step2_right = pygame.transform.scale(pygame.image.load("assets/step_2_r.png"), (90, 90))
step3_right = pygame.transform.scale(pygame.image.load("assets/step_3_r.png"), (90, 90))
step4_right = pygame.transform.scale(pygame.image.load("assets/step_4_r.png"), (90, 90))
step5_right = pygame.transform.scale(pygame.image.load("assets/step_5_r.png"), (90, 90))
step1_left = pygame.transform.scale(pygame.image.load("assets/step_1_left.png"), (50, 60))
step2_left = pygame.transform.scale(pygame.image.load("assets/step_2_left.png"), (50, 60))
step3_left = pygame.transform.scale(pygame.image.load("assets/step_3_left.png"), (50, 60))
step4_left = pygame.transform.scale(pygame.image.load("assets/step_4_left.png"), (50, 60))
step5_left = pygame.transform.scale(pygame.image.load("assets/step_5_left.png"), (50, 60))
#image.load end

font = pygame.font.SysFont("Arial", 40)
win_label = font.render("YOU WIN!", True, (0, 0, 0))
whole_time = font.render("TIME:", True, (0, 0, 0))
record_label = font.render("BEST SCORE:", True, (0, 0, 0))
lose_label = font.render("YOU LOSE!", True, (255, 255, 255))
bullet_way = []
move_frames = pygame.sprite.Group()
last_key = []
step_iter = 0

#walls
barriers = pygame.sprite.Group()
#ЭКЗЕМПЛЯРЫ ПО ОСИ ОРДИНАТЫ(y)
barriers.add(GameSprite(wall_y, 80, 550))
barriers.add(GameSprite(wall_y, 80, 400))
barriers.add(GameSprite(wall_y, 80, 0))
barriers.add(GameSprite(wall_y, 210, 143))
barriers.add(GameSprite(wall_y, 340, 0))
barriers.add(GameSprite(wall_y, 590, -70))
barriers.add(GameSprite(wall_y, 340, 143))
barriers.add(GameSprite(wall_y, 340, 350))
barriers.add(GameSprite(wall_y, 340, 400))
barriers.add(GameSprite(wall_y, 340, 200))
barriers.add(GameSprite(wall_y, 230, 655))
barriers.add(GameSprite(wall_y, 340, 655))
barriers.add(GameSprite(wall_y, 470, 550))
barriers.add(GameSprite(wall_y, 590, 340))
barriers.add(GameSprite(wall_y, 590, 310))
barriers.add(GameSprite(wall_y, 740, 464))
barriers.add(GameSprite(wall_y, 740, 314))
barriers.add(GameSprite(wall_y, 740, 170))
barriers.add(GameSprite(wall_y, 740, 600))
barriers.add(GameSprite(special_wall_y, 460, 100))
barriers.add(GameSprite(special_wall_y, 740, 100))
#ЭКЗЕМПЛЯРЫ ПО ОСИ АБСЦИСС(x)
barriers.add(GameSprite(wall_x, 80, 253))
barriers.add(GameSprite(wall_x, 210, 110))
barriers.add(GameSprite(wall_x, 80, 390))
barriers.add(GameSprite(wall_x, 230, 520))
barriers.add(GameSprite(wall_x, 360, 425))
barriers.add(GameSprite(wall_x, 590, 575))
barriers.add(GameSprite(wall_x, 630, 170))
barriers.add(GameSprite(wall_x, 460, 170))
barriers.add(GameSprite(wall_x, 490, 170))
barriers.add(GameSprite(wall_x, 480, 290))
barriers.add(GameSprite(wall_x, 460, 290))

granicu = []
granicu.append(GameSprite(granica_y, -65, -30))
granicu.append(GameSprite(granica_y, 895, -30))
granicu.append(GameSprite(granica_x, 0, -65))
granicu.append(GameSprite(granica_x, 80, 695))
#walls end

#enemies start
enemies = pygame.sprite.Group()
prof_enemy = pygame.sprite.Group()
enemies.add(Enemy(enemy_sprite_right, 20, 300, 20, 280, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 150, 570, 150, 400, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 380, 340, 380, 535, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 380, 215, 380, 655, 4, 'right', 3))
prof_enemy.add(Enemy(profenemy_sprite_right, 510, 90, 510, 665, 5, 'right', 5))
#enemies end

bullets = pygame.sprite.Group()
bullets_enemy = pygame.sprite.Group()
hero = Player(our_sprite, 15, 800, 0, 0)
cup = GameSprite(win, 100, 0)
sad_monkey = GameSprite(lose, 0, 0)
funy_monkey = GameSprite(funny_monkey, 650, 400)
win_sprite = GameSprite(banana, 800, 600)