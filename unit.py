import pyglet
from VisibleEntity import *
from definitions import *

class Unit(VisibleEntity):
  def __init__(self, image, x = 0, y = 0):
    super(Unit, self).__init__(image, x, y)
