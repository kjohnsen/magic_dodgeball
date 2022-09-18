import pygame, sys
from pygame.locals import QUIT
from scenemgr import Game
from menu import Menu

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Magic Dodgeball')
game = Game(DISPLAYSURF, Menu)
while True:
    game.draw()
    for event in pygame.event.get():
        game.process_event(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.update()
    pygame.display.update()