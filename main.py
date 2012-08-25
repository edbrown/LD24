import pyglet

from pathfinding import *
from map import *
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

LEFT_CLICK = 1
RIGHT_CLICK = 4

PASSABLE = 0
IMPASSABLE  = 1


class Game(pyglet.window.Window):
  def __init__(self):
    super(Game, self).__init__()
    self.map = Map(data)
    self.pathfinding = AStar(self.map)

    self.pathfinding.calcShortest(self.map.tiles[5], self.map.tiles[12])

  def on_draw(self):
    self.map.draw() 

  def on_mouse_press(self, x, y, button, modifiers):
    if button == RIGHT_CLICK:
      print self.map.unit.x

if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


