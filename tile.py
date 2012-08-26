import pyglet
from VisibleEntity import *
from definitions import *

class Tile(VisibleEntity):

  item = None
  
  def __init__(self, image, x = 0, y = 0, passable = 1):
    super(Tile, self).__init__(image, x, y)
    self.parent = None
    self.f = 0
    self.g = 0
    self.passable = passable

  def add_item(self, item):
    self.item = item

  def remove_item(self, item):
    temp = self.item
    self.item = None
    return temp

  def is_passable(self):
    return self.passable == PASSABLE
  
  def set_passable(self, passable):
    self.passable = passable
