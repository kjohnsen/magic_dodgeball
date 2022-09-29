from attrs import define, field, Factory

from gameobj import GameObject, NeedsCleanup
from gvars import SCREEN
import scenelist
from scenelist import *


# @define
class Game():
    scene = None

    def __init__(self, surf, start_scene):
        self.surf = surf
        self.scene = start_scene(surf, self)

    def change_scene(self, scene_type, *args, **kwargs):
        prev = self.scene
        scene_type = getattr(scenelist, scene_type)
        self.scene = scene_type(self.surf, self, *args, **kwargs)
        prev.cleanup()
        del prev

