from turtle import Turtle

class Score:
    def __init__(self):
        self.SCORES = 0
        self.show_score()


    def show_score(self):
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(-550, 360)
        self.score.color('green')
        self.score.write(f"SCORE: {self.SCORES}", font=('Arial', 18, 'bold'))
        return self.score


    def reset_score(self):
        self.score.clear()
        self.SCORES+=10
        self.show_score()


