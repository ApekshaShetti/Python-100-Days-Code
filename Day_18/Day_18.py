import turtle as t
from turtle import Screen
import random

timmy=t.Turtle()
t.colormode(255)
timmy.shape("turtle")


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120)
    
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(5):
#     timmy.forward(100)
#     timmy.right(72)

# for i in range(6):
#     timmy.forward(100)
#     timmy.right(60)

# for i in range(7):
#     timmy.forward(100)
#     timmy.right(51.4)

# for i in range(8):
#     timmy.forward(100)
#     timmy.right(45)

# for i in range(9):
#     timmy.forward(100)
#     timmy.right(40)

# for i in range(10):
#     timmy.forward(100)
#     timmy.right(36)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup
    
# colors=["Red","Yellow","Blue","Green","Violet","Purple"]
# directions=[0,90,180,270]
# timmy.pensize(15)
# timmy.speed("fastest")
# for _ in range(200):
#     # timmy.color(random.choice(colors))
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(directions))

timmy.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size)
draw_spirograph(5)

screen=Screen()
screen.exitonclick()
