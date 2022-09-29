from button import Button
from scene import Scene
from gvars import DARKPURPLE
from utils import relrect


class End(Scene):
    def init(self, winner):
        self.winner = winner
        self.text = Button(
            relrect(self.surf, 0.5, 0.4, 0.5, 0.2),
            f"{winner.name} wins",
            lambda: None,
            DARKPURPLE,
        )
        self.restart = Button(
            relrect(self.surf, 0.5, 0.6, 0.3, 0.1),
            f"restart",
            lambda: self.game.change_scene('Menu'),
            DARKPURPLE,
        )

    def draw_bg(self):
        self.surf.fill("black")
        self.text.draw(self.surf)
        self.restart.draw(self.surf)
