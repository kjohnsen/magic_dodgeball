import pygame
from pygame import Rect
from pygame.locals import MOUSEBUTTONDOWN

from scene import Scene
from button import Button
from gvars import DARKPURPLE
from player import Player
from utils import relrect, relrect_side
from playerlist import players


# @define
class Menu(Scene):
    start: Button
    pleft: Player = None
    pright: Player = None

    def _player_buttons(self, side):
        draw_h = 1 / len(players)
        button_h = draw_h * 0.8
        out = []
        for i, ptype in enumerate(players):
            top = (i + 0.5) * draw_h
            rect = relrect_side(self.surf, side, 0.15, top, 0.25, button_h)
            def select(ptype):
                def select():
                    if side == 'left':
                        self.pleft = ptype
                    else:
                        self.pright = ptype
                return select
            b = Button(rect, ptype.__name__, select(ptype), 'gray')
            b.ptype = ptype
            out.append(b)
        return out

    def init(self, *args, **kwargs):
        def on_start_click():
            if self.pleft and self.pright:
                self.game.change_scene('Match', self.pleft, self.pright)

        self.start = Button(
            relrect(self.surf, 0.5, 0.5, 0.35, 0.2), "START", on_start_click, 'gray'
        )
        self.left_buttons = self._player_buttons('left')
        self.right_buttons = self._player_buttons('right')

    def draw_bg(self):
        self.surf.fill(DARKPURPLE)
        self.start.draw(self.surf)
        for buttons in [self.left_buttons, self.right_buttons]:
            for b in buttons:
                b.draw(self.surf)
    
    def update_self(self):
        for (ptype_attr, pbuttons) in [('pleft', self.left_buttons), ('pright', self.right_buttons)]:
            for b in pbuttons:
                if b.ptype == getattr(self, ptype_attr):
                    b.color = 'firebrick1'
                else:
                    b.color = 'gray'
        if self.pleft and self.pright:
            self.start.color = 'firebrick1'

