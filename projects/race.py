#This program creates 4 turtles that race towards the finish line
import turtle
import random
def main():
  turtle.setup(500, 400) 

  leo = turtle.Turtle()
  donnie = turtle.Turtle()
  mikey = turtle.Turtle()
  raph = turtle.Turtle()

  leo_dist = 0
  donnie_dist = 0
  mikey_dist = 0
  raph_dist = 0

  y_pos = 100

  for ninja in [[leo, "blue"], [donnie, "purple"], [mikey, "orange"], [raph, "red"]]:
    ninja[0].penup()
    ninja[0].shape("turtle")
    ninja[0].fillcolor(ninja[1])
    ninja[0].goto(-300, y_pos)
    y_pos -= 50

  while leo_dist <= 500 and donnie_dist <= 500 and mikey_dist <= 500 and raph_dist <= 500:
    go_forward = random.randint(20, 50)
    leo.forward(go_forward)
    leo_dist += go_forward

    go_forward = random.randint(20, 50)
    donnie.forward(go_forward)
    donnie_dist += go_forward

    go_forward = random.randint(20, 50)
    mikey.forward(go_forward)
    mikey_dist += go_forward

    go_forward = random.randint(20, 50)
    raph.forward(go_forward)
    raph_dist += go_forward

  if leo_dist >= 500:
    winning_ninja = "Leo"
  elif donnie_dist >= 500:
    winning_ninja = "Donnie"
  elif mikey_dist >= 500:
    winning_ninja = "Mikey"
  elif raph_dist >= 500:
    winning_ninja = "Raph"
  

  winner = turtle.Turtle()
  winner.penup()
  winner.goto(-100, -125)
  winner.write("Ladies and Gentlemen we have winner!")
  winner.goto(-100, -150)
  winner.write(winning_ninja + " you are the ultimate winner of the race!")
  winner.hideturtle()
  
  turtle.done()
main()