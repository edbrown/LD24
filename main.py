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
    pyglet.clock.schedule_interval(self.update, 1/120.0)

  def on_draw(self):
    self.clear()
    self.map.draw() 
 
  def update(self, dt):
    self.map.unit.update(dt)



  def on_mouse_press(self, x, y, button, modifiers):
    if button == RIGHT_CLICK:
      for tile in self.map.tiles:
        if(tile.contains_2(x, y) == True):
          tasks = self.pathfinding.calcShortest(self.map.get_tile(self.map.unit.grid_x, self.map.unit.grid_y), tile)
          if tasks:
            tasks.reverse()
            self.map.unit.tasks = tasks
          else:
            print "No path!"
          break;

if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


