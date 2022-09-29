from turtle import color
import pygame
from pygame import MOUSEBUTTONDOWN, Rect, Surface, Color
from pygame.sprite import Sprite
from pygame.font import Font
from attrs import define, field

from gameobj import NeedsCleanup
from eventhandler import register_event_handler

@define(eq=False)
class Button(NeedsCleanup):
    rect: Rect
    text: str
    onclick: callable
    color: Color = 'firebrick1'

    font: Font = field()
    @font.default
    def _font_default(self):
        return pygame.font.Font('BungeeSpice.ttf', 32)

    def __attrs_post_init__(self):
        def click_handler(event):
            assert event.type == MOUSEBUTTONDOWN
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                print(f'clicked button {self.text}')
                self.onclick()
        self.cleanups.append(register_event_handler(MOUSEBUTTONDOWN, self, click_handler))

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=10)
        text = self.font.render(self.text, True, 'white')
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        surf.blit(text, text_rect)
