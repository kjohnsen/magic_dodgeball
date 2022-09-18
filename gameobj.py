class GameObject():
  '''mixin for standard things: draw, update, process event on self and recursively on GameObject children'''


  @property
  def children(self):
    for c in vars(self):
      if type(c) == GameObject:
        yield c
  
  def draw(self):
    self.draw_self()
    for c in self.children:
      c.draw()

  def draw_self(self):
    pass

  def update(self):
    self.update_self()
    for c in self.children:
      c.update()

  def update_self(self):
    pass

  def register_event_handler(event_type, function):
    
