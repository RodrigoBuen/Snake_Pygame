import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.2)
music_thema = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

sound_colision = pygame.mixer.Sound('smw_jump.wav')

largura = 640
altura = 480

x_cobra , y_cobra = largura/2 - 20 , altura/2 - 20

velocity = 5
x_controler = velocity
y_controler = 0

death = False

x_maca, y_maca = randint(40, 580), randint(50, 430)

font_score = pygame.font.SysFont('arial', 30, True, False)
font_high_score = pygame.font.SysFont('arial', 15, True, True)

points = 0
high_score = 0

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Do Trollmon')
clock = pygame.time.Clock()

list_snake = []
len_init_snake = 5

def big_snake(list_snake):
    for XeY in list_snake:
        pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 20, 20))
        
def restart_game():
    global points, len_init_snake, x_cobra, y_cobra, list_snake, head_snake, x_maca, y_maca, death
    points = 0
    len_init_snake = 5
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    list_snake = []
    head_snake = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    death = False

while True:
    clock.tick(30)
    screen.fill((230,232,242))
    msg_score = f'Score: {points}'
    msg_final_score = font_score.render(msg_score, True, (0,0,0))
    msg_high_score = f'High Score: {high_score}'
    msg_final_high_score = font_high_score.render(msg_high_score, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_a and x_controler != velocity:
                x_controler = -velocity
                y_controler = 0
            if event.key == K_d and x_controler != -velocity:
                x_controler = velocity
                y_controler = 0
            if event.key == K_w and y_controler != velocity:
                y_controler = -velocity
                x_controler = 0
            if event.key == K_s and y_controler != -velocity:
                y_controler = velocity
                x_controler = 0
                
    x_cobra += x_controler
    y_cobra += y_controler
    
    cobra = pygame.draw.rect(screen, (0,255,0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(screen, (255,0,0), (x_maca, y_maca, 20, 20))
    
    if cobra.colliderect(maca):
        pygame.mixer.music.play()
        x_maca = randint(40, 580)
        y_maca = randint(50, 430)
        points += 1
        len_init_snake += 1
        sound_colision.play()
        
        if high_score <= points:
            high_score = points
            
        if points == 10:
            velocity += 2
        if points == 20:
            velocity += 2
        if points == 30:
            velocity += 2
        if points == 40:
            velocity += 2
        if points == 50:
            velocity += 3
        if points == 60:
            velocity += 3
        if points == 70:
            velocity += 3
        if points == 80:
            velocity += 4
        if points == 90:
            velocity += 4
        if points == 100:
            velocity += 5
        
    head_snake = []
    head_snake.append(x_cobra)
    head_snake.append(y_cobra)
    
    list_snake.append(head_snake)
    
    if x_cobra > largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura
    elif y_cobra < 0:
        y_cobra = altura
    elif y_cobra > altura:
        y_cobra = 0
        
    if len(list_snake) > len_init_snake:
        del list_snake[0]
        
    if list_snake.count(head_snake) > 1:
        font_game_over = pygame.font.SysFont('arial', 30, True, True)
        msg_game_over = 'Game Over, Aperte R para jogar novamente'
        game_over_final = font_game_over.render(msg_game_over, True, (0,0,0))
        center_over = game_over_final.get_rect()
        
        death = True
        while death:
            screen.fill((230,232,242))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
                    
            center_over.center = (largura//2, altura//2)
            screen.blit(game_over_final, center_over)
            pygame.display.update()
    big_snake(list_snake)
    
    screen.blit(msg_final_score, (480,10))
    screen.blit(msg_final_high_score, (480,50))
    pygame.display.update()