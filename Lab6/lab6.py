from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius)
        self.color(color)
        self.speed(speed)
ball1 = Ball(50,"blue",10)
ball2 = Ball(10,"red",10)

a = ball1.xcor()
b = ball1.ycor()
d = ball2.xcor()
c = ball2.ycor()
e = int(ball1.radius) + int(ball2.radius)
f = e/2 


def check_collision(ball1,ball2):
    if math.sqrt(math.pow((a-d),2) + math.pow((b-c),2)) == f:
        ball1.color() = ball2.color()
        ball2.color() = ball2.color()
    elif math.sqrt(math.pow((a-d),2) + math.pow((b-c),2))<f:
        ball2.color() = ball2.color()
        ball1.color() = ball2.color()
        print("slf")
    else :
        print("try again")

    
check_collision(ball1,ball2)
