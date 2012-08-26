import pyglet
from AnimatedEntity import *
from definitions import *
from AnimationBuilder import *
from TaskQueue import *
from Inventory import *
from item import *

class Player(AnimatedEntity):
  
  
  def __init__(self, game, image, x = 0, y = 0):
    super(Player, self).__init__(image, x, y)
    print self.x
    self.tasks = TaskQueue()
    self.speed = 1
    self.direction = NORTH
    self.scale = 0.5
    self.health = 100
    self.moving = False
    self.game = game

    inventory_image = pyglet.image.load("resources/inventory.png")
    self.inventory = Inventory(inventory_image)


  def create_animations(self):
    sprite_sheet = pyglet.image.ImageGrid(pyglet.image.load("resources/minotaur.png"), 8, 24, 128, 128)
    grid = pyglet.image.TextureGrid(sprite_sheet)
    self.animation_walk = [
      AnimationBuilder.build(grid, 4, 4, 11),
      AnimationBuilder.build(grid, 0, 4, 11),
      AnimationBuilder.build(grid, 6, 4, 11),
      AnimationBuilder.build(grid, 2, 4, 11)
    ]
    self.animation_halt = [
      AnimationBuilder.build(grid, 4, 0, 3),
      AnimationBuilder.build(grid, 0, 0, 3),
      AnimationBuilder.build(grid, 6, 0, 3),
      AnimationBuilder.build(grid, 2, 0, 3)
    ]
    self.animation_action = [
      AnimationBuilder.build(grid, 4, 4, 11),
      AnimationBuilder.build(grid, 0, 4, 11),
      AnimationBuilder.build(grid, 6, 4, 11),
      AnimationBuilder.build(grid, 2, 4, 11)
    ]
    self.animation_attack = [
      AnimationBuilder.build(grid, 4, 4, 11),
      AnimationBuilder.build(grid, 0, 4, 11),
      AnimationBuilder.build(grid, 6, 4, 11),
      AnimationBuilder.build(grid, 2, 4, 11)
    ]
    self.animation_die = [
      AnimationBuilder.build(grid, 4, 4, 11),
      AnimationBuilder.build(grid, 0, 4, 11),
      AnimationBuilder.build(grid, 6, 4, 11),
      AnimationBuilder.build(grid, 2, 4, 11)
    ]

    self.animate_halt(NORTH)

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
        pass
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

  def find_direction(self, point):
    point_x = point.grid_x
    point_y = point.grid_y
    self_x = self.grid_x
    self_y = self.grid_y
    direction = NORTH;

    if(point_x == self_x):
      if(point_y > self_y):
        direction = WEST
      if(point_y < self_y):
        direction = EAST
    elif(point_y == self_y):
      if(point_x > self_x):
        direction = NORTH
      if(point_x < self_x):
        direction = SOUTH

    return direction
  
  def get_animation(self):
    if self.direction == NORTH:
        return self.animation_north
    elif self.direction == SOUTH:
        return self.animation_south
    elif self.direction == EAST:
        return self.animation_east
    elif self.direction == WEST:
        return self.animation_west

