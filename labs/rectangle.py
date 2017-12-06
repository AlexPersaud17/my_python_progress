# Draws a simple rectangle

# 1. Run once to see the result of this code
# 2. Update the code following the steps below:
#    a. change the sequential code to a for-loop
#       that draws two-sides in each iteration
#    b. change the pensize from the default value to 10
#    c. change the pencolor to one of the valid colors shown here:
#       https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
#    d. change the fillcolor to one of the valid colors shown above.
#    e. update the code to ask the user for the 2 dimensions of the rectangle

import turtle
user_width = eval(input("Enter your desired width: "))
user_height = eval(input("Enter your desired height: "))
tess = turtle.Turtle()
tess.shape("turtle")

# Step (a): update the sequential code with a for-loop
tess.pencolor("red")
tess.pensize(10)
for length in [user_width, user_height, user_width, user_height]:
        tess.forward(length)
        tess.right(90)

tess.hideturtle()
