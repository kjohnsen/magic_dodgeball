import pygame
from pygame import Rect
from pygame.sprite import Sprite
from attrs import define, field

from gvars import SCREEN
from magic import MagicSource


class Ball(Sprite):
    rect: Rect
    active: bool = False
    magic: MagicSource

    def __init__(self, rect) -> None:
        super().__init__()
        self.rect = rect
        self.v = [0, 0]

    def draw(self):
        if not self.active:
            return
        pygame.draw.circle(SCREEN, 'firebrick1', self.rect.center, self.rect.width//2)

    def start_traj(self, traj, magic):
        self.traj = traj
        self.magic = magic

    def update(self):
        if not self.active:
            return
        req_v = self.traj(self.rect.center, self.v)
        self.v = self.magic.try_update(self.v, req_v)
        self.rect = self.rect.move(self.v)

        if not self.rect.colliderect(SCREEN.get_rect()):
            self.active = False