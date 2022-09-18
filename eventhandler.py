class EventHandler:
  event_handlers = {{}}  # persistent across instances
  
  @classmethod
  @property
  def register_event_handler(event_type, function):
    ehs_for_type = self.event_handlers.get(event_type, [])
