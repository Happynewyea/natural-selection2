import numpy as np
import math
import pygame
from mutation import mutation

def new_gene_moth(mothLife):
    mts = []
    for i in range(50):
        mothes = pygame.Rect(np.random.randint(145, 746), np.random.randint(145, 746), 10, 10)
        moths_range = pygame.Rect(mothes.centerx, mothes.centery, np.random.randint(100, 161), np.random.randint(100, 161))
        
        mts.append(mothes)
        mts.append(moths_range)
        mts.append(120)
        mothLife.append(mts)

        mts = []    

def life():
    pass

def execute():
    pass

def new_gene_bat(batLife):
    firstbat = batLife.pop(0)
    secondbat = batLife.pop(0)

    batbase = []
    while (len(batLife) < 10):
        
        newbat = pygame.Rect(np.random.randint(420, 441), np.random.randint(420, 441), 40, 40)
        newbat_range = pygame.Rect(newbat.centerx, newbat.centery, mutation((firstbat[1][2] + secondbat[1][2]) / 2), mutation((firstbat[1][3] + secondbat[1][3]) / 2))

        batbase.append(newbat)
        batbase.append(newbat_range)
        batbase.append(1500)

        batLife.append(batbase)
        batbase = []
    print("dones")
    
