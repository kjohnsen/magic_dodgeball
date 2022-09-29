from math import sin
from player import Player

class Kyle(Player):
    def traj1(self, pos, v):
        v = [5*s for s in self.forward]
        return v

    def traj2(self, pos, v):
        vx = 5*self.forward[0]
        vy = 5*sin(pos[0]/50)
        return [vx, vy]

    def traj3(self, pos, v):
        # target is 400 pixels away from wherever the player is
        xtarget = self.center[0] + 400 * self.forward[0]
        slowdown = 40
        vx = (xtarget - pos[0]) / slowdown
        vy = self.v[1]
        return [vx, vy]
