from gameobj import NeedsCleanup

class Scene():
    def __init__(self, surf, game: 'Game', *args, **kwargs):
        self.surf = surf
        self.game = game
        self.things = []
        self.init(*args, **kwargs)
    
    def init(self, *args, **kwargs):
        pass

    def draw(self):
        self.draw_bg()
        for g in self.things:
            g.draw()

    def draw_bg(self):
        pass

    def update(self):
        self.update_self()
        for g in self.things:
            g.update()

    def update_self(self):
        pass

    def cleanup(self):
        self.cleanup_self()
        for child in vars(self).values():
            if isinstance(child, NeedsCleanup):
                child.cleanup()

    def cleanup_self(self):
        pass