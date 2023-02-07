from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segment.append(tim)

    def move(self):
        for num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[num - 1].xcor()
            new_y = self.segment[num - 1].ycor()
            self.segment[num].goto(new_x, new_y)

        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading() != LEFT:
            self.head.setheading(RIGHT)




