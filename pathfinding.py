import math
from definitions import *

class AStar:
    
    def __init__(self, m):
        self.map = m

    def calcShortest(self, start, end):
        open_list = [ start ]
        closed = []

        while len(open_list):
            current = self.get_minimum(open_list)

            if current == None:
                return None
            
            if current == end:
                return self.reconstruct(start, end)
            else:
                closed.append(current)
                open_list.remove(current)
                adj = self.map.get_adjacent(current)
                for a in adj:
                    
                    if closed.count(a):
                        continue
                    temp_g = current.g + self.distance(a, current)
                    
                    if open_list.count(a) == 0 or temp_g < a.g:
                        if open_list.count(a) == 0:
                            open_list.append(a)
                        a.parent = current
                        a.g = temp_g
                        a.f = a.g + self.distance(a, end)

    def reconstruct(self, start, end):
        path = []
        current = end
        while current != start:
            path.append(current)
            current = current.parent

        path.append(start)
        return path

    def get_minimum(self, elems):
        if len(elems) > 0:
            minimum = None

            for n in elems:

                if minimum == None:
                    if n.is_passable():
                        minimum = n
                else:
                    if n.f < minimum.f and n.is_passable():
                        minimum = n

            return minimum
        
        return None
                
    def distance(self, one, two):
        return math.sqrt(math.pow(one.x - two.x, 2) + math.pow(one.y - two.y, 2))
