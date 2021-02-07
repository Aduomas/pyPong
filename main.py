import pygame
from ball import Ballzzzz
from paddle import *
import entity
import pygame_menu


#screen
width = 800
height = 800

#game variables
entity.entityList.extend([Paddle(15, 400, 16, 125),
    Enemy(784, 0, 16, height),
    Enemy(0, 0, width, 0),
    Enemy(0, height, width, 0),
    Ballzzzz(width/2,  height/2)])

#PYGAME
pygame.init()

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

font = pygame.font.SysFont(None, 24)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((240, 248, 255))

    entity.update()


    # MENU
    #menu.mainloop(display)

    pygame.display.update()