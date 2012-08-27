import pyglet

from AnimatedEntity import *
from item import *

class ActionEntity(AnimatedEntity):
    def __init__(self, image, x, y, passable = 1, follow = False):
        super(ActionEntity, self).__init__(image, x, y)
        self.tasks = TaskQueue()
        self.follow = follow
        print "Follow"
        print self.follow

    def update(self, dt):
      if self.tasks.has_tasks():
        task = self.tasks.get_task()
        if task.is_walk():
          self.task_walk(task.data, dt)
        elif task.is_attack():
          self.task_attack(task.data)
        elif task.is_action():
          self.task_action(task.data)
        elif task.is_speak():
          self.task_speak(task.data)
        else:
          print "Task not supported"
        
      else:
        self.animate_halt(self.direction)

    def task_walk(self, point, dt):
      new_direction = self.find_direction(point)
      if(new_direction != self.direction):
        self.direction = new_direction
        self.status = "change"

      self.animate_walk(self.direction)
      self.move(point.x, point.y, dt)

      if point.item:
        if point.item.is_floor_item():
          self.task_action(point.item)

      if self.follow:
        self.game.update_viewport()

      if self.x == point.x:
        if self.y == point.y:
          self.grid_x = point.grid_x
          self.grid_y = point.grid_y
          self.tasks.remove_task()

    def task_action(self, item):
      cur_tile = self.game.map.get_tile(self.grid_x, self.grid_y)
      adj = self.game.map.get_adjacent(cur_tile)
      if adj.count(item.tile):
        new_direction = self.find_direction(item.tile)
        if(new_direction != self.direction):
          self.direction = new_direction
          self.status = "change"

        item.animate_action(self.find_direction(item.tile))
        inv_item = self.game.map.remove_item(item)
        if item.image.frames:
            self.inventory.add_item(InventoryItem(item.id, item.image.frames[0].image, item.type))
        else:
            self.inventory.add_item(InventoryItem(item.id, item.image, item.type))
          
        self.tasks.remove_task()
    
    def task_speak(self, person):
      self.game.message = person.speak()
      self.tasks.remove_task()

    def task_attack(self, person):
      self.animate_attack(self.direction)
