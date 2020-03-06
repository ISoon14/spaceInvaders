import pygame
import sys

from pygame import font
from pygame.locals import *


class window:
    def init(self):
        self.start()


    def start(self):
        pygame.init()
        # Chargement du logo et du fond
        background = pygame.image.load("pictures/bg.png")
        logo = pygame.image.load("pictures/logo.png")
        # chargement de la fenetre
        self.frame = pygame.display.set_mode((500, 700))
        pygame.display.set_caption('Space invaders')
        inProgress = True
        # boucle de jeu
        while inProgress:
            self.frame.blit(background, (0, 0))
            self.frame.blit(logo, (57.5, 30))

            self.createButtons()
            for event in pygame.event.get():
                if event.type == QUIT:
                    inProgress = False
            pygame.display.flip()
        pygame.quit()

    def createButtons(self):
        black = (0, 0, 0)
        yellow = (255, 231, 9)
        blue = (71, 63, 132)
        highlight = (56, 112, 127)
        pygame.init()
        mouse = pygame.mouse.get_pos()

        if 73 + 152 > mouse[0] > 73 and 350 + 52 > mouse[1] > 352:
            pygame.draw.rect(self.frame, highlight, (75, 350, 150, 50))
        else:
            pygame.draw.rect(self.frame, yellow, (75, 350, 150, 50))

        if 273 + 152 > mouse[0] > 273 and 350 + 52 > mouse[1] > 352:
            pygame.draw.rect(self.frame, highlight, (275, 350, 150, 50))
        else:
            pygame.draw.rect(self.frame, blue, (275, 350, 150, 50))

        textLaunch = pygame.font.Font("tahoma.ttf", 30).render("Jouer !", True, black)
        textLaunch.center = ((75 + (100 / 2)), (350 + (50 / 2)))
        self.frame.blit(textLaunch)
        pygame.display.flip()

    def getObject(self):
        return self.frame

    def text_objects(text, font):
        black = (0, 0, 0)
        textSurface = font.render("Jouer !", True, black)
        return textSurface, textSurface.get_rect()