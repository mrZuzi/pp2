import math
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y


    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
