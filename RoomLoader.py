import pyglet

import * from Room

class RoomLoader:

  @staticmethod
  def get_room(num):
    filename = 'resources/rooms/room_{0}.cfg'.format(num)
    f = open(filename, 'r')

    if f:
      for line in f:
        values = line.split(',')
        for int(value) in values:
          
        
