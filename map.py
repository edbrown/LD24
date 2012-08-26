import pyglet

from tile import *
from unit import *
from definitions import *
from item import *

class Map():
  def __init__(self, data):
    self.data = data;
    self.grid = pyglet.image.ImageGrid(pyglet.image.load("resources/tiles.png"), 16, 2, TILE_WIDTH, TILE_HEIGHT)
    self.grid = pyglet.image.TextureGrid(self.grid)
    self.tiles = []
    for i in range(len(self.data)):
      for j in range(len(self.data[i])):
        if(self.data[i][j] == PASSABLE):
          type = self.grid[1,0]
        else:
          type = self.grid[0,0]
        self.tiles.append(Tile(type, i, j, self.data[i][j]))
    self.unit = Unit(self.grid[2,1], 0, 0)
    
    minotaur = pyglet.image.ImageGrid(pyglet.image.load("resources/minotaur.png"), 8, 24, 128, 128)

    minotaur_grid = pyglet.image.TextureGrid(minotaur)
    walking_north = [minotaur_grid[4,4], minotaur_grid[4,5], minotaur_grid[4,6], minotaur_grid[4,7], minotaur_grid[4,8], minotaur_grid[4,9], minotaur_grid[4,10], minotaur_grid[4,11]]
    walking_south = [minotaur_grid[0,4], minotaur_grid[0,5], minotaur_grid[0,6], minotaur_grid[0,7], minotaur_grid[0,8], minotaur_grid[0,9], minotaur_grid[0,10], minotaur_grid[0,11]]
    walking_east = [minotaur_grid[6,4], minotaur_grid[6,5], minotaur_grid[6,6], minotaur_grid[6,7], minotaur_grid[6,8], minotaur_grid[6,9], minotaur_grid[6,10], minotaur_grid[6,11]]
    walking_west = [minotaur_grid[2,4], minotaur_grid[2,5], minotaur_grid[2,6], minotaur_grid[2,7], minotaur_grid[2,8], minotaur_grid[2,9], minotaur_grid[2,10], minotaur_grid[2,11]]
    animation_north = pyglet.image.Animation.from_image_sequence(walking_north, 0.1)
    animation_south = pyglet.image.Animation.from_image_sequence(walking_south, 0.1)
    animation_east = pyglet.image.Animation.from_image_sequence(walking_east, 0.1)
    animation_west = pyglet.image.Animation.from_image_sequence(walking_west, 0.1)
    self.unit.set_animation(animation_north, animation_south, animation_east, animation_west)
    self.chests = []
    
    chest = pyglet.image.ImageGrid(pyglet.image.load("resources/chest.png"), 4, 4, TILE_WIDTH, TILE_WIDTH)
    chest_grid = pyglet.image.TextureGrid(chest)
    item = Item(chest_grid[0,0], self.tiles[3], ITEM_FOOD, ITEM_LOCATION_CHEST, NORTH)
    self.chests.append(item)
    self.tiles[3].add_item(item)

    item = Item(chest_grid[1,0], self.tiles[12], ITEM_FOOD, ITEM_LOCATION_FLOOR, WEST)
    self.chests.append(item)
    self.tiles[12].add_item(item)
    
  def draw(self):
    for tile in self.tiles:
      tile.draw()
    for chest in self.chests:
      chest.draw()
    self.unit.draw()

  def get_tile(self, x, y):
    for tile in self.tiles: 
      if tile.grid_x == x and tile.grid_y == y:
        return tile
    
    return None

  def get_adjacent(self, tile):
    
    adj = []
    if tile.grid_x > 0:
      adj.append(self.get_tile(tile.grid_x - 1, tile.grid_y))

    if tile.grid_y > 0:
      adj.append(self.get_tile(tile.grid_x, tile.grid_y - 1))

    if tile.grid_x < (len(self.data) - 1):
      adj.append(self.get_tile(tile.grid_x + 1, tile.grid_y))

    if tile.grid_y < (len(self.data[0]) - 1):
      adj.append(self.get_tile(tile.grid_x, tile.grid_y + 1))
      
    return adj
