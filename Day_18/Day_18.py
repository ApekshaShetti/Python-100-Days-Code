import turtle as t
from turtle import Screen
import random

new_Turtlemy=t.Turtle()
t.colormode(255)
new_Turtlemy.shape("Turtle")


# for _ in range(4):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(90)


# for _ in range(15):
#     new_Turtlemy.forward(10)
#     new_Turtlemy.penup()
#     new_Turtlemy.forward(10)
#     new_Turtlemy.pendown()

# for _ in range(3):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(120)
    
# for i in range(4):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(90)

# for i in range(5):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(72)

# for i in range(6):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(60)

# for i in range(7):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(51.4)

# for i in range(8):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(45)

# for i in range(9):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(40)

# for i in range(10):
#     new_Turtlemy.forward(100)
#     new_Turtlemy.right(36)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup
    
# colors=["Red","Yellow","Blue","Green","Violet","Purple"]
# directions=[0,90,180,270]
# new_Turtlemy.pensize(15)
# new_Turtlemy.speed("fastest")
# for _ in range(200):
#     # new_Turtlemy.color(random.choice(colors))
#     new_Turtlemy.color(random_color())
#     new_Turtlemy.forward(20)
#     new_Turtlemy.setheading(random.choice(directions))

new_Turtlemy.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360/size)):
        new_Turtlemy.color(random_color())
        new_Turtlemy.circle(100)
        new_Turtlemy.setheading(new_Turtlemy.heading()+size)
draw_spirograph(5)

screen=Screen()
screen.exitonclick()
