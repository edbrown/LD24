import pyglet
from definitions import *

class VisibleEntity(pyglet.sprite.Sprite):
  def __init__(self, image, x, y):
    super(VisibleEntity, self).__init__(image)
    self.grid_x = x
    self.grid_y = y
    self.x = 0
    self.y = 0
    self.set_real_coords(x, y)

  def set_real_coords(self, x, y):
    self.x = (y * TILE_WIDTH / 2) + (x * TILE_WIDTH / 2)
    self.y = (x * TILE_HEIGHT / 2) - (y * TILE_HEIGHT / 2) + OFFSET_Y

  def get_pixel(self, image, x, y):
    if x > self.x and y > self.y and x < (self.x + image.width) and y < (self.y + image.height):

      y_pos = int(y - self.y)
      x_pos = int(x - self.x)
      
      pixel = image.get_region(x_pos, y_pos, 1, 1).get_image_data()
      data = pixel.get_data('A', 1)
      components = map(ord, list(data))
      return [float(c) for c in components]

    return [0.0]

  def contains(self, image, x, y):
    
    passed = 0
    last_in_shape = None
    y_pos = y
    while y_pos < (y + image.height):
      alpha_data = self.get_pixel(image, x, y_pos)
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

  def find_direction(self, point, origin=None):
    if not origin:
      origin = self
    point_x = point.grid_x
    point_y = point.grid_y
    self_x = origin.grid_x
    self_y = origin.grid_y
    direction = NORTH;

    if(point_x == self_x):
      if(point_y > self_y):
        direction = WEST
      if(point_y < self_y):
        direction = EAST
    elif(point_y == self_y):
      if(point_x > self_x):
        direction = NORTH
      if(point_x < self_x):
        direction = SOUTH

    return direction

  def print_coords(self):
    print 'X: {0}, y: {1}'.format(self.grid_x, self.grid_y)
