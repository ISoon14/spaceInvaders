import pygame
import sys
from pygame import font
from pygame.locals import *


class Level:
    def __init__(self, number):
        self.number = number


    def getNumber(self):
        return self.number

    def getImage(self):
        return pygame.image.load("pictures/level-up.png")
