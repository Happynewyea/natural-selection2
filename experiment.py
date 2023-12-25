from brain import detect, detect_bat, movement_bat, movement_moth
from position import distance
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


mts = []
a = 300
for i in range(30):
    mothes = pygame.Rect(np.random.randint(WIDTH / 2 - a, WIDTH / 2 + a + 1), np.random.randint(HEIGHT / 2 - a, HEIGHT / 2 + a + 1), 10, 10)
    moths_range = pygame.Rect(mothes.centerx, mothes.centery, np.random.randint(20, 61), np.random.randint(20, 61))

    mothLife.append(mothes)
    

bts = []
for i in range(10):
    bates = pygame.Rect(np.random.randint(440, 461), np.random.randint(440, 461), 40, 40)
    bats_range = pygame.Rect(bates.centerx, bates.centery, np.random.randint(120, 201), np.random.randint(120, 201))

    bts.append(bates)
    bts.append(bats_range)
    batLife.append(bts)

    bts = []
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for moths in mothLife:
        for bats in batLife:
            if distance(moths, bats[0]) < 20:
                mothLife.remove(moths)
                print(f"Killed. {len(mothLife)} left")
                break

        movement_moth(moths)
        if moths.left <= 0: moths.left = 0
        if moths.right >= WIDTH: moths.right = WIDTH
        if moths.top <= 0: moths.top = 0
        if moths.bottom >= HEIGHT: moths.bottom = HEIGHT
        
        
    for bats in batLife:
        movement_bat(bats)
        if bats[0].left <= 0 + 150: bats[0].left = 0 + 150
        if bats[0].right >= WIDTH - 150: bats[0].right = WIDTH - 150
        if bats[0].top <= 0 + 150: bats[0].top = 0 + 150
        if bats[0].bottom >= HEIGHT - 150: bats[0].bottom = HEIGHT - 150
        

    screen.fill(WHITE)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100))


    for bats in batLife:
        detect_bat(bats, mothLife)
        pygame.draw.circle(screen, (0, 255, 0), bats[1].center, bats[1][3]/2)
        
    for bats in batLife:
        pygame.draw.circle(screen, (255, 0, 0), bats[0].center, 20)
        

    for moths in mothLife:
        detect(moths, batLife, screen)
        

    pygame.display.flip()

    
    clock.tick(30)