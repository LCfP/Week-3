import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

side_length = 400
tess.left(36)
tess.hideturtle()
for _ in range(5):
    tess.forward(side_length)
    tess.left(144)

screen.exitonclick()
