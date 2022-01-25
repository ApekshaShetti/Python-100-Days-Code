from paddle import paddle,Screen, clearscreen

new_paddle=paddle()
screen=Screen()

def move_forward():
    new_paddle.forward(50)
def move_backward():
    new_paddle.backward(50)
def clockwise():
    new_paddle.right(50)
def counter_clockwise():
    new_paddle.left(50)
def clear_scr():
    new_paddle.clear()
    new_paddle.penup()
    new_paddle.home()
    new_paddle.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_scr)
clear_scr()
screen.exitonclick()