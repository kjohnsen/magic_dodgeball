import pygame, sys
from pygame.locals import QUIT
from game import Game
from menu import Menu
from eventhandler import EventHandler
from gvars import SCREEN, FPS

pygame.init()
pygame.display.set_caption('Magic Dodgeball')
pygame.font.init()
game = Game(SCREEN, Menu)
clock = pygame.time.Clock()
while True:
    game.scene.draw()
    for event in pygame.event.get():
        EventHandler.handle(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.scene.update()
    pygame.display.update()
    clock.tick(FPS)
    