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
print("point2 ({}, {})" .format(point1.getX(),point1.getY()))

# EX : Create a class called Animal that accepts two numbers as inputs and
#      assigns them respectively to two instance variables: arms and legs.
#      Create an instance method called limbs that, when called, returns the
#      total number of limbs the animal has. To the variable name spider,
#      assign an instance of Animal that has 4 arms and 4 legs.
#      Call the limbs method on the spider instance and save the result to the
#      variable name spidlimbs.

class Animal():
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
    def limbs(self):
        return self.arms + self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
