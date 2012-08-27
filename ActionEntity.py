import pyglet

from AnimatedEntity import *
from item import *
from pathfinding import *

class ActionEntity(AnimatedEntity):
    def __init__(self, game, image, x, y, passable = 1, follow = False):
        super(ActionEntity, self).__init__(image, x, y)
        self.follow = follow
        self.tasks = TaskQueue()
        self.last_attack = 0
        self.health = 100
        self.attack_speed = 0.4
        self.damage = 20
        self.tile = None
        self.game = game

    def update(self, dt):
      if self.tasks.has_tasks():
        task = self.tasks.get_task()
        if task.is_walk():
          self.task_walk(task.data, dt)
        elif task.is_attack():
          self.task_attack(task.data, dt)
        elif task.is_action():
          self.task_action(task.data)
        elif task.is_speak():
          self.task_speak(task.data)
        elif task.is_halt():
          self.task_halt()
        elif task.is_goto():
          self.task_goto(task.data)
        else:
          print "Task not supported"
        
      else:
        pass
    
    def task_goto(self, person):
      move_loc = person.tile.get_move_loc()
      tasks = self.game.pathfinding.calcShortest(self.game.map.get_tile(self.grid_x, self.grid_y),self.game.map.get_tile(move_loc[0], move_loc[1]))

      if self.grid_x == person.grid_x and self.grid_y == person.grid_y:
        self.tasks.remove_task()
      else:
        if len(tasks) >= 2:
          self.tasks.tasks.appendleft(Task(tasks.pop(len(tasks)-2), TASK_WALK))


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
          if self.tile:
            self.tile.person = None
          self.tile = point
          self.tile.add_person(self)
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
        inv_item = self.game.map.items.remove(item)
        if item.image.frames:
            self.inventory.add_item(InventoryItem(item.id, item.image.frames[0].image, item.type))
        else:
            self.inventory.add_item(InventoryItem(item.id, item.image, item.type))
          
        self.tasks.remove_task()
    
    def task_speak(self, person):
      self.game.message = person.speak()
      self.tasks.remove_task()

    def task_attack(self, person, dt):
      if person.tasks.has_tasks():
        person.tasks.clear_tasks()
        person.tasks.add_task(None, TASK_HALT)
      self.animate_attack(self.find_direction(self, person.tile))
      if self.last_attack >= self.attack_speed:
        self.last_attack -= self.attack_speed
        person.hit(self.damage)
        print "Attacked for %s damage" % self.damage
        if not person.is_alive():
          print "Dead"
          self.tasks.clear_tasks()
          self.tasks.add_task(None, TASK_HALT)
          person.tasks.clear_tasks()
          person.die()
      
      self.last_attack += dt

    def task_halt(self):
      self.animate_halt(self.direction)

    def hit(self, amount):
      self.health -= amount
