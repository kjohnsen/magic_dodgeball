import pygame
from pygame import Rect
from pygame.locals import MOUSEBUTTONDOWN
from attrs import define, field, Factory

from game import Game, Scene
from gameobj import GameObject, NeedsCleanup
from button import Button
from utils import relrect
from match import Match


# @define
class Menu(Scene):
    start: Button

    def init(self, *args, **kwargs):
        def on_start_click():
            self.game.change_scene(Match)

        self.start = Button(
            relrect(self.surf, 0.5, 0.5, 0.5, 0.2), "START", on_start_click
        )

    def draw_bg(self):
        self.surf.fill((31, 1, 52))
        self.start.draw(self.surf)
