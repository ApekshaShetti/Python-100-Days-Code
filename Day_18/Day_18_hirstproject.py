# import colorgram
from turtle import Screen
import turtle as t
import random
t.colormode(255)
new_Turtle=t.Turtle()

# colors=colorgram.extract('Day_18/image.jpg',30)
# print(colors)
# color_list=[]

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     tup=(r,g,b)
#     color_list.append(tup)
# print(color_list)

rgb_color=[(249, 246, 240), (240, 250, 246), (251, 243, 249), (241, 245, 250), (35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]
new_Turtle.penup()
new_Turtle.hideTurtle()
new_Turtle.speed("fastest")
new_Turtle.setheading(225)
new_Turtle.forward(250)
new_Turtle.setheading(0)

no_of_dots=100
for count in range(1,no_of_dots+1):
    new_Turtle.dot(20,random.choice(rgb_color))
    new_Turtle.forward(50)
    if count%10==0:
        new_Turtle.setheading(90)
        new_Turtle.forward(50)
        new_Turtle.setheading(180)
        new_Turtle.forward(500)
        new_Turtle.setheading(0)




screen=Screen()
screen.exitonclick()