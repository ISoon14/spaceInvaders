import pygame, sys
from entities.monster import Monster
from entities.window import window
from entities.hero import Hero
from entities.balle import Bullet
from entities.level import Level
import time

pygame.init()
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Liste de tout les sprites du jeux ( pour avoir un ensemble, utile pour le coté joueur en code)
all_sprites_list = pygame.sprite.Group()

# Liste des block (max appel là comme tu le sent juste un réfractoring fonctionnera avec moi)
monsterList = pygame.sprite.Group()

# Liste de chaque balle tiré
bullet_list = pygame.sprite.Group()

NbMonster = 25

# ICI ON INSTANCIE LES BLOCKS (chronologiquement pour que le code ne fasse pas d'erreur)

# On instancie le héro
hero = Hero()
all_sprites_list.add(hero)
Monster.containers = monsterList
imageLevel = ""

myfont = pygame.font.SysFont("Arial", 15)
title = myfont.render("Appuyez sur espace pour commencer",0, (0, 0, 0))

def displayMonster(nb, speed):
    column = 0
    line = 0
    for i in range(0, nb):
        if i % 9 == 0:
            column = column + 1
            line = 0
        else:
            line = i % 5

        monsterObj = Monster(screen, line, column)
        monsterObj.setSpeed(speed)
        monsterList.add(monsterObj)
        all_sprites_list.add(monsterObj)


# La condition d'arrêt du jeu
done = False

# Pour faire l'actualisation du jeu
clock = pygame.time.Clock()

lastShoot = 0
score = 0
hero.rect.y = 370
xTouch = 0
lastInsert = time.time()
timeRespawn = 15
speedMonster = 0
levelNumber = 1
lastDisplayImage = 0



while not done:
    # --- Gestion des évènement du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if time.time() - lastShoot > 0.8:
                # Tire une balle si on clique
                bullet = Bullet()
                # On met la balle là ou est le joueur (le plus 24 c'est pour qu'il soit au centre de l'image)
                bullet.rect.x = hero.rect.x + 24
                bullet.rect.y = hero.rect.y
                # On l'ajoute dans le groupe
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                lastShoot = time.time()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               if speedMonster == 0:
                   speedMonster = 5
                   displayMonster(NbMonster, speedMonster)
                   screen.blit(title, (-50, -50))


    # Permet d'actualiser tous les objets (monstre, héros, balle et + si affinité), ça appel la methode update de chaque obj
    all_sprites_list.update()

    # Les intéractions et actions de chaque balles
    for bullet in bullet_list:

        # Vérifie si on se cogne contre un monstre, le non de l'objet + le groupe qu'il cogne (se delete si il se croise)
        # et on le met dans la liste des block touché
        block_hit_list = pygame.sprite.spritecollide(bullet, monsterList, True)

        # Pour chaque block touché on augmente le score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1

        # Enlève la ball quand elle est trop haute sur l'écran à vous de voir quel hauteur précisement
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    if (time.time() - lastInsert) > timeRespawn:
        speedMonster += 1
        levelNumber += 1
        displayMonster(8, speedMonster)
        lastInsert = time.time()
        if levelNumber % 2 == 0:
            level = Level(levelNumber)
            imageLevel = level.getImage()
            imageLevel = pygame.transform.scale(imageLevel, (100, 100))
            lastDisplayImage = time.time()

    # Fait un écran blanc (j'ai fait ça pour mes testes)
    screen.fill((255, 255, 255))

    # affiche tout les sprites
    all_sprites_list.draw(screen)
    myfont = pygame.font.SysFont("Arial", 15)
    letter = myfont.render("Score : "+str(score), 0, (0, 0, 0))
    screen.blit(letter, (10, 10))
    myfont = pygame.font.SysFont("Arial", 15)
    letter = myfont.render("Prochaine vague dans : " + str(int(timeRespawn - (time.time() - lastInsert))) + ' secondes',
                           0, (0, 0, 0))
    screen.blit(letter, (screen.get_rect().width - 250, 10))
    if speedMonster == 0:
        screen.blit(title, (200, 50))
    if imageLevel != "":
        screen.blit(imageLevel, (250, 50))
        if (time.time() - lastDisplayImage) > 5:
            screen.blit(imageLevel, (-100, -100))
            lastDisplayImage = 0
            imageLevel = ""
    # Met à jour ce qu'on dessine
    pygame.display.flip()
    clock.tick(40)