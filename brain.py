from typing import overload
from position import distance, distance_x, distance_y
import numpy as np
import pygame

detect_distance_moth = 80
detect_distance_bat = 80


def movement_moth(moth):
    moth.move(np.random.randint(-5, 6), np.random.randint(-5, 6))

def movement_bat(bat):
    bat[0].move_ip(np.random.randint(-8, 9), np.random.randint(-8, 9))
    bat[1].center = bat[0].center






def detect(moth, batlife, screen):
    is_con = False  # is contact
    nearest_dist = 10000
    nearest_x = 0
    nearest_y = 0
    for bat in batlife:
        
        if distance(moth, bat[1]) < detect_distance_moth:
            if distance(moth, bat[1]) < nearest_dist:
                nearest_dist = distance(moth, bat[1])
                nearest_x = bat[1].centerx
                nearest_y = bat[1].centery

            #moth.centerx += (moth.centerx - nearest_x) / (0.5 * distance_x(moth, bat[1]))
            #moth.centery += (moth.centery - nearest_y) / (0.5 * distance_y(moth, bat[1]))
            is_con = True

        

    if is_con: pygame.draw.circle(screen, (255, 255, 0), moth.center, 5)
    else: pygame.draw.circle(screen, (0, 0, 255), moth.center, 5)
    


def detect_bat(bat, mothlife):
    nearest_dist = 10000
    nearest_x = 0
    nearest_y = 0
    for moth in mothlife:
        if distance(moth, bat[1]) < detect_distance_bat:
            if distance(moth, bat[1]) < nearest_dist:
                nearest_dist = distance(moth, bat[1])
                nearest_x = moth.centerx
                nearest_y = moth.centery
            bat[0].centerx += (nearest_x - bat[0].centerx) / (0.35 * distance_x(moth, bat[0]))
            bat[0].centery += (nearest_y - bat[0].centery) / (0.35 * distance_y(moth, bat[0]))


    bat[1].centerx = bat[0].centerx
    bat[1].centery = bat[0].centery