import turtle           # allows us to use turtle library
wn = turtle.Screen()    # creates a graphic window
wn.bgcolor("black")

alex = turtle.Turtle()  # creates a turtle named alex
alex.color("blue")      # make alex blue
alex.pensize(3)         # set the width of alex pen to 3

alex.forward(150)       # tell alex to go forward by 150 units
alex.left(90)           # turn by 90 degrees
alex.forward(75)        # continue forward by 75 units
alex.left(90)           # turn by 90 degrees
alex.forward(150)       # continue forward by 150 units
alex.left(90)           # turn by 90 degrees
alex.forward(75)        # continue forward by 75 units

wn.exitonclick()
