import pygame
from pygame.locals import MOUSEBUTTONDOWN

from game import Game, Scene
from utils import relrect
from eventhandler import EventHandler
from player import Player
from kyle import Kyle

class Match(Scene):
    def init(self, *args, **kwargs):
        self.midline = relrect(self.surf, .5, .5, .01, 1)
        self.pleft = Kyle('left')
        self.pright = Kyle('right')
        self.things.extend(self.pleft)
        self.things.extend(self.pright)
        
    def draw_bg(self):
        self.surf.fill((31, 1, 52))
        pygame.draw.rect(self.surf, 'white', self.midline)

    def update_self(self):
        active_ball_dict = {b: b.rect for b in [*self.pleft.active_balls, *self.pright.active_balls]}
        for b in active_ball_dict:
            collisions = b.rect.collidedictall(active_ball_dict)
            for (bcoll, _) in collisions:
                if b == bcoll:
                    continue
                b.active = False
                bcoll.active = False