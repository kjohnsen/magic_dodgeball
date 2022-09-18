import pygame
from pygame import Rect
from scenemgr import Scene

class Button():
  def __init__(self, rect, c='gray'):
    self.rect = rect
    self.c = c
    
  def draw(self):
    pygame.draw.rect(self.screen, self.c, self.rect)

class Menu(Scene):
      
  bg = (100, 100, 100)
  
  def init(self):
    self.add_child(StartButton)
    pass
  
  def draw_scene(self):
    self.screen.fill(self.bg)