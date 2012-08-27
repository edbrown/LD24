import pyglet
from ActionEntity import *
from definitions import *
from AnimationBuilder import *
from TaskQueue import *
from Inventory import *
from item import *
from pyglet.gl import *

class Player(ActionEntity):
  
  
  def __init__(self, game, image, x = 0, y = 0):
    super(Player, self).__init__(image, x, y)
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
      AnimationBuilder.build(grid, 4, 12, 17),
      AnimationBuilder.build(grid, 0, 12, 17),
      AnimationBuilder.build(grid, 6, 12, 17),
      AnimationBuilder.build(grid, 2, 12, 17)
    ]
    self.animation_die = [
      AnimationBuilder.build(grid, 4, 4, 11),
      AnimationBuilder.build(grid, 0, 4, 11),
      AnimationBuilder.build(grid, 6, 4, 11),
      AnimationBuilder.build(grid, 2, 4, 11)
    ]

    self.animate_halt(self.direction)

