import pyglet

from definitions import *

class Inventory(pyglet.sprite.Sprite):
    
    items = []
    
    def __init__(self, image):
        super(Inventory, self).__init__(image)
        self.x = 0
        self.y = 0
        self.init_x = 0
        self.init_y = 0

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, index):
        return self.items.remove(item)
   
    def item_count(self, item):
        return items.count(item)

    def show(self):
        self.image.blit(self.x, self.y)

    def update(self, offset_x, offset_y):
        self.x = self.init_x - offset_x
        self.y = self.init_y - offset_y
        self.show()
        
        x = 14 - offset_x
        y = 113 - offset_y
        no = 0
        for item in self.items:
            item.show(x, y)
            x += 35
            no += 1
            
            if (no % 6) == 0: 
                y -= 20
                x = 14 - offset_x

            
