from typing import overload
from position import distance
import numpy as np
import pygame


def movement_moth(moth):
    moth.move_ip(np.random.randint(-5, 6), np.random.randint(-5, 6))
def movement_bat(bat):
    bat[0].move_ip(np.random.randint(-8, 9), np.random.randint(-8, 9))
    bat[1].center = bat[0].center






def detect(moth, batlife, screen):
    pygame.draw.circle(screen, (0, 0, 255), moth.center, 5)
    for bat in batlife:
        if moth.colliderect(bat[1]):
            pygame.draw.circle(screen, (255, 255, 0), moth.center, 5)
            break
    
    