from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",15,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",False,align=ALIGNMENT,font=FONT)
        self.hideturtle()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",ALIGNMENT,FONT)
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",False,align=ALIGNMENT,font=FONT)

