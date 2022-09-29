from player import Player

class Kyle(Player):
    def traj1(self, pos, v):
        v = [5*s for s in self.forward]
        return v
