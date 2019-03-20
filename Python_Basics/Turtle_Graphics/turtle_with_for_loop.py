import turtle

wn = turtle.Screen()
elan = turtle.Turtle()

distance = 50
angle = 90
times = 15

for _ in range(times):
    elan.forward(distance)
    elan.right(angle)
    distance += 10
    angle -= 3

wn.exitonclick()
