import turtle
import random
tess = turtle.Turtle()

petals = eval(input("How many petals? "))

turn_angle = 360 / petals

turtle.colormode(255)


for count in range(petals):
    tess.fillcolor(random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
    tess.begin_fill()
    for angle in [45, 135, 45, 135]:
        tess.forward(100)
        tess.left(angle)
    tess.left(turn_angle)
    tess.end_fill()

tess.hideturtle()

