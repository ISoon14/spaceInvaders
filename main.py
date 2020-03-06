import pygame
from entities.window import window

obj = window()
obj.init()

# Liste de tout les sprites du jeux ( pour avoir un ensemble, utile pour le coté joueur en code)
all_sprites_list = pygame.sprite.Group()

# Liste des block (max appel là comme tu le sent juste un réfractoring fonctionnera avec moi)
block_list = pygame.sprite.Group()

# Liste de chaque balle tiré
bullet_list = pygame.sprite.Group()


# ICI ON INSTANCIE LES BLOCKS (chronologiquement pour que le code ne fasse pas d'erreur)

# On instancie le héro
hero = Hero()
all_sprites_list.add(hero)

# La condition d'arrêt du jeu
done = False

# Pour faire l'actualisation du jeu
clock = pygame.time.Clock()

score = 0
hero.rect.y = 370

while not done:
    # --- Gestion des évènement du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Tire une balle si on clique
            bullet = Bullet()
            # On met la balle là ou est le joueur (le plus 24 c'est pour qu'il soit au centre de l'image)
            bullet.rect.x = hero.rect.x +24
            bullet.rect.y = hero.rect.y
            # On l'ajoute dans le groupe
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)


    # Permet d'actualiser tout les objet (monstre, héros, balle et + si affinité), ça appel la methode update de chaque obj
    all_sprites_list.update()

    # Les intéractions et actions de chaque balles
    for bullet in bullet_list:

        # Vérifie si on se cogne contre un monstre, le non de l'objet + le groupe qu'il cogne (se delete si il se croise)
        # et on le met dans la liste des block touché
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # Pour chaque block touché on augmente le score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        # Enlève la ball quand elle est trop haute sur l'écran à vous de voir quel hauteur précisement
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    # Fait un écran blanc (j'ai fait ça pour mes testes)
    screen.fill(white)

    # affiche tout les sprites
    all_sprites_list.draw(screen)

    # Met à jour ce qu'on dessine
    pygame.display.flip()


    clock.tick(20)
