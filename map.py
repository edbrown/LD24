import pyglet

from tile import *
from unit import *

PASSABLE = 0
IMPASSABLE  = 1
TILE_WIDTH = 64
TILE_HEIGHT = 32
OFFSET_Y = 200

class Map():
  def __init__(self, data):
    self.data = data;
    self.grid = pyglet.image.ImageGrid(pyglet.image.load("resources/tiles.png"), 16, 2, TILE_WIDTH, TILE_HEIGHT)
    self.grid = pyglet.image.TextureGrid(self.grid)
    self.tiles = []
    for i in range(len(data)):
      for j in range(len(data[i])):
        if(self.data[i][j] == PASSABLE):
          type = self.grid[1,0]
        else:
          type = self.grid[0,0]
        self.tiles.append(Tile(type, i, j, self.data[i][j]))
    self.unit = Unit(self.grid[2,1], 0, 0)

  def draw(self):
    for tile in self.tiles:
      tile.draw()
    self.unit.draw()

  def get_tile(self, x, y):
    for tile in self.tiles: 
      if tile.grid_x == x and tile.grid_y == y:
        return tile
    
    return None


  def get_adjacent(self, tile):
    
    adj = []
    if tile.grid_x > 0:
      adj.append(self.get_tile(tile.grid_x - 1, tile.grid_y))

    if tile.grid_y > 0:
      adj.append(self.get_tile(tile.grid_x, tile.grid_y - 1))

    if tile.grid_x < (len(data) - 1):
      adj.append(self.get_tile(tile.grid_x + 1, tile.grid_y))

    if tile.grid_y < (len(data[0]) - 1):
      adj.append(self.get_tile(tile.grid_x, tile.grid_y + 1))
      
    return adj

  def print_tile(self, tile):
    print 'X: {0}, y: {1}, g_x: {2}, g_y: {3}'.format(tile.x, tile.y, tile.grid_x, tile.grid_y)
