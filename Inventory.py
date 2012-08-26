import pyglet

from definitions import *

class Inventory(pyglet.sprite.Sprite):
    
    items = []
    
    def __init__(self, image):
        super(Inventory, self).__init__(image)

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, index):
        return self.items.remove(item)
   
    def item_count(self, item):
        return items.count(item)

    def show(self):
        self.image.blit(0, 0)

    def update(self):
        self.show()
        x = 14
        y = 113
        no = 0
        for item in self.items:
            item.show(x, y)
            x += 35
            no += 1
            
            if (no % 6) == 0: 
                y -= 20
                x = 14

            
