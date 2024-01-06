from turtle import Turtle

class Shield:
    def __init__(self):
        self.block = None
        self.blocks = []
        self.x = -550
        self.y = -140

    def create_blocks(self):
        for i in range(34):
            self.block = Turtle(shape="square")
            self.block.penup()
            self.block.color("green")
            self.block.shapesize(stretch_len=2, stretch_wid=2)
            self.blocks.append(self.block)

        # move block
        for i in self.blocks:
            i.goto(self.x, self.y)
            self.x += 70
            if i.xcor() > 500:
                self.x = -550
                self.y += -50