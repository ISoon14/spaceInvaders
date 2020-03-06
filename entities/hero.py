import pygame

class Hero(pygame.sprite.Sprite):
    """ La class du héro. """

    def __init__(self):
        """ Nous permet d'instancier l'image qui est sur le joueur. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load("pictures/hero.png"), (50, 50))
        self.rect = self.image.get_rect()


    def update(self):
        """ Met à jour la position du joueur. """
        pos = pygame.mouse.get_pos()

        # on défini la position x du joueur par rapport à la position récupéré plus haut
        self.rect.x = pos[0]
