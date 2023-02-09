from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self._snake_body = []
        self.create_snake()
        self._direction = "Right"

    def get_head(self):
        return self._snake_body[0]

    def get_body(self):
        return self._snake_body

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self._snake_body) - 1, 0, -1):
            new_x = self._snake_body[seg_num - 1].xcor()
            new_y = self._snake_body[seg_num - 1].ycor()
            self._snake_body[seg_num].goto(new_x, new_y)
        self._snake_body[0].forward(20)

    def up(self):
        if self._direction == "Right":
            self._snake_body[0].right(270)
        if self._direction == "Left":
            self._snake_body[0].right(90)
        self._direction = "Up"

    def left(self):
        if self._direction == "Up":
            self._snake_body[0].right(270)
        if self._direction == "Down":
            self._snake_body[0].right(90)
        self._direction = "Left"

    def down(self):
        if self._direction == "Right":
            self._snake_body[0].right(90)
        if self._direction == "Left":
            self._snake_body[0].right(270)
        self._direction = "Down"

    def right(self):
        if self._direction == "Up":
            self._snake_body[0].right(90)
        if self._direction == "Down":
            self._snake_body[0].right(270)
        self._direction = "Right"

    def add_segment(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self._snake_body.append(new_part)

    def extend(self):
        self.add_segment(self._snake_body[-1].position())

    def reset(self):
        for seg in self._snake_body:
            seg.goto(1000, 1000)
        self._snake_body.clear()
        self.create_snake()
        self._direction = "Right"

