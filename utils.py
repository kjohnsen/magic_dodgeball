from pygame import Rect

def relrect(screen, top, left, widgth, height):
  topabs = int(top/screen.height) + height//2
  leftabs = int(left/screen.width) + width//2
  