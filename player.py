from __future__ import annotations
import pygame
from pygame.sprite import Group, DirtySprite, AbstractGroup, Sprite
from pygame import KEYUP, Rect
from pygame.event import Event
from pygame.locals import KEYDOWN
from attrs import define, field, Factory

from gameobj import NeedsCleanup
from ball import Ball
from gvars import SCREEN
from magic import MagicSource
from utils import relrect, relrect_side
from eventhandler import register_event_handler
from keymap import Keymap


class PlayerSprite(DirtySprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, rect: Rect, player: 'Player') -> None:
        super().__init__()
        self.player = player
        self.image = pygame.image.load("wizard.png")
        self.image = pygame.transform.scale(self.image, rect.size)
        if player.side == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = rect

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.player.v)

class Health(Sprite):
    full: int = 100
    curr: int = 100
    rect: Rect

    def __init__(self, rect) -> None:
        super().__init__()
        self.rect = rect

    def draw(self):
        pygame.draw.rect(SCREEN, "black", self.rect)
        indicator = self.rect.copy()
        indicator.width = self.rect.width * self.curr / self.full
        pygame.draw.rect(SCREEN, "red", indicator)


class BallIndicator(Sprite):
    def __init__(self, rect, player: "Player") -> None:
        super().__init__()
        self.rect: Rect = rect
        self.player = player

    def draw(self):
        draw_w = self.rect.width / len(self.player.balls)
        ball_w = min((draw_w * 0.8, self.rect.height))
        for i in range(len(self.player.inactive_balls)):
            centerx = self.rect.left + (i + 0.5) * draw_w
            pygame.draw.circle(
                SCREEN, "firebrick1", (centerx, self.rect.centery), ball_w // 2
            )


class Player(Group, NeedsCleanup):
    side: str
    lives: int = 3
    nballs: int = 5
    balls: list[Ball]
    rect: Rect
    v: list[int, int]
    speed: int = 3
    health: Health
    keymap: Keymap

    @property
    def inactive_balls(self):
        out = []
        for b in self.balls:
            if not b.active:
                out.append(b)
        return out

    @property
    def active_balls(self):
        out = []
        for b in self.balls:
            if b.active:
                out.append(b)
        return out

    @property
    def center(self):
        return self.psprite.rect.center

    @property
    def rect(self):
        return self.psprite.rect

    @property
    def name(self):
        return type(self).__name__

    def __init__(self, side) -> None:
        super().__init__()
        self.side = side
        self.v = [0, 0]
        self.balls = []
        self.magic = MagicSource(
            relrect_side(SCREEN, side, 0.02, 0.04, 0.46, 0.04, (0, 0.5))
        )
        self.add(self.magic)

        player_rect = relrect_side(SCREEN, side, 0.1, 0.5, 0.08, 0.08)
        self.forward = [1, 0] if side == "left" else [-1, 0]
        self.psprite = PlayerSprite(player_rect, self)
        self.add(self.psprite)

        ball_rect = relrect(SCREEN, 0, 0, 0.04, 0.04)
        for i in range(self.nballs):
            b = Ball(ball_rect)
            self.balls.append(b)
            self.add(b)

        self.health = Health(
            relrect_side(SCREEN, side, 0.02, 0.10, 0.23, 0.04, (0, 0.5))
        )
        self.add(self.health)

        self.add(
            BallIndicator(
                relrect_side(SCREEN, side, 0.26, 0.10, 0.23, 0.04, (0, 0.5)), self
            )
        )

        self.keymap = Keymap(side)
        trajs = {
            self.keymap.t1: self.traj1,
            self.keymap.t2: self.traj2,
            self.keymap.t3: self.traj3,
        }

        def handle_keydown(event: Event):
            if event.key in trajs.keys():
                traj = trajs[event.key]
                if len(self.inactive_balls) > 0:
                    req_v = traj(self.center, self.v)
                    if not self.magic.can_update(self.v, req_v):
                        return
                    ball = self.inactive_balls[0]
                    ball.rect.center = self.center
                    ball.v = self.v.copy()
                    ball.start_traj(trajs[event.key], self.magic)
                    ball.active = True

            # movement
            elif event.key == self.keymap.left:
                self.v[0] = -self.speed
            elif event.key == self.keymap.right:
                self.v[0] = self.speed
            elif event.key == self.keymap.up:
                self.v[1] = -self.speed
            elif event.key == self.keymap.down:
                self.v[1] = self.speed

        def handle_keyup(event: Event):
            if event.key in (self.keymap.left, self.keymap.right):
                self.v[0] = 0
            elif event.key in (self.keymap.up, self.keymap.down):
                self.v[1] = 0

        self.cleanups.append(register_event_handler(KEYDOWN, self, handle_keydown))
        self.cleanups.append(register_event_handler(KEYUP, self, handle_keyup))

    def hit(self):
        self.health.curr -= 30

    def traj1(self, pos, v):
        return v

    def traj2(self, pos, v):
        return v

    def traj3(self, pos, v):
        return v