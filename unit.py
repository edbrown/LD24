import pyglet
from VisibleEntity import *
from definitions import *

class Unit(VisibleEntity):
  def __init__(self, image, x = 0, y = 0):
    super(Unit, self).__init__(image, x, y)

  def move(self, x, y):
    self.grid_x = x
    self.grid_y = y
    self.set_real_coords(x, y)

