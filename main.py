import pyglet

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

  def on_draw(self):
    self.map.draw() 

class Map():
  def __init__(self):
    self.grid = pyglet.image.ImageGrid(pyglet.image.load("resources/tiles.png"), 16, 2, TILE_WIDTH, TILE_HEIGHT)
    self.grid = pyglet.image.TextureGrid(self.grid)
    self.tiles = []
    for i in range(len(data)):
      for j in range(len(data[i])):
        x = (j * TILE_WIDTH / 2) + (i * TILE_WIDTH / 2)
        y = (i * TILE_HEIGHT / 2) - (j * TILE_HEIGHT / 2)
        if(data[i][j] == PASSABLE):
          type = self.grid[1,0]
        else:
          type = self.grid[0,0]

        self.tiles.append(Tile(type,x, y, data[i][j]))

  def draw(self):
    for tile in self.tiles:
      tile.draw()



class Tile(pyglet.sprite.Sprite):
  def __init__(self, image, x = 0, y = 0, passable = 0):
    super(Tile, self).__init__(image)
    self.x = x
    self.y = y + OFFSET_Y
    self.passable = passable

if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


