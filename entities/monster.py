import pygame as py
import time
import sys

class Monster:
    def __init__(self, surface):
        self.monsterListObject = []
        self.surface = surface
        self.sleep = 5
        self.countMonter = 20
        self.displayAllMonster()


    def displayAllMonster(self):
        column = 0
        line = 0
        for i in range(0, self.countMonter):
            if i % 9 == 0:
                column = column + 1
                line = 0
            else:
                line = i % 5
            self.displayMonster(line, column)

    def displayMonster(self, line, column):
        line = 60 + 60*line
        column = 50 * column
        image = py.image.load(r'pictures/monster.png')
        image = py.transform.scale(image, (40, 40))
        self.monsterListObject.append({'obj' : image, 'line' : line, 'column' : column})
        self.surface.blit(image, (line, column))
        self.moveMonster(image)

    def moveMonster(self, obj):
        perso = obj.convert_alpha()
        position_perso = perso.get_rect()
        hero_pos = position_perso.move(5, 1)
        self.surface.blit(obj, hero_pos)
        py.display.update()

