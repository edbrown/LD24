import pyglet

from definitions import *
from VisibleEntity import *

class Inventory_Item(pyglet.sprite.Sprite):
    
    item_type = -1
    
    def __init__(self, image, item_type):
        super(Item, self).__init__(image, x, y)
        self.item_type = item_type

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

class Item(VisibleEntity):

    item_type = -1
    item_holder = -1

    def __init__(self, image, tile, item_type = ITEM_FOOD, item_holder = ITEM_LOCATION_FLOOR):
        super(Item, self).__init__(image, tile.grid_x, tile.grid_y)
        self.item_type = item_type
        self.item_holder = item_holder

    def is_floor_item(self):
        return self.item_holder == ITEM_LOCATION_FLOOR

    def is_chest_item(self):
        return self.item_holder == ITEM_LOCATION_CHEST
