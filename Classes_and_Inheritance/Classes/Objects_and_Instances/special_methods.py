class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __sub__(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y)

p1 = Point(7,6)
print(p1)

p2 = Point(1,5)
print(p2)

print(p1 + p2)
print(p1 - p2)
