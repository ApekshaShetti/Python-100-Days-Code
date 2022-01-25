import paddle as t
from paddle import Screen
import random

new_paddlemy=t.paddle()
t.colormode(255)
new_paddlemy.shape("paddle")


# for _ in range(4):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(90)


# for _ in range(15):
#     new_paddlemy.forward(10)
#     new_paddlemy.penup()
#     new_paddlemy.forward(10)
#     new_paddlemy.pendown()

# for _ in range(3):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(120)
    
# for i in range(4):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(90)

# for i in range(5):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(72)

# for i in range(6):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(60)

# for i in range(7):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(51.4)

# for i in range(8):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(45)

# for i in range(9):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(40)

# for i in range(10):
#     new_paddlemy.forward(100)
#     new_paddlemy.right(36)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup
    
# colors=["Red","Yellow","Blue","Green","Violet","Purple"]
# directions=[0,90,180,270]
# new_paddlemy.pensize(15)
# new_paddlemy.speed("fastest")
# for _ in range(200):
#     # new_paddlemy.color(random.choice(colors))
#     new_paddlemy.color(random_color())
#     new_paddlemy.forward(20)
#     new_paddlemy.setheading(random.choice(directions))

new_paddlemy.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360/size)):
        new_paddlemy.color(random_color())
        new_paddlemy.circle(100)
        new_paddlemy.setheading(new_paddlemy.heading()+size)
draw_spirograph(5)

screen=Screen()
screen.exitonclick()
