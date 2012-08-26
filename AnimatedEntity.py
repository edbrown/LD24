import pyglet

from VisibleEntity import *

class AnimatedEntity(VisibleEntity):

  def __init__(self, image, x, y, passable = 1):
    super(AnimatedEntity, self).__init__(image, x, y)
    self.animate_walk = [None, None, None, None]
    self.animate_halt = [None, None, None, None]
    self.animate_attack = [None, None, None, None]
    self.animate_action = [None, None, None, None]
    self.animate_die = [None, None, None, None]

  def walk(self, direction):
    if self.animate_walk[direction]:
      self.image = animate_walk[direction]

  def halt(self, direction):
    if self.animate_halt[direction]:
      self.image = animate_halt[direction]
      
  def attack(self, direction):
    if self.animate_attack[direction]:
      self.image = animate_attack[direction]

  def action(self, direction):
    if self.animate_action[direction]:
      self.image = animate_attack[direction]

  def die(self, direction):
    if self.animate_die[direction]:
      self.image = animate_die[direction]
