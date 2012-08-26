import pyglet

from pathfinding import *
from map import *
from definitions import *
from Message import *
from Player import *

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
    self.pause = False
    self.message = Message(["Well hello there, you sexy beast. This is long text...", "You bastard"]);
    self.player = Player(self, self.map.grid[2,1], 0, 0)
    self.player.create_animations()

 
  def update(self, dt):
    self.clear()
    self.map.draw()
    self.player.draw()
    if not self.message.finished:
      self.pause = True
      self.message.show()
    else:
      self.pause = False
    if self.pause:
      return  
    self.player.update(dt)

  def on_mouse_press(self, x, y, button, modifiers):
    if button == LEFT_CLICK:
      if self.message:
        self.message.next()
    if self.pause:
      return
    if button == RIGHT_CLICK:
      for tile in self.map.tiles:
        if(tile.contains(x, y) == True):
          if tile.is_passable():
            move_loc = tile.get_move_loc()
            tasks = self.pathfinding.calcShortest(self.map.get_tile(self.player.grid_x, self.player.grid_y), self.map.get_tile(move_loc[0], move_loc[1]))
            if tasks:
              tasks.reverse()
              if len(tasks) != 0:
                tasks.pop(0)
                self.player.tasks.clear_tasks()
                for task in tasks:
                  self.player.tasks.add_task(task, TASK_WALK)
            else:
              print "No path!"
            break;



if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


