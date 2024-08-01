from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.random_list_of_x_moves = [10,-10]
        self.random_list_of_y_moves = [10,-10]
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = random.choice(self.random_list_of_x_moves)
        self.y_move = random.choice(self.random_list_of_y_moves)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def go_to_start(self):
        self.goto(0, 0)

