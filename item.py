import pyglet

from definitions import *

class Inventory_Item(pyglet.sprite.Sprite):
    
    item_type = -1
    
    def __init__(self, image, item_type):
        super(Item, self).__init__(image)
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

class Item(VisibleItem):

    item_type = -1

    def __init__(self, image, tile, item_type):
        super(Item, self).__init__(image, tile.x, tile.y)
        self.item_type = item_type
