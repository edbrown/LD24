import pyglet
from Player import *
from ActionEntity import *
from definitions import *
from AnimationBuilder import *
from Message import *
from TaskQueue import *
import random

class Enemy(ActionEntity):
  
  def __init__(self, game, image, tile):
    super(Enemy, self).__init__(game, image, tile.grid_x, tile.grid_y)
    self.tile = tile
    self.tile.add_person(self)
    self.health = 50
    self.next_move = tile
    self.game = game
    self.scale = 0.5
    self.speed = 0.5
    self.under_attack = False
    self.damage = 5

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
      AnimationBuilder.build(grid, 4, 18, 23, loop=False),
      AnimationBuilder.build(grid, 0, 18, 23, loop=False),
      AnimationBuilder.build(grid, 6, 18, 23, loop=False),
      AnimationBuilder.build(grid, 2, 18, 23, loop=False)
    ]

    self.animate_halt(NORTH)

  def calculate_next_move(self):
    adj = self.game.map.get_adjacent(self.tile)
    index = random.randint(0,3)
    
    while index >= len(adj) or adj[index] == None or not adj[index].is_passable():
      index = random.randint(0,3)

    for tile in adj:
      if self.under_attack and type(tile.person) == Player:
        return
    self.next_move = adj[index]

  def die(self):
    self.animate_death(self.direction)
    self.tile.person = None
