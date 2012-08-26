import pyglet

from VisibleEntity import *

class AnimatedEntity(VisibleEntity):

  def __init__(self, image, x, y, passable = 1):
    super(AnimatedEntity, self).__init__(image, x, y)
