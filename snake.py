from idlelib.config_key import MOVE_KEYS
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)
    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.segment.append(snake)
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(180)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(0)

    def eat_Tails(self):
        self.tails = self.segment[1:]
        for tail in self.tails:
            if self.head.distance(tail) < 10:  # Si la distance est inférieure à 10, cela signifie une collision
                return True
        return False