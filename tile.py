import pyglet


TILE_HEIGHT = 32
TILE_WIDTH = 64
OFFSET_Y = 200

class Tile(pyglet.sprite.Sprite):  
  def __init__(self, image, x = 0, y = 0, passable = 0):
    super(Tile, self).__init__(image)
    self.grid_x = x
    self.grid_y = y
    self.x = (y * TILE_WIDTH / 2) + (x * TILE_WIDTH / 2)
    self.y = (x * TILE_HEIGHT / 2) - (y * TILE_HEIGHT / 2) + OFFSET_Y
    self.passable = passable
    self.parent = None
    self.f = 0
    self.g = 0

  def is_passable(self):
    return self.passable == PASSABLE
