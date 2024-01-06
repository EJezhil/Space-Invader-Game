import time
from turtle import Turtle

class Enemy:
    def __init__(self):
        self.enemy = None
        self.enemies = []
        self.x = -400
        self.y = 300
        self.enemy_bullet_list = []
        self.move = 10

    def create_enemies(self):
        for i in range(24):
            self.enemy = Turtle(shape="turtle")
            self.enemy.penup()
            self.enemy.color("red")
            self.enemy.shapesize(stretch_len=2, stretch_wid=2)
            self.enemy.setheading(270)
            self.enemies.append(self.enemy)

        # move enemy
        for i in self.enemies:
            i.goto(self.x, self.y)
            self.x += 70
            if i.xcor() > 350:
                self.x = -400
                self.y += -50
    
    def create_enemy_bullet(self):
        for i in self.enemies[:16:2]:
            self.enemy_bullet = Turtle()
            self.enemy_bullet.penup()
            self.enemy_bullet.shape("arrow")
            self.enemy_bullet.color("red")
            self.enemy_bullet.shapesize(stretch_len=0.4)
            self.enemy_bullet_list.append(self.enemy_bullet)
            self.enemy_bullet.goto(i.xcor(), i.ycor())

    def move_enemy_bullet(self):
        for i in self.enemy_bullet_list:
            i.goto(i.xcor(),i.ycor()-40)

    def create_enemy_bullet_again(self):
        len_enemies = len(self.enemies)
        len_enemy_bullets = len(self.enemy_bullet_list)

        # print(len_enemies)
        # print(len_enemy_bullets)
        if len_enemies > len_enemy_bullets:
            for i in range(0,len(self.enemy_bullet_list)):
                if self.enemy_bullet_list[i].ycor() <-600:
                        self.enemy_bullet_list[i].goto(self.enemies[i].xcor(), self.enemies[i].ycor())
        else:
            for i in range(0,len(self.enemies)):
                if self.enemy_bullet_list[i].ycor() <-600:
                        self.enemy_bullet_list[i].goto(self.enemies[i].xcor(), self.enemies[i].ycor())
            # print("limit exceed")



    def enemy_move(self):
        for i in self.enemies:
            i.goto(i.xcor()+self.move,i.ycor())
            if i.xcor() > 590:
                i.goto(590,i.ycor())
                self.move=-10
            if i.xcor() < -590:
                i.goto(-590, i.ycor())
                self.move = 10

    #
    # def create_enemy_bullet_one(self,pos):
    #     self.enemy_bullet = Turtle()
    #     self.enemy_bullet.penup()
    #     self.enemy_bullet.shape("arrow")
    #     self.enemy_bullet.color("black")
    #     self.enemy_bullet.shapesize(stretch_len=0.4)
    #     self.enemy_bullet_list.append(self.enemy_bullet)
    #     self.enemy_bullet.goto(pos, self.enemy.ycor())