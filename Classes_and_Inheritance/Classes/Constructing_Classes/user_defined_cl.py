class Point():
    # each method has at least self argument
    def getX(self):
        return self.x

# Create instances of class Point
point1 = Point()
point2 = Point()

print(point1)
print(point2)
print(point1 is point2)

point1.x = 5
point2.x = 10
print(point1.getX())
print(point2.getX())
