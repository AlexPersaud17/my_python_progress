import turtle

tess = turtle.Turtle()
petals = eval(input("How many petals? "))
petal_color = input("What color do you want to paint them? ")
turn_angle = 360 / petals


# print one petal of the flower
# tess.forward(100)
# tess.left(45)
# tess.forward(100)
# tess.left(135)
# tess.forward(100)
# tess.left(45)
# tess.forward(100)
# tess.left(135)

for count in range(petals):
  tess.fillcolor(petal_color)
  tess.begin_fill()
  for angle in [45, 135, 45, 135]:
    tess.forward(100)
    tess.left(angle)
  tess.left(turn_angle)
  tess.end_fill()
    

tess.hideturtle()


