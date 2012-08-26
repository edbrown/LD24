import pyglet

from definitions import *

class Inventory(pyglet.sprite.Sprite):
    
    items = []
    
    def __init__(self, image, x, y):
        super(Item, self).__init__(image, x, y)

    def add_item(item):
        return self.items.append(item)

    def remove_item(self, index):
        return self.items.remove(item)
   
    def item_count(self, item):
        return items.count(item)
