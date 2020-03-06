import pygame

class Bullet(pygame.sprite.Sprite):
    """ La classe de la balle . """

    def __init__(self):
        # on init grâce à la classe parente
        pygame.sprite.Sprite.__init__(self)

        # pui on set l'image dans mon cas, un polygonne
        self.image = pygame.Surface([4, 10])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        """ Pour déplacer la balle à chaque update. """
        self.rect.y -= 15

