#Total of number
total=0
for i in range(1,200):
    total+=i
    print(total)
#Turtle.py
import turtle as t
import random

tl=t.Turtle()


colours=["cornflowerBlue","Darkblue","blue","green","yellow","lightyellow","lightGreen","seaGreen","grey"]


def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tl.forward(100)
        tl.right(angle)


for shape_side_n in range(3,11):
    tl.color(random.choice(colours))
    draw_shape(shape_side_n)
