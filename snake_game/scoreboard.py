from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        file = open("/Users/andre/Desktop/data.txt", "r")
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center",
                   font=("Courier", 16, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("/Users/andre/Desktop/data.txt", "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
