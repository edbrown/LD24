import pyglet

from definitions import *
from AnimatedEntity import *

class InventoryItem(pyglet.sprite.Sprite):
    
    item_type = -1
    
    def __init__(self, image, item_type):
        super(InventoryItem, self).__init__(image)
        self.item_type = item_type
        self.scale = 0.5

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

    def __init__(self, image, tile, item_type, item_holder, item_direction = -1):
        super(Item, self).__init__(image, tile.grid_x, tile.grid_y)
        self.type = item_type
        self.holder = item_holder
        self.direction = item_direction
        self.tile = tile
        
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
