import colorgram
import random
import turtle as turtle_module
# lista = []
# colors = colorgram.extract('image.jpg', 25)
#
# for coloring in colors:
#
#     r = coloring.rgb.r
#     g = coloring.rgb.g
#     b = coloring.rgb.b
#     new_color = (r, g, b)
#     lista.append(new_color)
#
# print(lista)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.shape("turtle")
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
dots = 100
for i in range(1, dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()