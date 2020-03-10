import turtle

screen = turtle.Screen()

hour_turtle = turtle.Turtle()
hour_turtle.shape("turtle")
# the next line causes my turtle to end in the "wrong" position
# I like it better to start at the top though
hour_turtle.left(90)
hour_turtle.penup()

for hour in range(12):
    hour_turtle.forward(200)
    hour_turtle.pendown()
    hour_turtle.forward(25)
    hour_turtle.penup()
    hour_turtle.forward(25)
    hour_turtle.stamp()
    hour_turtle.setposition(0, 0)
    hour_turtle.right(30)

screen.exitonclick()
