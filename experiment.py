from gene import new_gene_bat, new_gene_moth
from event import move, draw
import numpy as np
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 900
WHITE, RED, BLUE = (255, 255, 255), (255, 0, 0), (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nature")

clock = pygame.time.Clock()


mothLife, batLife = [], []


mts = []
for i in range(50):
    mothes = pygame.Rect(np.random.randint(145, 746), np.random.randint(145, 746), 10, 10)
    moths_range = pygame.Rect(mothes.centerx, mothes.centery, np.random.randint(100, 161), np.random.randint(100, 161))
    
    mts.append(mothes)
    mts.append(moths_range)
    mts.append(120)
    mothLife.append(mts)

    mts = []    

summed = 0
bts = []
for i in range(10):
    bates = pygame.Rect(np.random.randint(420, 441), np.random.randint(420, 441), 40, 40)
    bats_range = pygame.Rect(bates.centerx, bates.centery, np.random.randint(120, 181), np.random.randint(120, 181))

    bts.append(bates)
    bts.append(bats_range)
    bts.append(1500)
    batLife.append(bts)

    bts = []
    summed += batLife[i][1][2] / 2
print(summed / len(batLife))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    summed = 0
    if len(batLife) == 2:
        new_gene_bat(batLife)
        new_gene_moth(mothLife)
        for i in range(10):
            summed += batLife[i][1][2] / 2
        print(summed / len(batLife))

    
    move(mothLife, batLife, screen, WIDTH, HEIGHT)
    draw(mothLife, batLife, screen, WIDTH, HEIGHT, WHITE)
    
    
    clock.tick(120)