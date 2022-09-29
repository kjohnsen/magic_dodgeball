from pygame.locals import *

class Keymap():
    t1: int
    t2: int
    t3: int
    up: int
    down: int
    left: int
    right: int

    def __init__(self, side) -> None:
        if side == 'left':
            self.t1 = K_1
            self.t2 = K_2
            self.t3 = K_3
            self.up = K_w
            self.down = K_s
            self.left = K_a
            self.right = K_d
        elif side == 'right':
            self.t1 = K_8
            self.t2 = K_9
            self.t3 = K_0
            self.up = K_i
            self.down = K_k
            self.left = K_j
            self.right = K_l