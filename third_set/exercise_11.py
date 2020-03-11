import turtle

house_path = [(0, 200), (90, 200), (90, 200), (-135, 141), (-90, 141), (-90, 283), (-135, 200), (-135, 283)]

screen = turtle.Screen()
bob = turtle.Turtle()       # the builder

for (angle, steps) in house_path:
    bob.left(angle)
    bob.forward(steps)

screen.exitonclick()
