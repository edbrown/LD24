import pyglet

from pathfinding import *

data = [
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]
TILE_WIDTH = 64
TILE_HEIGHT = 32
OFFSET_Y = 200;

PASSABLE = 0
IMPASSABLE  = 1

class Game(pyglet.window.Window):
  def __init__(self):
    super(Game, self).__init__()
    self.map = Map()
    self.pathfinding = AStar(self.map)

    self.pathfinding.calcShortest(self.map.tiles[5], self.map.tiles[24])

  def on_draw(self):
    self.map.draw() 

class Map():
  def __init__(self):
    self.grid = pyglet.image.ImageGrid(pyglet.image.load("resources/tiles.png"), 16, 2, TILE_WIDTH, TILE_HEIGHT)
    self.grid = pyglet.image.TextureGrid(self.grid)
    self.tiles = []
    for i in range(len(data)):
      for j in range(len(data[i])):
        if(data[i][j] == PASSABLE):
          type = self.grid[1,0]
        else:
          type = self.grid[0,0]

        self.tiles.append(Tile(type, i, j, data[i][j]))


  def draw(self):
    for tile in self.tiles:
      tile.draw()

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

if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


