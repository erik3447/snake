from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 23, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        with open("highscore.txt") as scorefile:
            self.high_score = int(scorefile.readline())
        self.update_scoreboard()

    def new_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as scorefile:
                scorefile.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
    def score_refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
