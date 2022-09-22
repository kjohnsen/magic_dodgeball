import pygame
from pygame.locals import MOUSEBUTTONDOWN

from game import Game, Scene
from utils import relrect
from eventhandler import EventHandler
from player import Player

class Match(Scene):
    def init(self, *args, **kwargs):
        self.midline = relrect(self.surf, .5, .5, .01, 1)
        self.pleft = Player('left')
        self.pright = Player('right')
        self.groups.append()
        
    def draw_bg(self):
        self.surf.fill((31, 1, 52))
        pygame.draw.rect(self.surf, 'white', self.midline)