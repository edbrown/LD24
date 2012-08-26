import pyglet

from VisibleEntity import *

class AnimatedEntity(VisibleEntity):

  def __init__(self, image, x, y, passable = 1):
    super(AnimatedEntity, self).__init__(image, x, y)
    self.animation_walk = [None, None, None, None]
    self.animation_halt = [None, None, None, None]
    self.animation_attack = [None, None, None, None]
    self.animation_action = [None, None, None, None]
    self.animation_die = [None, None, None, None]

  def animate_walk(self, direction):
    if self.animation_walk[direction]:
      self.image = self.animation_walk[direction]

  def animate_halt(self, direction):
    if self.animation_halt[direction]:
      self.image = self.animation_halt[direction]
      
  def animate_attack(self, direction):
    if self.animation_attack[direction]:
      self.image = self.animation_attack[direction]

  def animate_action(self, direction):
    if self.animation_action[direction]:
      self.image = self.animation_action[direction]

  def animate_die(self, direction):
    if self.animation_die[direction]:
      self.image = self.animation_die[direction]
