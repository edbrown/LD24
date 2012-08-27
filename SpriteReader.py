import pyglet
from pyglet.image import *

from definitions import *

class SpriteReader():

    out_tiles = None
    in_tiles = None
    walls = None
    demon = None
    tombwoof = None
    chest = None
    item = None
    player = None
    enemy = None
    npc = None
    
        
    @staticmethod
    def load_all():
      self.out_tiles = ImageGrid(load("resources/tiles.png"), 16, 2, TILE_WIDTH, TILE_HEIGHT)
      self.out_tiles = TextureGrid(self.out_tiles)

      self.in_tiles = ImageGrid(load("resources/indoor_tiles.png"), 5, 4, TILE_WIDTH, TILE_HEIGHT)
      self.in_tiles = TextureGrid(self.in_tiles)

      self.walls = ImageGrid(load("resources/dungeon_walls.png"), 8, 4, WALL_WIDTH, WALL_HEIGHT)
      self.walls = TextureGrid(self.walls)

      self.demon = ImageGrid(load("resources/demon.png"), 1, 1, 413, 606)
      self.demon = TextureGrid(self.demon)

      self.tombwoof = ImageGrid(load("resources/tombwoof.png"), 2, 2, 96, 96)
      self.tombwoof = TextureGrid(self.tombwoof)

      self.chest = ImageGrid(load("resources/chest.png"), 4, 4, TILE_WIDTH, TILE_WIDTH)
      self.chest = TextureGrid(self.chest)

      self.item = self.chest

      self.player = ImageGrid(pyglet.image.load("resources/minotaur.png"), 8, 24, 128, 128)
      self.player = TextureGrid(self.player)
      
      self.enemy = self.player
      
      self.npc = self.player
