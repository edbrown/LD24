import pyglet
from ActionEntity import *
from definitions import *
from AnimationBuilder import *
from Message import *
from TaskQueue import *

class NPC(ActionEntity):
  
  def __init__(self, image, tile):
    super(NPC, self).__init__(image, tile.grid_x, tile.grid_y)
    self.tile = tile
    self.tile.add_person(self)

  def create_animations(self):
    sprite_sheet = pyglet.image.ImageGrid(pyglet.image.load("resources/minotaur.png"), 8, 24, 128, 128)
    grid = pyglet.image.TextureGrid(sprite_sheet)
    self.animation_halt = [
      AnimationBuilder.build(grid, 4, 0, 3),
      AnimationBuilder.build(grid, 0, 0, 3),
      AnimationBuilder.build(grid, 6, 0, 3),
      AnimationBuilder.build(grid, 2, 0, 3)
    ]
    self.animate_halt(SOUTH)

  def speak(self):
    return Message(["Test action message"])


