import pyglet

from pathfinding import *
from map import *
from definitions import *

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


class Game(pyglet.window.Window):
  def __init__(self):
    super(Game, self).__init__()
    self.map = Map(data)
    self.pathfinding = AStar(self.map)

    self.pathfinding.calcShortest(self.map.tiles[4], self.map.tiles[6])

  def on_draw(self):
    self.map.draw() 

  def on_mouse_press(self, x, y, button, modifiers):
    if button == RIGHT_CLICK:
      for tile in self.map.tiles:
        if tile.contains_2(x, y):
          self.map.unit.move(tile.grid_x, tile.grid_y)
          break;

if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


