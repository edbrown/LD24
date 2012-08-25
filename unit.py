import pyglet
from VisibleEntity import *
from definitions import *

class Unit(VisibleEntity):
  
  
  def __init__(self, image, x = 0, y = 0):
    super(Unit, self).__init__(image, x, y)
    self.tasks = []
    self.speed = 1

  def move(self, x, y, dt):
    if self.x < x:
      self.x += self.speed *2

    if self.x > x:
      self.x -= self.speed * 2

    if self.y < y:
      self.y += self.speed

    if self.y > y:
      self.y -= self.speed

  def update(self, dt):
    if self.tasks:
      point = self.tasks[0]
      self.move(point.x, point.y, dt)
      if self.x == point.x:
        if self.y == point.y:
          self.grid_x = point.grid_x
          self.grid_y = point.grid_y

          point = self.tasks.pop(0)



