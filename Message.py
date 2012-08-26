import pyglet

class Message(pyglet.text.Label):

  def __init__(self, text_list):
    super(Message, self).__init__()
    self.box_x = 100
    self.box_y = 50
    self.item_number = 0
    self.text_list = text_list
    self.finished = False

  def show(self):
    if not self.finished:
      bg = pyglet.image.load("resources/message.png")
      bg.blit(self.box_x, self.box_y)
      self.text = self.text_list[self.item_number]
      self.width = bg.width - 60
      self.y = self.box_y + bg.height - 40
      self.x = self.box_x + 30
      self.multiline = True
      self.font_size = 10
      self.draw()

  def next(self):
    self.item_number += 1
    if self.item_number >= len(self.text_list):
      self.item_number = 0
      self.finished = True;

