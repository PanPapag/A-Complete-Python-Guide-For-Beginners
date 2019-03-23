class Point():
    # each method has at least self argument
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

# Create instances of class Point
point1 = Point(5,10)
point2 = Point(1,2)

print("point1 ({}, {})" .format(point1.getX(),point1.getY()))
print("point2 ({}, {})" .format(point2.getX(),point2.getY()))
