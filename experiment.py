from brain import detect, movement_bat, movement_moth
import numpy as np
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 900
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nature")

clock = pygame.time.Clock()


mothLife = []
batLife = []


for i in range(10):
    moths = pygame.Rect(np.random.randint(100, 201), np.random.randint(100, 201), 10, 10)
    mothLife.append(moths)

bts = []
for i in range(10):
    bats = pygame.Rect(np.random.randint(250, 301), np.random.randint(400, 601), 40, 40)
    bats_range = pygame.Rect(bats.centerx, bats.centery, 160, 160)

    bts.append(bats)
    bts.append(bats_range)
    batLife.append(bts)

    bts = []
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for moths in mothLife:
        movement_moth(moths)
        if moths.left <= 0: moths.left = 0
        if moths.right >= WIDTH: moths.right = WIDTH
        if moths.top <= 0: moths.top = 0
        if moths.bottom >= HEIGHT: moths.bottom = HEIGHT
        
    for bats in batLife:
        movement_bat(bats)
        if bats[0].left <= 0: bats[0].left = 0
        if bats[0].right >= WIDTH: bats[0].right = WIDTH
        if bats[0].top <= 0: bats[0].top = 0
        if bats[0].bottom >= HEIGHT: bats[0].bottom = HEIGHT

    screen.fill(WHITE)

    for bats in batLife:
        pygame.draw.circle(screen, (0, 255, 0), bats[1].center, 80)

    for bats in batLife:
        pygame.draw.circle(screen, RED, bats[0].center, 20)
        

    for moths in mothLife:
        detect(moths, batLife, screen)
        

    pygame.display.flip()

    
    clock.tick(30)