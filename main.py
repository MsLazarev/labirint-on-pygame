import pygame
import time
# Разработай свою игру в этом файле!

pygame.init()
window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Лабиринт")
window.fill((138, 43, 226))
start_time = time.time()
run = True
finish = False
#ВЫЗОВ КАРТИНОК
win = pygame.transform.scale(pygame.image.load("win_cup.png"), (700, 900))
lose = pygame.transform.scale(pygame.image.load("sad_monkey.jpg"), (900, 900))
our_sprite = pygame.transform.scale(pygame.image.load("monkey.png"), (55, 75))
enemy_sprite_right = pygame.transform.scale(pygame.image.load("sliz_right.png"), (50, 70))
enemy_sprite_left = pygame.transform.scale(pygame.image.load("sliz_left.png"), (50, 70))
profenemy_sprite_right = pygame.transform.scale(pygame.image.load("boss_enemy_right.png"), (50, 70))
profenemy_sprite_left = pygame.transform.scale(pygame.image.load("boss_enemy_left.png"), (50, 70))
banana = pygame.transform.scale(pygame.image.load("banana.png"), (75, 75))
wall_y = pygame.transform.scale(pygame.image.load("wall_labirint_yy.jpg"), (40, 150))
wall_x = pygame.transform.scale(pygame.image.load("wall_labirint_xx.jpg"), (150, 40))
special_wall_y = pygame.transform.scale(pygame.image.load("wall_labirint_yy.jpg"), (40, 75))
granica_y = pygame.transform.scale(pygame.image.load("wall_labirint_y.jpg"), (70, 900))
granica_x = pygame.transform.scale(pygame.image.load("wall_labirint_x.jpg"), (900, 70))
bullet_r = pygame.transform.scale(pygame.image.load("bullet_right.png"), (40, 10))
bullet_l = pygame.transform.scale(pygame.image.load("bullet_left.png"), (40, 10))
funny_monkey = pygame.transform.scale(pygame.image.load("fun_monkey.jpg"), (250, 250))
step1_right = pygame.transform.scale(pygame.image.load("step_1_r.png"), (90, 90))
step2_right = pygame.transform.scale(pygame.image.load("step_2_r.png"), (90, 90))
step3_right = pygame.transform.scale(pygame.image.load("step_3_r.png"), (90, 90))
step4_right = pygame.transform.scale(pygame.image.load("step_4_r.png"), (90, 90))
step5_right = pygame.transform.scale(pygame.image.load("step_5_r.png"), (90, 90))
step1_left = pygame.transform.scale(pygame.image.load("step_1_left.png"), (50, 60))
step2_left = pygame.transform.scale(pygame.image.load("step_2_left.png"), (50, 60))
step3_left = pygame.transform.scale(pygame.image.load("step_3_left.png"), (50, 60))
step4_left = pygame.transform.scale(pygame.image.load("step_4_left.png"), (50, 60))
step5_left = pygame.transform.scale(pygame.image.load("step_5_left.png"), (50, 60))
#КОНЕЦ ВЫЗОВА КАРТИНОК
font = pygame.font.SysFont("Arial", 40)
win_label = font.render("YOU WIN!", True, (0, 0, 0))
whole_time = font.render("TIME:", True, (0, 0, 0))
record_label = font.render("BEST SCORE:", True, (0, 0, 0))
lose_label = font.render("YOU LOSE!", True, (255, 255, 255))
bullet_way = []
move_frames = pygame.sprite.Group()
last_key = []
cnt = 0
step_iter = 0
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, picture, x, y, x_speed, y_speed):
        super().__init__(picture, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self, last_key):
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
                    return 1
                elif self.y_speed < 0:
                    return 1
    def fire(self):
        if bullet_way[-1] == "right":
            new_bullet_r = Bullet(bullet_r, self.rect.right, self.rect.centery, 13, 'new_bullet_r')
            bullets.add(new_bullet_r)
        else:
            new_bullet_l = Bullet(bullet_l, self.rect.left, self.rect.centery, 13, "new_bullet_l")
            bullets.add(new_bullet_l)
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
            print("здесь")
    def make_bullet(self):
        if self.direction == "right":
            new_bullet_r = Bullet(bullet_r, self.rect.right, self.rect.centery, 13, 'new_bullet_r')
            bullets_enemy.add(new_bullet_r)
        else:
            new_bullet_l = Bullet(bullet_l, self.rect.left, self.rect.centery, 13, "new_bullet_l")
            bullets_enemy.add(new_bullet_l)


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
        
        
            
bullets = pygame.sprite.Group()
bullets_enemy = pygame.sprite.Group()
hero = Player(our_sprite, 15, 800, 0, 0)
cup = GameSprite(win, 100, 0)
sad_monkey = GameSprite(lose, 0, 0)
funy_monkey = GameSprite(funny_monkey, 650, 400)
win_sprite = GameSprite(banana, 800, 600)
#speed_hero = Player(0, 0)
#СОЗДАНИЕ ВРАГОВ
enemies = pygame.sprite.Group()
prof_enemy = pygame.sprite.Group()
enemies.add(Enemy(enemy_sprite_right, 20, 300, 20, 280, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 150, 570, 150, 400, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 380, 340, 380, 535, 4, 'right', 3))
enemies.add(Enemy(enemy_sprite_right, 380, 215, 380, 655, 4, 'right', 3))

prof_enemy.add(Enemy(profenemy_sprite_right, 510, 90, 510, 665, 5, 'right', 5))

#СОЗДАНИЕ ЭКЗЕМПЛЯРОВ ДЛЯ ВСЕХ СТЕН ЛАБИРИНТА И ПРЯМОЕ ДОБАВЛЕНИЕ ИХ В СПЕЦ ГРУППУ ДЛЯ НИХ
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


#СОЗДАНИЕ 4 ЭКЗЕМПЛЯРОВ В КАЧЕСТВЕ ПОГРАНИЧНЫХ СТЕНОК
granicu = []
granicu.append(GameSprite(granica_y, -65, -30))
granicu.append(GameSprite(granica_y, 895, -30))
granicu.append(GameSprite(granica_x, 0, -65))
granicu.append(GameSprite(granica_x, 80, 695))

chill = time.time()
while run:
    step_iter += 1
    #ПРОВЕРКА НЕ ЗАШЕЛ ЛИ ИГРОК ЗА ГРАИНЦЫ ОКНА
    if hero.rect.y > 615:
        hero.y_speed = 0
        hero.rect.bottom = 695
    if hero.rect.y < 0:
        hero.y_speed = 0
        hero.rect.top = 0
    if hero.rect.x < 0:
        hero.x_speed = 0
        hero.rect.left = 0
    if hero.rect.x > 825:
        hero.x_speed = 0
        hero.rect.right = 885
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                hero.y_speed = -5
            if e.key == pygame.K_s:
                hero.y_speed = 5
            if e.key == pygame.K_a:
                hero.x_speed = -5
            if e.key == pygame.K_d:
                hero.x_speed = 5
            if e.key == pygame.K_RIGHT:
                bullet_way.append('right')
                hero.fire()
            if e.key == pygame.K_LEFT:
                bullet_way.append("left")
                hero.fire()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                hero.y_speed = 0
                cnt = 0
                hero.image = our_sprite
            if e.key == pygame.K_s:
                hero.y_speed = 0
                cnt = 0
                hero.image = our_sprite
            if e.key == pygame.K_a:
                hero.x_speed = 0
                cnt = 0
                hero.image = our_sprite
            if e.key == pygame.K_d:
                hero.x_speed = 0
                cnt = 0
                hero.image = our_sprite
    if finish == False:
        window.fill((138, 43, 226))
        hero.reset()
        win_sprite.reset()
        for i in range(4):
            granicu[i].reset()
        barriers.draw(window)
        bullets.draw(window)
        bullets_enemy.draw(window)
        enemies.draw(window)
        if time.time() - chill >= 1:
            chill = time.time()
            for i in prof_enemy:
                i.make_bullet()
        for i in enemies:
            if i.direction == "right":
                i.image = enemy_sprite_right
            else:
                i.image = enemy_sprite_left
        for i in prof_enemy:
            if i.direction == "right":
                i.image = profenemy_sprite_right
            else:
                i.image = profenemy_sprite_left
        for i in enemies:
            if pygame.sprite.groupcollide(bullets, enemies, True, False):
                i.health -= 1
        for i in prof_enemy:
            if pygame.sprite.groupcollide(bullets, prof_enemy, True, False):
                i.health -= 1
        prof_enemy.draw(window)
        bullets.update()
        bullets_enemy.update()
        enemies.update()
        prof_enemy.update()
        hero.update(last_key)
        pygame.sprite.groupcollide(bullets, barriers, True, False)
        pygame.sprite.groupcollide(bullets_enemy, barriers, True, False)
        if pygame.sprite.collide_rect(hero, win_sprite):
            finish = True
            end_time = time.time()
            window.fill((255, 255, 255))
            f = open("records.txt", "r+")
            wrong_records = f.readlines()#ВМЕСТЕ С \n
            right_records = []#БЕЗ \n
            f.write(f"{end_time - start_time}\n")
            for i in range(len(wrong_records)):
                symbol = wrong_records[i][:-1]
                symbol = float(symbol)
                symbol = int(symbol)
                right_records.append(symbol)
            min_element = 1000000000000000000000000000000000000
            for i in range(len(right_records)):
                if end_time - start_time < min_element:
                    min_element = end_time - start_time    
                elif right_records[i] < min_element:
                    min_element = right_records[i]
                else:
                    pass
            cup.reset()
            funy_monkey.reset()
            window.blit(win_label, (370, 200))
            window.blit(whole_time, (20, 580))
            label_time = font.render(str(round(end_time - start_time, 2)), True, (0, 0, 0))
            window.blit(label_time, (120, 580))
            window.blit(record_label, (20, 650))
            record_time = font.render(str(round(min_element, 1)), True, (0, 0, 0))
            window.blit(record_time, (250, 650))
        for i in enemies:
            if pygame.sprite.collide_rect(hero, i):
                finish = True
                window.fill((0, 0, 0))
                sad_monkey.reset()
                window.blit(lose_label, (700, 600))
        if pygame.sprite.spritecollide(hero, prof_enemy, False) or pygame.sprite.spritecollide(hero, bullets_enemy, False):
            finish = True
            window.fill((0, 0, 0))
            sad_monkey.reset()
            window.blit(lose_label, (700, 600))

    pygame.time.delay(40)
    pygame.display.update()