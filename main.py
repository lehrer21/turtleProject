import turtle as turtle_module
import random

turtle_module.colormode(255)
my_turtle = turtle_module.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
color_list = [(240, 242, 247), (203, 157, 117), (58, 96, 133)]
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()