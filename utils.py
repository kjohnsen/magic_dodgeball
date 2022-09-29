from pygame import Rect, Surface


def relrect(screen: Surface, left, top, width, height, obj_center=(0.5, 0.5)):
    sw, sh = screen.get_width(), screen.get_height()
    width_abs = width * sw
    height_abs = height * sh
    left_abs = int(sw * (left - width * obj_center[0]))
    top_abs = int(sh * (top - height * obj_center[1]))
    return Rect(left_abs, top_abs, width_abs, height_abs)

def relrect_side(screen: Surface, side, left, top, width, height, obj_center=(.5, .5)):
    if side == 'right':
        left = 1 - left
        obj_center = [1 - obj_center[0], obj_center[1]]
    return relrect(screen, left, top, width, height, obj_center)
