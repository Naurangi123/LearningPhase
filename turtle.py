import turtle as t
import random

t=t.Turtle


colours=["cornflowerBlue","Darkblue","blue","green","yellow","lightyellow","lightGreen","seaGreen","grey"]


def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3,11):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)
