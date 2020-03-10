import turtle

pirate_path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

screen = turtle.Screen()
pirate = turtle.Turtle()

for (angle, steps) in pirate_path:
    pirate.left(angle)
    pirate.forward(steps)

screen.exitonclick()
