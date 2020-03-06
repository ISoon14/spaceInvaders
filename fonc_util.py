import pygame
from entities.sqllite import Sqllite

# param = textBtn, posX, psoY, width, height, color, color hoover, function called
def button(screen, msg, x, y, w, h, ic, ac, action=None, action2=None):
    black = (0, 0, 0)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None and action2 != None:
            action()
            action2()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    myfont = pygame.font.SysFont("pictures/retroGaming.ttf", 35)
    letter = myfont.render(msg, 0, black)
    screen.blit(letter, ((x + (w / 3.5)), (y + (h / 3.5))))

def game_over(score):
    # Set the height and width of the screen
    pygame.init()

    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])
    font = pygame.font.Font(None, 32)
    blue = (71, 63, 132)
    highlight = (56, 112, 127)
    letter = font.render("Partie terminé, il est temps d'enregistrer votre score !", 0, (0, 0, 0))
    score_text = font.render("Votre score : " + str(score), 0, (0, 0, 0))
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    nomjoueur = ""
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        nomjoueur = text
                        text = ''

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        nomjoueur = text
                    else:
                        text += event.unicode
                        nomjoueur = text

        screen.fill((255, 255, 255))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(score_text, (input_box.x + 250, input_box.y + 5))
        screen.blit(letter, (50, 10))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        sqllite = Sqllite()
        button(screen, "Enregistrer", 300, 175, 250, 50, blue, highlight, sqllite.insert_data(nomjoueur, score))
        classement = sqllite.get_classement()
        for score_classement in classement:
            print(score_classement)
        pygame.display.flip()
        clock.tick(30)

