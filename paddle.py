from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, positon):
        super().__init__()
        self.position = positon
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(positon)

    def paddle_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)
