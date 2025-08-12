from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(x_coordinate, y_coordinate)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 250:
            y_coordinate = self.ycor() + 20
            self.goto(self.xcor(), y_coordinate)

    def down(self):
        if self.ycor() > -230:
            y_coordinate = self.ycor() - 20
            self.goto(self.xcor(), y_coordinate)
