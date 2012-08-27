import pyglet

from definitions import *
from AnimationBuilder import *
from AnimatedEntity import *

class InventoryItem(VisibleEntity):
    
    item_type = -1
    
    def __init__(self, i, image, item_type):
        super(InventoryItem, self).__init__(image, 0, 0)
        self.item_type = item_type
        self.scale = 0.5
        self.id = i

    def __cmp__(self, other):
        return cmp(self.id, other.id)

    def is_food(self):
        return self.item_type == ITEM_FOOD

    def is_potion(self):
        return self.item_type == ITEM_POTION

    def action(self, unit):
        if self.is_food():
            pass
        elif self.is_potion():
            unit.change_health(+30)
        else:
            print "ERROR: Item type not recognised"

    def show(self, x, y):
        self.x = x
        self.y = y
        self.draw()

class Item(AnimatedEntity):

    def __init__(self, i, image, tile, item_type, item_holder, item_direction = -1):
        super(Item, self).__init__(image, tile.grid_x, tile.grid_y)
        self.type = item_type
        self.holder = item_holder
        self.direction = item_direction
        self.tile = tile
        self.id = i

    def create_animations(self):
      sprite_sheet = pyglet.image.ImageGrid(pyglet.image.load("resources/chest.png"), 4, 4, TILE_WIDTH, TILE_WIDTH)
      grid = pyglet.image.TextureGrid(sprite_sheet)
      print "Direction"
      print self.direction
      self.animation_action = [
        AnimationBuilder.build(grid, 2, 0, 3),
        AnimationBuilder.build(grid, 0, 0, 3),
        AnimationBuilder.build(grid, 1, 0, 3),
        AnimationBuilder.build(grid, 3, 0, 3)
      ]
      self.animation_halt = [
        AnimationBuilder.build(grid, 2, 0, 1),
        AnimationBuilder.build(grid, 0, 0, 1),
        AnimationBuilder.build(grid, 1, 0, 1),
        AnimationBuilder.build(grid, 3, 0, 1)
      ]
      self.animate_halt(self.direction)
        
    def is_floor_item(self):
        return self.holder == ITEM_LOCATION_FLOOR

    def is_chest_item(self):
        return self.holder == ITEM_LOCATION_CHEST

    def is_food(self):
        return self.type == ITEM_FOOD

    def is_potion(self):
        return self.type == ITEM_POTION

    def get_direction(self):
        return self.direction

    def get_item_move_loc(self):
        if self.is_chest_item():
            if self.direction == NORTH:
                return [self.tile.grid_x, self.tile.grid_y + 1]
            elif self.direction == SOUTH:
                return [self.tile.grid_x, self.tile.grid_y - 1]
            elif self.direction == EAST:
                return [self.tile.grid_x + 1, self.tile.grid_y]
            else:
                return [self.tile.grid_x - 1, self.tile.grid_y]

        return  [self.tile.grid_x, self.tile.grid_y]



