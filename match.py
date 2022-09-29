import pygame
from pygame.locals import MOUSEBUTTONDOWN

from scene import Scene
from gvars import DARKPURPLE
from utils import relrect
from eventhandler import EventHandler
from player import Player

class Match(Scene):
    def init(self, pleft, pright, *args, **kwargs):
        self.midline = relrect(self.surf, .5, .5, .01, 1)
        self.pleft = pleft('left')
        self.pright = pright('right')
        self.things.extend(self.pleft)
        self.things.extend(self.pright)
        
    def draw_bg(self):
        self.surf.fill(DARKPURPLE)
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
        for (p1, p2) in [(self.pleft, self.pright), (self.pright, self.pleft)]:
            icoll = p1.rect.collidelist(p2.active_balls)
            if icoll != -1:
                p1.hit()
                p2.active_balls[icoll].active = False
                if p1.health.curr <= 0:
                    self.game.change_scene('End', p2)

        