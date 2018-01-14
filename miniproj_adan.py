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
        if right_side_ball > screen_width/2:
            self.goto(new_x - self.dx,new_y)
        if left_side_ball < - screen_width/2:
            self.goto(new_x + self.dx,new_y)
        if up_side_ball > screen_hieght/2:
            self.goto(new_x , new_y - self.dy)
        if down_side_ball < - screen_hieght/2:
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


#PART 0
for i in range(NUMBER_OF_BALLS):
    X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
    Y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUUM_BALL_RADIUS)
    DX = random.randinit(MINIMUM_BALL_DX , MAXIMUM_BALL_DX )#how can we make  sure that the dx and dy are not 0
    DY = random.randinit(MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
    RADIUS = random.randinit(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    COLOR = (random.random(), random.random() , random.random())
    new_ball = Ball(X,Y,DX,DY,RADIUS,COLOR)
    Ball.append(new_ball)

# PART 1 

def move_balls(SCREEN_WIDTH,SCREEN_HEIGHT):
    random_place_x = random.randinit(-SCREEN_WIDTH + RADIUS , SCREEN_WIDTH-RADIUS)
    random_place_y = random.randinit(-SCREEN_HEIGHT + RADIUS , SCREEN_HEIGHT - RADIUS)
    new_ball.goto(random_place_x , random_place_y)
for balls in [BALLS]:
    new_ball.move_balls(SCREEN_WIDTH,SCREEN_HEIGHT)


#PART 2

def collide(ball_a,ball_b):
    if ball_a == ball_b
        return False
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d +10 <= ball_a.RADIUS + ball_b.RADIUS:
        return True
    else:
        return False


#part 3

def check_all_balls_collision():
    for ball_a in [BALLS]:
        for ball_b in [BALLS]:
            if ball_a.collide(ball_a,ball_b)== True:
                A_radius =  ball_a.RADIUS 
                B_radius = ball_b.RADIUS
                
    X_COORDINATE= random.randinit(-SCREEN_WIDTH + ball_a.RADIUS , SCREEN_WIDTH - a.RADIUS)
    Y_COORDINATE= random.randinit(-SCREEN_HEIGHT + ball_a.RADIUS , SCREEN_HEIGHT - a.RADIUS)
    X_AXISSPEED = random.randinit(                
    Y_AXISSPEED = random.randinit(
    Radius =random.randinit(
    Color =  
    

    

    
        










                   





























  
            
        
        
        
        
