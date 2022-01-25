from paddle import paddle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="Which paddle will win the race? Enter a color: ")
print(user_bet)
colors=["blue","red","green","yellow"]
y_pos=[-60,-20,20,60]
all_paddle=[]

for paddle in range(0,4):
    new_paddle=paddle(shape="paddle")
    new_paddle.color(colors[paddle])
    new_paddle.penup()
    new_paddle.goto(x=-220,y=y_pos[paddle])
    all_paddle.append(new_paddle)

if user_bet:
    is_race_on=True

while is_race_on:
    for paddle in all_paddle:
        if paddle.xcor()>230:
            is_race_on=False
            winning_color=paddle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} paddle is the winner.")
            else:
                print(f"You Lost! The {winning_color} paddle is the winner.")
        rand_dist=random.randint(0,10)
        paddle.forward(rand_dist)

screen.exitonclick()