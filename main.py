# import colorgram
# colors = colorgram.extract("picture.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import turtle

color_list = [ (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
spot_num = 50
for spot_count in range(1, spot_num+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if spot_count %10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.pendown()
        tim.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
