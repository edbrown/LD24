import pyglet
from VisibleEntity import *
from definitions import *

class Unit(VisibleEntity):
  
  
  def __init__(self, image, x = 0, y = 0):
    super(Unit, self).__init__(image, x, y)
    self.tasks = []
    self.speed = 1
    self.direction = NORTH
    self.scale = 0.5

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
    if self.tasks:
      point = self.tasks[0]
      new_direction = self.find_direction(point)
      if(new_direction != self.direction):
        self.direction = new_direction
        self.image = self.get_animation()

      self.move(point.x, point.y, dt)
      if self.x == point.x:
        if self.y == point.y:
          self.grid_x = point.grid_x
          self.grid_y = point.grid_y

          point = self.tasks.pop(0)
    

  
  def set_animation(self, north, south, east, west):
    self.image = north
    self.animation_north = (north)
    self.animation_south = (south)
    self.animation_east = (east)
    self.animation_west = (west)

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


    print direction

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

