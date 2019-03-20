import turtle

wn = turtle.Screen()

pentagon = turtle.Turtle()
pentagon.pensize(2)

for _ in range(5):
    pentagon.forward(50)
    pentagon.left(72)

wn.exitonclick()
