import pygame
from pygame.sprite import Sprite

from gvars import FPS, SCREEN


class MagicSource(Sprite):
    curr: int
    maximum: int
    c: int = 1

    def __init__(self, rect, maximum=100) -> None:
        super().__init__()
        self.rect = rect
        self.maximum = maximum
        self.curr = maximum

    def _calc_work(self, prev_v, req_v):
        return self.c * (prev_v[0] - req_v[0])**2 + (prev_v[1] - req_v[1])**2

    def can_update(self, prev_v, req_v):
        work = self._calc_work(prev_v, req_v)
        return work <= self.curr

    def try_update(self, prev_v, req_v):
        work = self._calc_work(prev_v, req_v)
        if work <= self.curr:
            self.curr -= work
            return req_v
        else:
            return prev_v

    def draw(self):
        pygame.draw.rect(SCREEN, 'black', self.rect)
        indicator = self.rect.copy()
        indicator.width = self.rect.width * self.curr / self.maximum
        pygame.draw.rect(SCREEN, 'yellow', indicator)


    def update(self):
        if self.curr < self.maximum:
            sec_to_fill = 3
            self.curr += self.maximum / (sec_to_fill * FPS)
            if self.curr > self.maximum:
                self.curr = self.maximum