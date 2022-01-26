from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="Which Turtle will win the race? Enter a color: ")
print(user_bet)
colors=["blue","red","green","yellow"]
y_pos=[-60,-20,20,60]
all_Turtle=[]

for Turtle in range(0,4):
    new_Turtle=Turtle(shape="Turtle")
    new_Turtle.color(colors[Turtle])
    new_Turtle.penup()
    new_Turtle.goto(x=-220,y=y_pos[Turtle])
    all_Turtle.append(new_Turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for Turtle in all_Turtle:
        if Turtle.xcor()>230:
            is_race_on=False
            winning_color=Turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} Turtle is the winner.")
            else:
                print(f"You Lost! The {winning_color} Turtle is the winner.")
        rand_dist=random.randint(0,10)
        Turtle.forward(rand_dist)

screen.exitonclick()