from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("snake_data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()
        print(self.high_score)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("snake_data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(str(self.score))

        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER 😔: ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()