import pyglet
from VisibleEntity import *
from definitions import *

class Tile(VisibleEntity):  
  def __init__(self, image, x = 0, y = 0, passable = 0):
    super(Tile, self).__init__(image, x, y)
    passable = passable
    self.parent = None
    self.f = 0
    self.g = 0
