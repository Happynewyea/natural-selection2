from math import sqrt
import pygame

def distance(self, other):
    return sqrt( (other.x - self.x) ** 2 + (other.y - self.y) ** 2 )
        
