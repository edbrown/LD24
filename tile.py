import pyglet
from VisibleEntity import *
from definitions import *

class Tile(VisibleEntity):

  def __init__(self, image, x = 0, y = 0, passable = 1):
    super(Tile, self).__init__(image, x, y)
    self.parent = None
    self.f = 0
    self.g = 0
    self.passable = passable
    self.item = None
    self.person = None

  def add_item(self, item):
    self.item = item

  def remove_item(self, item):
    temp = self.item
    self.item = None
    return temp

  def add_person(self, person):
    self.person = person

  def remove_person(self, person):
    temp = self.person
    self.person = None
    return temp

  def is_empty(self):
    return self.item == None

  def get_move_loc(self):
    if self.is_empty():
      return [self.grid_x, self.grid_y]

    return self.item.get_item_move_loc()

  def is_passable(self):
    if self.is_empty:
      return self.passable == PASSABLE
    return self.passable == PASSABLE and self.item.is_chest_item()
  
  def set_passable(self, passable):
    self.passable = passable
