import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

side_length = 50

# equilateral triangle
for _ in range(3):
    tess.forward(side_length)
    tess.left(120)

screen.exitonclick()
