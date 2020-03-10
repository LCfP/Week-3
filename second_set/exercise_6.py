import turtle

drunk_angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

screen = turtle.Screen()
pirate = turtle.Turtle()

for angle in drunk_angles:
    pirate.left(angle)      # positive angles are counter-clockwise i.e. left
    pirate.forward(100)     # 100 steps forward

screen.exitonclick()
