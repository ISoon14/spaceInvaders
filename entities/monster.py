import pygame as py
import time
import sys

class Monster(py.sprite.Sprite):
    def __init__(self, surface, line, column):
        py.sprite.Sprite.__init__(self, self.containers)
        self.monsterListObject = []
        self.surface = surface
        self.speed = 5
        line = 60 + 60 * line
        column = 50 * column
        self.image = py.image.load(r'pictures/monster.png')
        self.image = py.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = line
        self.rect.y = column
        self.direction = 'right'

    def update(self):
        if self.rect.x > 650 and self.direction != 'left':
            self.direction = 'left'
            self.rect.y += 15

        if self.rect.x == 0:
            self.direction = 'right'
            self.rect.y += 15

        if self.direction == 'right':
            self.rect.x = self.rect.x + self.speed
        else:
            self.rect.x = self.rect.x - self.speed

        if self.rect.y > self.surface.get_rect().height*0.85:
            self.speed = 0




