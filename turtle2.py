import turtle
import colorsys
t=turtle.Turtle

turtle.Screen().bgcolor("black")
t.pensize(3)
t.speed(10)
n=90
h=6
for i in range(30):
    c=colorsys.hsv_to_rgb(h,1,0,7)
    h+=1/n
    t.pencolor(c)
    t.circle(180.360)
    t.backward(100)
    t.left(20)
    t.circle(60,50)
    t.right(85)
    t.forward(38)
    t.left(23)
turtle.done()
