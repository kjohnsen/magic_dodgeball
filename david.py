from player import Player

class David(Player):
    def traj1(self, pos, v):
        v = [5*s for s in self.forward]
        return v

    def traj2(self, pos, v):
        v = [5*s for s in self.forward]
        return v

    def traj3(self, pos, v):
        v = [5*s for s in self.forward]
        return v
