import pyglet

from VisibleEntity import *
from TaskQueue import *

class AnimatedEntity(VisibleEntity):

  def __init__(self, image, x, y, passable = 1):
    super(AnimatedEntity, self).__init__(image, x, y)
    self.animation_walk = [None, None, None, None]
    self.animation_halt = [None, None, None, None]
    self.animation_attack = [None, None, None, None]
    self.animation_action = [None, None, None, None]
    self.animation_die = [None, None, None, None]
    self.tasks = TaskQueue()
    self.direction = NORTH
    self.speed = 1

  def animate_walk(self, direction):
    if self.animation_walk[direction]:
      if self.image != self.animation_walk[direction]:
        self.image = self.animation_walk[direction]

  def animate_halt(self, direction):
    if self.animation_halt[direction]:
      if self.image != self.animation_halt[direction]:
        self.image = self.animation_halt[direction]
      
  def animate_attack(self, direction):
    if self.animation_attack[direction]:
      if self.image != self.animation_attack[direction]:
        self.image = self.animation_attack[direction]

  def animate_action(self, direction):
    if self.animation_action[direction]:
      if self.image != self.animation_action[direction]:
        self.image = self.animation_action[direction]

  def animate_die(self, direction):
    if self.animation_die[direction]:
      if self.image != self.animation_die[direction]:
        self.image = self.animation_die[direction]
   
  def get_animation(self):
    if self.direction == NORTH:
        return self.animation_north
    elif self.direction == SOUTH:
        return self.animation_south
    elif self.direction == EAST:
        return self.animation_east
    elif self.direction == WEST:
        return self.animation_west       

  def change_health(self, amount):
    self.health += amount

  def is_alive(self):
    return self.health > 0  
    

  def move(self, x, y, dt):
    if self.x < x:
      self.x += self.speed * 2

    if self.x > x:
      self.x -= self.speed * 2

    if self.y < y:
      self.y += self.speed

    if self.y > y:
      self.y -= self.speed

  def update(self, dt):
    if self.tasks.has_tasks():
      task = self.tasks.get_task()
      if task.is_walk():
        self.task_walk(task.data, dt)
      elif task.is_attack():
        print "elif"
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

    if self.x == point.x:
      if self.y == point.y:
        self.grid_x = point.grid_x
        self.grid_y = point.grid_y
        self.tasks.remove_task()

  def task_action(self, item):
    new_direction = self.find_direction(item.tile)
    if(new_direction != self.direction):
      self.direction = new_direction
      self.status = "change"

    item.animate_action(self.find_direction(item.tile))
    inv_item = self.game.map.chests.remove(item)
    self.inventory.add_item(InventoryItem(item.image, item.type))
    self.tasks.remove_task()
    
  def task_speak(self, person):
    self.game.message = person.speak()
    self.tasks.remove_task()

  def task_attack(self, person):
    print "Attack@!!@"
    self.tasks.remove_task()
