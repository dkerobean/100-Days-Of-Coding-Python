from turtle import Turtle, Screen
import random
import turtle as t

timmy = Turtle()
timmy.shape("turtle")
#timmy.color("red")

t.colormode(255)

def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#colors = ["red", "blue", "black", "green", "indigo", "yellow", "seagreen", "orange"]
directions = [0, 90, 180, 270]
#timmy.pensize(10)
timmy.speed("fastest")

# #drawsquare
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#
#
# #draw dashed line
#
# for _ in range(10):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.forward(50)
#     timmy.pendown()


#
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for i in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(i)


#random walk

# for _ in range(400):
#     timmy.color(colors())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(20)



#spiral graph


def draw_circle(size):
    for _ in range(int(360 / size) ):
        timmy.color(colors())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size)

draw_circle(6)














screen = Screen()
screen.exitonclick()

