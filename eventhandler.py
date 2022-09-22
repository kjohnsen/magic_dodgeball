class EventHandler:
    event_handlers = {}  # persistent across instances

    @classmethod
    def handle(cls, event):
        ehs_for_type = cls.event_handlers.get(event.type, {}).copy()
        for owner, handler in ehs_for_type.items():
            handler(event)


def register_event_handler(event_type, owner, function):
    if not event_type in EventHandler.event_handlers.keys():
        EventHandler.event_handlers[event_type] = {}
    ehs_for_type = EventHandler.event_handlers[event_type]
    ehs_for_type[owner] = function

    def unregister():
        del EventHandler.event_handlers[event_type][owner]

    return unregister
