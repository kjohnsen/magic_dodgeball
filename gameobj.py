import pygame
from attrs import define, field, Factory


# @define
class GameObject:
    """mixin for standard things: draw, update, process event on self and recursively on GameObject children"""
    surf: pygame.Surface = None

    @property
    def children(self):
        for c in vars(self):
            if type(c) == GameObject:
                yield c

    def draw(self):
        self.draw_self()
        for c in self.children:
            c.draw()

    def draw_self(self):
        pass

    def update(self):
        self.update_self()
        for c in self.children:
            c.update()

    def update_self(self):
        pass

    def register_event_handler(event_type, function):
        pass


class NeedsCleanup:
    @property
    def cleanups(self):
        if not '_cleanups' in vars(self):
            self._cleanups = []
        return self._cleanups

    def cleanup(self):
        for cu in self.cleanups:
            cu()
        self._cleanups = []