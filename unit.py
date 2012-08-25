import pyglet
from definitions import *

class Unit(pyglet.sprite.Sprite):
  def __init__(self, image, x = 0, y = 0):
    super(Unit, self).__init__(image)
    self.x = (y * TILE_WIDTH / 2) + (x * TILE_WIDTH / 2)
    self.y = (x * TILE_HEIGHT / 2) - (y * TILE_HEIGHT / 2) + OFFSET_Y
