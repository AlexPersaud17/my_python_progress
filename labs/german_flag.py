import turtle

tess = turtle.Turtle()
tess.shape("turtle")

y_position = 0
for color in ["black", "red", "yellow"]:
    y_position -= 30

    tess.pencolor(color)
    tess.fillcolor(color)
    tess.begin_fill()

    for length in [150, 30, 150, 30]:
        tess.forward(length)
        tess.right(90)
        
    tess.end_fill()

    tess.goto(0, y_position)

tess.up()
tess.goto(0, -150)
tess.pencolor("red")
tess.write("Flag of Germany", font=("Arial", 15, "bold"))


tess.hideturtle()
