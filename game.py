from gameobj import GameObject

class Game(GameObject):
  def __init__(self, screen, start_scene):
    self.screen = screen
    self.current = start_scene(screen, self)
    self.event_handlers = {}

  def change_scene(self, scene_type):
    self.current = scene_type(self.sreen, self)



class Scene(GameObject): 
  def __init__(self, screen, sm: Game, *args, **kwargs):
    self.screen = screen
    self.scene_mgr = sm
    self.children = []
    self.init(*args, **kwargs)

  
  def process_event(self, event):
    self.process_event_scene(event)
    for c in self.children:
      c.process_event(event)

  def process_event_scene(self, event):
    pass
