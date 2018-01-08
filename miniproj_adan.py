import turtle
import math
import random
import time
from ball.py import Ball
class Ball(Turtle):
    def__init__(self,x,y,dx,dy,r,color):
        Turtle__init__(self)
        self.pendown()
        self.ypos(y)
        self.xpos(x)
        self.dx(dx)
        self.dy(dy)
        self.r(r)
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
    def move(self,screen_width,screen_hieght):
        current_x = self.xcor()
        new_x = current_x + self.dx()
        current_y = self.ycor()
        new_y = current_y + self.dy()
        right_side_ball = new_x + self.r()
        left_side_ball = new_x - self.r()
        up_side_ball = new_y + self.r()
        down_side_ball = new_y - self.r()
        self.goto(new_x,new_y)
        if right_side_ball > screen_width/2
            self.goto(new_x - self.dx,new_y)
        if left_side_ball < - screen_width/2
            self.goto(new_x + self.dx,new_y)
        if up_side_ball > screen_hieght/2
            self.goto(new_x , new_y - self.dy)
        if down_side_ball < - screen_hieght/2
            self.goto(new_x , new_y + self.dy)
  turtle.tracer(0,)
  turtle.hideturtle()
  RUNNING = True
  SLEEP = o.oo77
  SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
  SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(0,0,10,10,13,"green")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALLS_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
Y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUUM_BALL_RADIUS)
DX = random.randinit(MINIMUM_BALL-DX , MAXIMUM_BALL_DX )
DY = random.randinit(MINIMUM_BALL-DY , MAXIMUM_BALL_DY )
RADIUS = random.randinit(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
COLOR = (random.random(), random.random() , random.random())









                   





























  
            
        
        
        
        
