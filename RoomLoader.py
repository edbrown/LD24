import pyglet
import * from pyglet.image

import * from Room

class RoomLoader:

  @staticmethod
  def get_room(num):
    filename = 'resources/rooms/room_{0}.cfg'.format(num)
    f = open(filename, 'r')

    if f:
      room = Room()
      for line in f:
        values = line.split(',')
        for value in values:
          val =  int(value)
          if val > WALL_NORTH and val < WALL_BLOOD_EAST
        
