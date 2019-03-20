import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(5)

alex = turtle.Turtle()
alex.pensize(5)
alex.color("hotpink")

# tess creates a triangle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)

alex.forward(40)
alex.left(90)
alex.forward(math.sqrt(4800))
alex.left(90)
alex.forward(40)
alex.left(90)
alex.forward(math.sqrt(4800))


wn.exitonclick()
