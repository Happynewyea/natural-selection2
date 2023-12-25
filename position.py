from math import sqrt
from numpy import inf
import pygame

def distance(self, other):
    return sqrt( (other.centerx - self.centerx) ** 2 + (other.centery - self.centery) ** 2 )

def distance_x(self, other):
    if abs(other.centerx - self.centerx) > 0: return abs(other.centerx - self.centerx)
    else: return 1
        
def distance_y(self, other):
    if abs(other.centery - self.centery) > 0: return abs(other.centery - self.centery)
    else: return 1