import pygame
import sys
from pygame.locals import *


class window:
    def init(self):
        self.start()

    def start(self):
        pygame.init()
        maSurface = pygame.display.set_mode((500, 300))
        pygame.display.set_caption('Space invader')
        inProgress = True
        while inProgress:
            for event in pygame.event.get():
                if event.type == QUIT:
                    inProgress = False
            pygame.display.update()
        pygame.quit()

    def button(self):
        print('a')