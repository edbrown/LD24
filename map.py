import pyglet

from tile import *
from Player import *
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

    self.items = []
    chest = pyglet.image.ImageGrid(pyglet.image.load("resources/chest.png"), 4, 4, TILE_WIDTH, TILE_WIDTH)
    chest_grid = pyglet.image.TextureGrid(chest)
    item = Item(chest_grid[0,0], self.tiles[3], ITEM_FOOD, ITEM_LOCATION_CHEST, NORTH)
    self.items.append(item)
    self.tiles[3].add_item(item)
    
    item = Item(chest_grid[0,0], self.tiles[4], ITEM_FOOD, ITEM_LOCATION_CHEST, NORTH)
    self.items.append(item)
    self.tiles[4].add_item(item)

    item = Item(chest_grid[1,0], self.tiles[12], ITEM_FOOD, ITEM_LOCATION_FLOOR, SOUTH)
    self.items.append(item)
    self.tiles[12].add_item(item)
    
  def draw(self):
    for tile in self.tiles:
      tile.draw()
    for item in self.items:
      item.draw()

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
