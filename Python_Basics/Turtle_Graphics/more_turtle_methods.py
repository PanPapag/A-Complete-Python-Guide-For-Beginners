import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()               # lift the pen so to print only the stamps of turtle

for _ in range(30):
    tess.stamp()        # leave an impression on the canvas
    tess.forward(dist)
    tess.right(24)
    dist = dist + 2

wn.exitonclick()
