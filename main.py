import pyglet

from pathfinding import *
from map import *
from definitions import *
from Message import *
from Player import *
from Enemy import *
from NPC import *

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
    self.npc = NPC(self.map.grid[2,1], self.map.get_tile(7,5))
    self.player.create_animations()
    self.npc.create_animations()
    self.enemy = Enemy(self, self.map.grid[2,1], self.map.get_tile(1,5))
    self.enemy.create_animations()

 
  def update(self, dt):
    self.clear()
    self.map.draw()
    self.player.draw()
    self.enemy.draw()
    self.npc.draw()
    self.player.inventory.update()

    if not self.message.finished:
      self.pause = True
      self.message.show()
    else:
      self.pause = False
    if self.pause:
      return  
    self.player.update(dt)
    if not self.enemy.tasks.has_tasks(): 
      self.enemy.calculate_next_move()
      self.enemy.tasks.add_task(self.enemy.next_move, TASK_WALK)
    self.enemy.update(dt)

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
              if len(tasks) > 1:
                self.player.tasks.clear_tasks()
                tasks.reverse()
                tasks.pop(0)
                index = len(tasks) - 1
                for task in tasks:
                  self.player.tasks.add_task(task, TASK_WALK)

                if type(tasks[index].person) == NPC:
                  action = self.player.tasks.add_task(tasks[index].person, TASK_SPEAK)
                if type(tasks[index].person) == Enemy:
                  print "Add attack"
                  action = self.player.tasks.add_task(tasks[index].person, TASK_ATTACK)
                  
            else:
              print "No path!"
            break;

      for chest in self.map.chests:
        if chest.contains(x, y):
          self.player.tasks.add_task(chest, TASK_ACTION)


if __name__ == "__main__":
  game = Game() #creates a 'MyGame' instance
  pyglet.app.run() #starts the pyglet application


