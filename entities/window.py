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
        yellow = (255, 231, 9)
        blue = (71, 63, 132)
        highlight = (56, 112, 127)
        pygame.init()
        self.button("Jouer !", 75, 350, 150, 50, blue, highlight, self.exitGame)
        self.button("Score", 275, 350, 150, 50, yellow, highlight, self.startGame)
        pygame.display.flip()

    def exitGame(self):
        print("aaaz")

    def startGame(self):
        print("eer")

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        black = (0, 0, 0)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.frame, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.frame, ic, (x, y, w, h))

        myfont = pygame.font.SysFont("pictures/retroGaming.ttf", 35)
        letter = myfont.render(msg, 0, black)
        self.frame.blit(letter, ((x + (w / 2)), (y + (h / 2))))

    def getObject(self):
        print("a")
        return self.frame