import pyglet
from definitions import *

TILE_HEIGHT = 32
TILE_WIDTH = 64
OFFSET_Y = 200

class VisibleEntity(pyglet.sprite.Sprite):
  def __init__(self, image, x, y, passable = 1):
    super(VisibleEntity, self).__init__(image)
    self.passable = passable
    self.grid_x = x
    self.grid_y = y
    self.x = 0
    self.y = 0
    self.set_real_coords(x, y)

  def set_real_coords(self, x, y):
    self.x = (y * TILE_WIDTH / 2) + (x * TILE_WIDTH / 2)
    self.y = (x * TILE_HEIGHT / 2) - (y * TILE_HEIGHT / 2) + OFFSET_Y

  def set_passable(self, passable):
    self.passable = passable

  def contains(self, x, y):
    x_pos = x
    y_pos = y
    x_pos -= x % TILE_WIDTH
    y_pos -= (y-OFFSET_Y) % TILE_HEIGHT

    if x_pos == self.x:
      if y_pos == self.y:
        return True
      else:
        return False
    else:
      return False

  def print_coords(self):
    print 'X: {0}, y: {1}'.format(self.grid_x, self.grid_y)

  def is_passable(self):
    return self.passable == PASSABLE
