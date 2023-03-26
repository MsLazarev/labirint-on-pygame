import pygame
import time
from variables_labWin import *
from variables_startWin import *
from counting_record import read_records
# Разработай свою игру в этом файле!

pygame.init()
start_time = time.time()
run = True
finish = False
first_win = True

chill = time.time()
while run:
    if first_win:
        window.fill((81, 11, 151))
        pygame.draw.rect(window, (255, 255, 255), rect_coord)
        window.blit(start_label, (110, 140))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if rect_coord.collidepoint(x, y):
                    first_win = False
        pygame.time.delay(40)
        pygame.display.update()
    else:
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
                    hero.fire(bullet_way, bullet_l, bullet_r, bullets)
                if e.key == pygame.K_LEFT:
                    bullet_way.append("left")
                    hero.fire(bullet_way, bullet_l, bullet_r, bullets)
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_w:
                    hero.y_speed = 0
                    hero.image = our_sprite
                if e.key == pygame.K_s:
                    hero.y_speed = 0
                    hero.image = our_sprite
                if e.key == pygame.K_a:
                    hero.x_speed = 0
                    hero.image = our_sprite
                if e.key == pygame.K_d:
                    hero.x_speed = 0
                    hero.image = our_sprite
        if finish == False:
            window.fill((138, 43, 226))
            hero.reset(window)
            win_sprite.reset(window)
            for i in range(4):
                granicu[i].reset(window)
            barriers.draw(window)
            bullets.draw(window)
            bullets_enemy.draw(window)
            enemies.draw(window)
            if time.time() - chill >= 1:
                chill = time.time()
                for i in prof_enemy:
                    i.make_bullet(bullet_r, bullet_l, bullets_enemy)
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
            hero.update(barriers, step1_right, step2_right, step3_right, step4_right, step5_right, step1_left, step2_left, step3_left, step4_left, step5_left, last_key)
            pygame.sprite.groupcollide(bullets, barriers, True, False)
            pygame.sprite.groupcollide(bullets_enemy, barriers, True, False)
            if pygame.sprite.collide_rect(hero, win_sprite):
                finish = True
                end_time = time.time()
                window.fill((255, 255, 255))
                min_element = read_records(end_time, start_time)
                cup.reset(window)
                funy_monkey.reset(window)
                window.blit(win_label, (370, 200))
                window.blit(whole_time, (20, 650))
                label_time = font.render(str(round(end_time - start_time, 2)), True, (0, 0, 0))
                window.blit(label_time, (120, 650))
                window.blit(record_label, (20, 580))
                record_time = font.render(str(round(min_element, 2)), True, (0, 0, 0))
                window.blit(record_time, (250, 580))
            for i in enemies:
                if pygame.sprite.collide_rect(hero, i):
                    finish = True
                    window.fill((0, 0, 0))
                    sad_monkey.reset(window)
                    window.blit(lose_label, (700, 600))
            if pygame.sprite.spritecollide(hero, prof_enemy, False) or pygame.sprite.spritecollide(hero, bullets_enemy, False):
                finish = True
                window.fill((0, 0, 0))
                sad_monkey.reset(window)
                window.blit(lose_label, (700, 600))

        pygame.time.delay(40)
        pygame.display.update()