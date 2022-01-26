from turtle import Turtle,Screen, clearscreen

new_Turtle=Turtle()
screen=Screen()

def move_forward():
    new_Turtle.forward(50)
def move_backward():
    new_Turtle.backward(50)
def clockwise():
    new_Turtle.right(50)
def counter_clockwise():
    new_Turtle.left(50)
def clear_scr():
    new_Turtle.clear()
    new_Turtle.penup()
    new_Turtle.home()
    new_Turtle.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_scr)
clear_scr()
screen.exitonclick()