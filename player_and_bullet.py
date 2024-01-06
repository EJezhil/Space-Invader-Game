import time
from turtle import Turtle


class PlayerBullet:
    bullet_list = []

    def __init__(self):
        self.player_x = None
        self.player_y = None

    def left(self):
        self.player_x = self.player.xcor()
        self.player_y = self.player.ycor()
        self.player.goto(self.player_x - 20, self.player_y)

    def right(self):
        self.player_x = self.player.xcor()
        self.player_y = self.player.ycor()
        self.player.goto(self.player_x + 20, self.player_y)

    def create_player(self):
        self.player = Turtle()
        self.player.penup()
        self.player.shape("triangle")
        self.player.color("blue")
        self.player.goto(0, -360)
        self.player.shapesize(stretch_len=2.5, stretch_wid=2.5)
        self.player.setheading(90)

    def create_player_bullet(self):
        self.player_bullet = Turtle()
        self.player_bullet.penup()
        self.player_bullet.shape("arrow")
        self.player_bullet.color("orange")
        self.player_bullet.shapesize(stretch_len=0.4)
        self.bullet_list.append(self.player_bullet)

        self.player_x = self.player.xcor()
        self.player_y = self.player.ycor()
        self.player_bullet.goto(self.player_x, self.player_y)

    def move_player_bullet(self):
        for i in self.bullet_list:
            i.goto(i.xcor(),i.ycor()+40)

    def boundry_check(self):
        if self.player.xcor() > 590:
            self.player.goto(590,self.player.ycor())
        if self.player.xcor() < -590:
            self.player.goto(-590,self.player.ycor())

