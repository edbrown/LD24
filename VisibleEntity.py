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

  def get_pixel(self, x, y):
    if x > self.x and y > self.y and x < (self.x + TILE_WIDTH) and y < (self.y + TILE_HEIGHT):

      y_pos = y - self.y
      x_pos = x - self.x
      
      pixel = self.image.get_region(x_pos, y_pos, 1, 1).get_image_data()
      data = pixel.get_data('A', 1)
      components = map(ord, list(data))
      return [float(c) for c in components]

    return [0.0]

  def contains(self, x, y):
    
    passed = 0
    last_in_shape = None
    y_pos = y
    while y_pos < (self.y + self.image.height):
      alpha_data = self.get_pixel(x, y_pos)
      if alpha_data[0] == 0.0:
        if last_in_shape == True:
          passed += 1
        last_in_shape = False
      else:
        if last_in_shape == False:
          passed += 1
        last_in_shape = True
          
      y_pos += 1
    
    return (passed % 2) == 1

  def print_coords(self):
    print 'X: {0}, y: {1}'.format(self.grid_x, self.grid_y)

  def is_passable(self):
    return self.passable == PASSABLE
