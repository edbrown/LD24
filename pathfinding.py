import math

class AStar:
    
    def __init__(self, m):
        self.map = m

    def calcShortest(self, start, end):
        open_list = [ start ]
        closed = []
        done = False

        while not done:
            current = self.get_minimum(open_list)

            if current == end:
                end.parent = current
                done = True
            else:
                closed.append(current)
                open_list.remove(current)
                adj = self.map.get_adjacent(current)
                for a in adj:
                    if closed.count(a) != 0 and current.g < a.g:
                        a.g = current.g + self.distance(a, current)
                        a.parent = current
                    elif open_list.count(a) !=  0 and current.g < a.g:
                        a.g = current.g + self.distance(a, current)
                        a.parent = current
                    else:
                        open_list.append(a)
                        a.g = 10000000
                        
        return self.reconstruct(start, end)

    def reconstruct(self, start, end):
        path = []
        current = end
        while current != start:
            current = current.parent
            path.append(current)

        return path

    def get_minimum(self, elems):
        if len(elems) > 0:
            minimum = elems[0]

            for n in elems:
                if n.f < minimum.f:
                    minimum = n

            return minimum
        
        return None
                
    def distance(self, one, two):
        return math.sqrt(math.pow(one.x - two.x, 2) + math.pow(one.y - two.y, 2))
